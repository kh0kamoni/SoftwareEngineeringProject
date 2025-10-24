from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q, Sum, Count
from django.utils import timezone
from decimal import Decimal
import json
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    UserProfile, MealRecord, Transaction, MealSchedule, 
    Notice, Feast, GuestFeastRequest, Complaint, MealRate
)
from .serializers import *

class IsDiningManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.is_dining_manager

class IsOwnerOrDiningManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.userprofile.is_dining_manager:
            return True
        return obj.user == request.user

from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        
        # Get user profile
        try:
            user_profile = UserProfile.objects.get(user=user)
            profile_serializer = UserProfileSerializer(user_profile)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "User profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        return Response({
            "user": UserSerializer(user).data,
            "profile": profile_serializer.data,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.userprofile.is_dining_manager:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UpdateProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def toggle_meal_status(self, request):
        profile = UserProfile.objects.get(user=request.user)
        profile.meal_active = not profile.meal_active
        profile.save()
        return Response({
            "message": f"Meal status changed to {'Active' if profile.meal_active else 'Inactive'}",
            "meal_active": profile.meal_active
        })
    
    @action(detail=True, methods=['post'], permission_classes=[IsDiningManager])
    def toggle_user_meal(self, request, pk=None):
        profile = self.get_object()
        profile.meal_active = not profile.meal_active
        profile.save()
        return Response({
            "message": f"Meal status for {profile.user.get_full_name()} changed to {'Active' if profile.meal_active else 'Inactive'}",
            "meal_active": profile.meal_active
        })
    
    @action(detail=True, methods=['post'], permission_classes=[IsDiningManager])
    def recharge(self, request, pk=None):
        profile = self.get_object()
        serializer = RechargeSerializer(data=request.data)
        
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            description = serializer.validated_data.get('description', 'Account recharge')
            
            # Update balance
            profile.balance += amount
            profile.save()
            
            # Create transaction
            Transaction.objects.create(
                user=profile.user,
                amount=amount,
                transaction_type='recharge',
                description=description,
                created_by=request.user
            )
            
            return Response({
                "message": f"Successfully recharged ৳{amount} for {profile.user.get_full_name()}",
                "new_balance": profile.balance
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MealRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDiningManager]
    
    def get_queryset(self):
        if self.request.user.userprofile.is_dining_manager:
            return MealRecord.objects.all()
        return MealRecord.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        today = timezone.now().date()
        records = MealRecord.objects.filter(user=request.user, date=today)
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def update_meal_count(self, request):
        serializer = UpdateMealCountSerializer(data=request.data)
        
        if serializer.is_valid():
            meal_type = serializer.validated_data['meal_type']
            meal_count = serializer.validated_data['meal_count']
            date = serializer.validated_data.get('date', timezone.now().date())
            
            profile = request.user.userprofile
            meal_rate = profile.get_meal_rate()
            cost = meal_count * meal_rate
            
            # Check balance
            if profile.balance < cost:
                return Response(
                    {"error": "Insufficient balance for this meal"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create or update meal record
            meal_record, created = MealRecord.objects.get_or_create(
                user=request.user,
                date=date,
                meal_type=meal_type,
                defaults={'meal_count': meal_count, 'taken': True}
            )
            
            if not created:
                meal_record.meal_count = meal_count
                meal_record.taken = True
                meal_record.save()
            
            # Deduct from balance
            profile.balance -= cost
            profile.save()
            
            # Record transaction
            Transaction.objects.create(
                user=request.user,
                amount=cost,
                transaction_type='meal_deduction',
                description=f'{meal_type} meal - {meal_count} portion(s)',
                created_by=request.user
            )
            
            return Response({
                "message": f"Meal recorded successfully! ৳{cost} deducted.",
                "new_balance": profile.balance
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], permission_classes=[IsDiningManager])
    def mark_meal_taken(self, request):
        user_id = request.data.get('user_id')
        meal_type = request.data.get('meal_type')
        date = request.data.get('date', timezone.now().date())
        
        user = User.objects.get(id=user_id)
        meal_record, created = MealRecord.objects.get_or_create(
            user=user,
            date=date,
            meal_type=meal_type
        )
        meal_record.taken = True
        meal_record.save()
        
        return Response({"message": f"Meal marked as taken for {user.get_full_name()}"})

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDiningManager]
    
    def get_queryset(self):
        if self.request.user.userprofile.is_dining_manager:
            return Transaction.objects.all()
        return Transaction.objects.filter(user=self.request.user)

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notice.objects.all().order_by('-date')
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsDiningManager]
        return super().get_permissions()

class FeastViewSet(viewsets.ModelViewSet):
    serializer_class = FeastSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Feast.objects.all().order_by('-date')
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsDiningManager]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GuestFeastRequestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestFeastRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.userprofile.is_dining_manager:
            return GuestFeastRequest.objects.all().order_by('-requested_at')
        return GuestFeastRequest.objects.filter(requested_by_mobile=self.request.user.userprofile.mobile_number)
    
    def create(self, request):
        serializer = CreateGuestFeastRequestSerializer(data=request.data)
        if serializer.is_valid():
            feast_id = request.data.get('feast_id')
            feast = Feast.objects.get(id=feast_id)
            
            guest_request = GuestFeastRequest.objects.create(
                feast=feast,
                **serializer.validated_data
            )
            
            return Response(
                GuestFeastRequestSerializer(guest_request).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], permission_classes=[IsDiningManager])
    def update_status(self, request, pk=None):
        guest_request = self.get_object()
        status = request.data.get('status')
        
        if status in ['approved', 'rejected']:
            guest_request.status = status
            guest_request.save()
            return Response({"message": f"Guest request {status} successfully"})
        
        return Response(
            {"error": "Invalid status"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

class ComplaintViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.userprofile.is_dining_manager:
            return Complaint.objects.all().order_by('-created_at')
        return Complaint.objects.filter(user=self.request.user).order_by('-created_at')
    
    def create(self, request):
        serializer = CreateComplaintSerializer(data=request.data)
        if serializer.is_valid():
            complaint = Complaint.objects.create(
                user=request.user,
                **serializer.validated_data
            )
            return Response(
                ComplaintSerializer(complaint).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], permission_classes=[IsDiningManager])
    def update_status(self, request, pk=None):
        complaint = self.get_object()
        serializer = UpdateComplaintStatusSerializer(data=request.data)
        
        if serializer.is_valid():
            complaint.status = serializer.validated_data['status']
            complaint.response = serializer.validated_data.get('response', '')
            complaint.save()
            return Response({"message": "Complaint status updated successfully"})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealRateViewSet(viewsets.ModelViewSet):
    serializer_class = MealRateSerializer
    permission_classes = [IsDiningManager]
    
    def get_queryset(self):
        return MealRate.objects.all().order_by('-effective_from')

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        profile = request.user.userprofile
        today = timezone.now().date()
        month_start = timezone.now().replace(day=1).date()
        
        # Today's meal records
        today_meals = MealRecord.objects.filter(user=request.user, date=today)
        
        # Monthly meal statistics
        monthly_meals = MealRecord.objects.filter(
            user=request.user, 
            date__gte=month_start,
            taken=True
        )
        total_meals_this_month = monthly_meals.aggregate(
            total=Sum('meal_count')
        )['total'] or Decimal('0.00')
        
        monthly_meal_cost = total_meals_this_month * profile.get_meal_rate()
        
        # Auto deactivate meal if balance is 0
        if profile.balance <= 0 and profile.meal_active:
            profile.meal_active = False
            profile.save()
        
        return Response({
            'profile': UserProfileSerializer(profile).data,
            'today_meals': MealRecordSerializer(today_meals, many=True).data,
            'monthly_stats': {
                'total_meals': total_meals_this_month,
                'total_cost': monthly_meal_cost,
            }
        })

class ManagerDashboardView(APIView):
    permission_classes = [IsDiningManager]
    
    def get(self, request):
        # Statistics
        active_users = UserProfile.objects.filter(meal_active=True).count()
        pending_guest_requests = GuestFeastRequest.objects.filter(status='pending').count()
        pending_complaints = Complaint.objects.filter(status='pending').count()
        
        # Today's meals taken
        today = timezone.now().date()
        today_meals_taken = MealRecord.objects.filter(date=today, taken=True).count()
        
        # Low balance users
        low_balance_users = UserProfile.objects.filter(
            balance__lt=50, meal_active=True
        ).count()
        
        # Search functionality
        query = request.GET.get('q', '')
        users = User.objects.all()
        if query:
            users = users.filter(
                Q(userprofile__room_number__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(userprofile__mobile_number__icontains=query)
            )
        
        return Response({
            'stats': {
                'active_users': active_users,
                'pending_guest_requests': pending_guest_requests,
                'pending_complaints': pending_complaints,
                'today_meals_taken': today_meals_taken,
                'low_balance_users': low_balance_users,
            },
            'users': UserProfileSerializer(
                UserProfile.objects.filter(user__in=users), 
                many=True
            ).data,
            'active_users_list': UserProfileSerializer(
                UserProfile.objects.filter(meal_active=True),
                many=True
            ).data,
        })

class FinancialSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Total recharges
        total_recharges = Transaction.objects.filter(
            transaction_type='recharge'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Total meal deductions
        total_meal_deductions = Transaction.objects.filter(
            transaction_type='meal_deduction'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Total expenses
        total_expenses = Transaction.objects.filter(
            transaction_type='expense'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Manager's current balance
        manager_balance = total_recharges - total_expenses - total_meal_deductions
        
        # User balances
        total_user_balances = UserProfile.objects.aggregate(
            total=Sum('balance')
        )['total'] or Decimal('0.00')
        
        # Recent transactions
        recent_transactions = Transaction.objects.all().order_by('-created_at')[:10]
        
        # User balances list
        user_balances = UserProfile.objects.select_related('user').order_by('-balance')[:10]
        
        return Response({
            'total_recharges': total_recharges,
            'total_meal_deductions': total_meal_deductions,
            'total_expenses': total_expenses,
            'manager_balance': manager_balance,
            'total_user_balances': total_user_balances,
            'recent_transactions': TransactionSerializer(recent_transactions, many=True).data,
            'user_balances': UserProfileSerializer(user_balances, many=True).data,
        })

class PublicDataView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        # Active users (public view)
        active_users = UserProfile.objects.filter(meal_active=True)
        
        # Today's meal schedule
        today = timezone.now().date()
        meal_schedule = MealSchedule.objects.filter(date=today).first()
        
        # Notices
        notices = Notice.objects.all().order_by('-date')[:10]
        
        # Feasts
        feasts = Feast.objects.filter(date__gte=today).order_by('date')[:5]
        
        return Response({
            'active_users': UserProfileSerializer(active_users, many=True).data,
            'meal_schedule': MealScheduleSerializer(meal_schedule).data if meal_schedule else None,
            'notices': NoticeSerializer(notices, many=True).data,
            'feasts': FeastSerializer(feasts, many=True).data,
        })