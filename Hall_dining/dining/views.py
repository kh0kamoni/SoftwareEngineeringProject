from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Sum
from django.utils import timezone
from decimal import Decimal
import json
from django.http import JsonResponse
from .models import UserProfile, MealRecord, Transaction, MealSchedule, User, Notice, MealRate, Feast, GuestFeastRequest, Complaint
from .forms import UserRegisterForm, RechargeForm, MealScheduleForm, NoticeForm, MealRateForm, FeastForm, GuestFeastRequestForm, ComplaintForm, UserProfileForm
from django.http import FileResponse, Http404
from django.conf import settings
import os



def home(request):
    return render(request, 'dining/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            # Print form errors to debug
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'dining/register.html', {'form': form})



def is_dining_manager(user):
    try:
        return user.userprofile.is_dining_manager
    except UserProfile.DoesNotExist:
        return False



# @login_required
# def dashboard(request):
#     user_profile = get_object_or_404(UserProfile, user=request.user)
    
#     # Get today's meal records
#     today = timezone.now().date()
#     today_meals = MealRecord.objects.filter(user=request.user, date=today)
    
#     # Calculate total meals this month
#     month_start = timezone.now().replace(day=1)
#     total_meals_this_month = MealRecord.objects.filter(
#         user=request.user, 
#         date__gte=month_start,
#         taken=True
#     ).count()
    
#     context = {
#         'profile': user_profile,
#         'today_meals': today_meals,
#         'total_meals_this_month': total_meals_this_month,
#         'today': today,
#     }
#     return render(request, 'dining/dashboard.html', context)

# Individual Meal Count in Dashboard
@login_required
def dashboard(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    # Get today's meal records
    today = timezone.now().date()
    today_meals = MealRecord.objects.filter(user=request.user, date=today)
    
    # Calculate total meals this month
    month_start = timezone.now().replace(day=1)
    meal_records_this_month = MealRecord.objects.filter(
        user=request.user, 
        date__gte=month_start,
        taken=True
    )
    total_meals_this_month = meal_records_this_month.aggregate(
        total=Sum('meal_count')
    )['total'] or Decimal('0.00')
    
    # Calculate monthly meal cost
    monthly_meal_cost = total_meals_this_month * user_profile.get_meal_rate()
    
    # Get current meal rate
    current_rate = MealRate.objects.filter(effective_from__lte=timezone.now().date()).first()
    if not current_rate:
        current_rate = MealRate.objects.create(full_meal_rate=50.00, half_meal_rate=25.00)
    
    # Auto turn off meal if balance is 0 or negative
    if user_profile.balance <= 0 and user_profile.meal_active:
        user_profile.meal_active = False
        user_profile.save()
        messages.warning(request, 'Your meal has been automatically deactivated due to insufficient balance.')
    # Check today's meal status
    noon_record = MealRecord.objects.filter(
        user=request.user,
        date=today,
        meal_type='noon'
    ).first()
    
    dinner_record = MealRecord.objects.filter(
        user=request.user,
        date=today,
        meal_type='dinner'
    ).first()
    context = {
        'noon_taken': noon_record.taken if noon_record else False,
        'noon_requested_night': noon_record.requested_for_night if noon_record else False,
        'dinner_taken': dinner_record.taken if dinner_record else False,
        'profile': user_profile,
        'today_meals': today_meals,
        'total_meals_this_month': total_meals_this_month,
        'monthly_meal_cost': monthly_meal_cost,
        'current_rate': current_rate,
        'today': today,
    }
    return render(request, 'dining/dashboard.html', context)

@login_required
def toggle_meal_status(request):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.meal_active = not profile.meal_active
        profile.save()
        messages.success(request, f'Meal status changed to {"Active" if profile.meal_active else "Inactive"}')
    return redirect('dashboard')

@login_required
def request_meal_for_night(request):
    if request.method == 'POST':
        today = timezone.now().date()
        noon_meal, created = MealRecord.objects.get_or_create(
            user=request.user,
            date=today,
            meal_type='noon',
            defaults={'requested_for_night': True}
        )
        if not created:
            noon_meal.requested_for_night = True
            noon_meal.save()
        messages.success(request, 'Noon meal requested for night')
    return redirect('dashboard')


# @login_required
# @user_passes_test(is_dining_manager)
# def manager_dashboard(request):
#     # Search functionality
#     query = request.GET.get('q', '')
#     users = User.objects.all()
    
#     if query:
#         users = users.filter(
#             Q(userprofile__room_number__icontains=query) |
#             Q(first_name__icontains=query) |
#             Q(last_name__icontains=query) |
#             Q(userprofile__mobile_number__icontains=query)
#         )
    
#     # Today's meal records
#     today = timezone.now().date()
#     active_users = UserProfile.objects.filter(meal_active=True)
    
#     if request.method == 'POST':
#         # Handle meal tick marks
#         user_id = request.POST.get('user_id')
#         meal_type = request.POST.get('meal_type')
#         action = request.POST.get('action')
        
#         if user_id and meal_type:
#             user = get_object_or_404(User, id=user_id)
#             meal_record, created = MealRecord.objects.get_or_create(
#                 user=user,
#                 date=today,
#                 meal_type=meal_type
#             )
            
#             if action == 'toggle':
#                 meal_record.taken = not meal_record.taken
#             elif action == 'set_taken':
#                 meal_record.taken = True
#             elif action == 'set_not_taken':
#                 meal_record.taken = False
                
#             meal_record.save()
    
#     context = {
#         'users': users,
#         'active_users': active_users,
#         'today': today,
#         'query': query,
#     }
#     return render(request, 'dining/manager_dashboard.html', context)
@login_required
@user_passes_test(is_dining_manager)
def manager_dashboard(request):
    # Search functionality for all users
    query = request.GET.get('q', '')
    users = User.objects.all()
    
    if query:
        users = users.filter(
            Q(userprofile__room_number__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(userprofile__mobile_number__icontains=query)
        )
    
    # Today's meal records
    today = timezone.now().date()
    
    # Search functionality for active users tracking
    active_user_search = request.GET.get('active_user_search', '')
    active_users = UserProfile.objects.filter(meal_active=True).select_related('user')
    
    if active_user_search:
        active_users = active_users.filter(
            Q(room_number__icontains=active_user_search) |
            Q(user__first_name__icontains=active_user_search) |
            Q(user__last_name__icontains=active_user_search)
        )
    
    # Statistics for dashboard
    pending_guest_requests = GuestFeastRequest.objects.filter(status='pending').count()
    pending_complaints = Complaint.objects.filter(status='pending').count()
    
    # Today's meals taken (count unique users who have taken both meals)
    users_with_both_meals = User.objects.filter(
        mealrecord__date=today,
        mealrecord__taken=True,
        mealrecord__meal_type='noon'
    ).filter(
        mealrecord__date=today,
        mealrecord__taken=True,
        mealrecord__meal_type='dinner'
    ).distinct().count()
    today_meals_taken = users_with_both_meals
    
    # Low balance users (balance < 50)
    low_balance_users = UserProfile.objects.filter(balance__lt=50, meal_active=True)
    
    # Inactive users
    inactive_users = UserProfile.objects.filter(meal_active=False)
    
    # Current month start
    month_start = timezone.now().replace(day=1)
    
    if request.method == 'POST':
        # Handle meal tick marks
        user_id = request.POST.get('user_id')
        meal_type = request.POST.get('meal_type')
        action = request.POST.get('action')
        
        if user_id and meal_type:
            user = get_object_or_404(User, id=user_id)
            profile = user.userprofile
            
            # Get current state before changes
            noon_before = MealRecord.objects.filter(
                user=user, date=today, meal_type='noon', taken=True
            ).first()
            dinner_before = MealRecord.objects.filter(
                user=user, date=today, meal_type='dinner', taken=True
            ).first()
            had_both_meals_before = noon_before and dinner_before
            
            # Store previous balance for message
            previous_balance = profile.balance
            
            if action == 'toggle':
                # Toggle meal taken status
                meal_record, created = MealRecord.objects.get_or_create(
                    user=user,
                    date=today,
                    meal_type=meal_type,
                    defaults={'taken': True, 'meal_count': 1.0}
                )
                if not created:
                    meal_record.taken = not meal_record.taken
                    meal_record.save()
                    
            elif action == 'set_taken':
                # Set meal as taken
                meal_record, created = MealRecord.objects.get_or_create(
                    user=user,
                    date=today,
                    meal_type=meal_type,
                    defaults={'taken': True, 'meal_count': 1.0}
                )
                if not created and not meal_record.taken:
                    meal_record.taken = True
                    meal_record.save()
                    
            elif action == 'set_not_taken':
                # Set meal as not taken
                meal_record = MealRecord.objects.filter(
                    user=user,
                    date=today,
                    meal_type=meal_type
                ).first()
                if meal_record:
                    meal_record.taken = False
                    meal_record.save()
            
            # Handle meal deduction/refund logic
            noon_after = MealRecord.objects.filter(
                user=user, date=today, meal_type='noon', taken=True
            ).first()
            dinner_after = MealRecord.objects.filter(
                user=user, date=today, meal_type='dinner', taken=True
            ).first()
            
            had_both_meals_after = noon_after and dinner_after
            
            # Check if we need to deduct or refund
            meal_rate = profile.get_meal_rate()
            
            if had_both_meals_after and not had_both_meals_before:
                # Both meals are now taken - deduct cost
                
                # Check if deduction already made for today
                existing_deduction = Transaction.objects.filter(
                    user=user,
                    transaction_type='meal_deduction',
                    created_at__date=today
                ).exists()
                
                if not existing_deduction and profile.balance >= meal_rate:
                    profile.balance -= meal_rate
                    profile.save()
                    
                    Transaction.objects.create(
                        user=user,
                        amount=meal_rate,
                        transaction_type='meal_deduction',
                        description=f'Full day meal (Noon + Dinner) - Manager recorded',
                        created_by=request.user
                    )
                    messages.success(request, f'✅ Meal cost ৳{meal_rate} deducted from {user.get_full_name()}. New balance: ৳{profile.balance}')
                elif profile.balance < meal_rate:
                    messages.error(request, f'❌ Insufficient balance for {user.get_full_name()}. Balance: ৳{profile.balance}')
                    
            elif not had_both_meals_after and had_both_meals_before:
                # One meal was untaken - refund the cost
                
                # Find today's meal deduction transaction
                today_deduction = Transaction.objects.filter(
                    user=user,
                    transaction_type='meal_deduction',
                    created_at__date=today
                ).first()
                
                if today_deduction:
                    # Refund the amount
                    profile.balance += meal_rate
                    profile.save()
                    
                    # Create refund transaction
                    Transaction.objects.create(
                        user=user,
                        amount=meal_rate,
                        transaction_type='meal_refund',
                        description=f'Meal refund - One meal untaken by manager',
                        created_by=request.user
                    )
                    
                    messages.warning(request, f'🔄 Meal cost ৳{meal_rate} refunded to {user.get_full_name()}. New balance: ৳{profile.balance}')

    # Prefetch meal records for today for all active users and organize them
    today_meal_records = MealRecord.objects.filter(
        date=today,
        user__userprofile__in=active_users
    ).select_related('user')
    
    # Create a structured data for template
    user_meal_data = []
    for profile in active_users:
        user_meals = {
            'profile': profile,
            'noon_meal': None,
            'dinner_meal': None
        }
        
        # Find meal records for this user
        for record in today_meal_records:
            if record.user.id == profile.user.id:
                if record.meal_type == 'noon':
                    user_meals['noon_meal'] = record
                elif record.meal_type == 'dinner':
                    user_meals['dinner_meal'] = record
        
        user_meal_data.append(user_meals)
    
    context = {
        'users': users,
        'active_users': active_users,
        'user_meal_data': user_meal_data,
        'today': today,
        'query': query,
        'active_user_search': active_user_search,
        'pending_guest_requests': pending_guest_requests,
        'pending_complaints': pending_complaints,
        'today_meals_taken': today_meals_taken,
        'low_balance_users': low_balance_users,
        'inactive_users': inactive_users,
        'month_start': month_start,
    }
    return render(request, 'dining/manager_dashboard.html', context)
@login_required
@user_passes_test(is_dining_manager)
def recharge_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = RechargeForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = user
            transaction.transaction_type = 'recharge'
            transaction.created_by = request.user
            transaction.save()
            
            # Update user balance
            profile = user.userprofile
            profile.balance += transaction.amount
            profile.save()
            
            messages.success(request, f'Successfully recharged {transaction.amount} for {user.get_full_name()}')
            return redirect('manager_dashboard')
    else:
        form = RechargeForm()
    
    return render(request, 'dining/recharge.html', {'form': form, 'user': user})

@login_required
@user_passes_test(is_dining_manager)
def toggle_user_meal_status(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        profile = user.userprofile
        profile.meal_active = not profile.meal_active
        profile.save()
        messages.success(request, f'Meal status for {user.get_full_name()} changed to {"Active" if profile.meal_active else "Inactive"}')
    return redirect('manager_dashboard')

def active_users_view(request):
    today = timezone.now().date()
    active_users = UserProfile.objects.filter(meal_active=True)
    
    context = {
        'active_users': active_users,
        'today': today,
    }
    return render(request, 'dining/active_users.html', context)

def meal_schedule(request):
    today = timezone.now().date()
    schedule = MealSchedule.objects.filter(date=today).first()
    
    context = {
        'schedule': schedule,
        'today': today,
    }
    return render(request, 'dining/meal_schedule.html', context)


def download_attachment(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'notices', 'attachments', filename)
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404("File not found")

# Public view -所有人都可以看到
def notice_list(request):
    notices = Notice.objects.all().order_by('-date')
    return render(request, 'dining/notice_list.html', {'notices': notices})

# Dining manager only - create notice
@login_required
@user_passes_test(is_dining_manager)
def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save()
            messages.success(request, f'Notice "{notice.title}" created successfully!')
            return redirect('notice_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = NoticeForm()
    
    return render(request, 'dining/create_notice.html', {'form': form})

# Dining manager only - edit notice
@login_required
@user_passes_test(is_dining_manager)
def edit_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            notice = form.save()
            messages.success(request, f'Notice "{notice.title}" updated successfully!')
            return redirect('notice_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = NoticeForm(instance=notice)
    
    return render(request, 'dining/edit_notice.html', {'form': form, 'notice': notice})

# Dining manager only - delete notice
@login_required
@user_passes_test(is_dining_manager)
def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    
    if request.method == 'POST':
        title = notice.title
        notice.delete()
        messages.success(request, f'Notice "{title}" deleted successfully!')
        return redirect('notice_list')
    
    return render(request, 'dining/delete_notice.html', {'notice': notice})

# Notice detail view -所有人都可以看到
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'dining/notice_detail.html', {'notice': notice})


# Feast Management
@login_required
@user_passes_test(is_dining_manager)
def create_feast(request):
    if request.method == 'POST':
        form = FeastForm(request.POST)
        if form.is_valid():
            feast = form.save(commit=False)
            feast.created_by = request.user
            feast.save()
            messages.success(request, f'Feast "{feast.title}" created successfully!')
            return redirect('feast_list')
    else:
        form = FeastForm()
    return render(request, 'dining/create_feast.html', {'form': form})

def feast_list(request):
    feasts = Feast.objects.all().order_by('-date')
    return render(request, 'dining/feast_list.html', {'feasts': feasts})

def request_guest_feast(request, feast_id):
    feast = get_object_or_404(Feast, id=feast_id)
    
    if request.method == 'POST':
        form = GuestFeastRequestForm(request.POST)
        if form.is_valid():
            guest_request = form.save(commit=False)
            guest_request.feast = feast
            guest_request.save()
            messages.success(request, 'Guest feast request submitted successfully!')
            return redirect('feast_list')
    else:
        form = GuestFeastRequestForm()
    
    return render(request, 'dining/request_guest_feast.html', {'form': form, 'feast': feast})

@login_required
@user_passes_test(is_dining_manager)
def guest_feast_requests(request):
    requests = GuestFeastRequest.objects.all().order_by('-requested_at')
    return render(request, 'dining/guest_feast_requests.html', {'requests': requests})

@login_required
@user_passes_test(is_dining_manager)
def update_guest_request_status(request, request_id, status):
    guest_request = get_object_or_404(GuestFeastRequest, id=request_id)
    guest_request.status = status
    guest_request.save()
    messages.success(request, f'Guest request {status} successfully!')
    return redirect('guest_feast_requests')

# # Meal Rate Management
# @login_required
# @user_passes_test(is_dining_manager)
# def set_meal_rate(request):
#     current_rate = MealRate.objects.filter(effective_from__lte=timezone.now().date()).first()
    
#     if request.method == 'POST':
#         form = MealRateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Meal rates updated successfully!')
#             return redirect('set_meal_rate')
#     else:
#         form = MealRateForm(instance=current_rate)
    
#     return render(request, 'dining/set_meal_rate.html', {'form': form, 'current_rate': current_rate})
@login_required
@user_passes_test(is_dining_manager)
def set_meal_rate(request):
    # Get the most recent effective rate
    current_rate = MealRate.objects.filter(
        effective_from__lte=timezone.now().date()
    ).order_by('-effective_from').first()
    
    if request.method == 'POST':
        form = MealRateForm(request.POST)
        if form.is_valid():
            new_rate = form.save()
            messages.success(request, f'Meal rates updated successfully! Effective from {new_rate.effective_from}')
            return redirect('set_meal_rate')
    else:
        form = MealRateForm(instance=current_rate)
    
    # Get all rates for history display
    meal_rates = MealRate.objects.all().order_by('-effective_from')
    
    return render(request, 'dining/set_meal_rate.html', {
        'form': form, 
        'current_rate': current_rate,
        'meal_rates': meal_rates
    })

# Complaint System
@login_required
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    
    return render(request, 'dining/create_complaint.html', {'form': form})

@login_required
def complaint_list(request):
    if request.user.userprofile.is_dining_manager:
        complaints = Complaint.objects.all().order_by('-created_at')
    else:
        complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'dining/complaint_list.html', {'complaints': complaints})

@login_required
@user_passes_test(is_dining_manager)
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if request.method == 'POST':
        complaint.status = request.POST.get('status')
        complaint.response = request.POST.get('response', '')
        complaint.save()
        messages.success(request, 'Complaint status updated successfully!')
    
    return redirect('complaint_list')

# # Multiple Meal Support
# @login_required
# def update_meal_count(request):
#     if request.method == 'POST':
#         meal_type = request.POST.get('meal_type')
#         meal_count = Decimal(request.POST.get('meal_count', '1.0'))
#         date = timezone.now().date()
        
#         meal_record, created = MealRecord.objects.get_or_create(
#             user=request.user,
#             date=date,
#             meal_type=meal_type,
#             defaults={'meal_count': meal_count, 'taken': True}
#         )
        
#         if not created:
#             meal_record.meal_count = meal_count
#             meal_record.taken = True
#             meal_record.save()
        
#         # Deduct meal cost
#         profile = request.user.userprofile
#         meal_rate = profile.get_meal_rate()
#         cost = meal_count * meal_rate
        
#         if profile.balance >= cost:
#             profile.balance -= cost
#             profile.save()
            
#             # Record transaction
#             Transaction.objects.create(
#                 user=request.user,
#                 amount=cost,
#                 transaction_type='meal_deduction',
#                 description=f'{meal_type} meal - {meal_count} portion(s)',
#                 created_by=request.user
#             )
            
#             messages.success(request, f'Meal recorded successfully! ৳{cost} deducted.')
#         else:
#             messages.error(request, 'Insufficient balance for this meal.')
        
#         return redirect('dashboard')
@login_required
def update_meal_count(request):
    if request.method == 'POST':
        meal_type = request.POST.get('meal_type')
        requested_for_night = request.POST.get('requested_for_night') == 'true'
        date = timezone.now().date()
        profile = request.user.userprofile
        
        # Check if user has active meal
        if not profile.meal_active:
            messages.error(request, 'Your meal service is not active.')
            return redirect('dashboard')
        
        if meal_type == 'noon' and requested_for_night:
            # User is requesting to take noon meal at dinner time
            meal_record, created = MealRecord.objects.get_or_create(
                user=request.user,
                date=date,
                meal_type='noon',
                defaults={
                    'taken': False,
                    'requested_for_night': True,
                    'meal_count': 1.0
                }
            )
            
            if not created:
                if meal_record.taken:
                    messages.warning(request, 'Noon meal already taken today.')
                    return redirect('dashboard')
                meal_record.requested_for_night = True
                meal_record.save()
            
            messages.success(request, 'Noon meal requested for dinner time pickup.')
            return redirect('dashboard')
        
        # Regular meal recording
        if meal_type == 'noon':
            # Check if noon meal already exists
            existing_noon = MealRecord.objects.filter(
                user=request.user,
                date=date,
                meal_type='noon'
            ).first()
            
            if existing_noon:
                if existing_noon.taken:
                    messages.warning(request, 'Noon meal already taken today.')
                    return redirect('dashboard')
                # Update existing record
                existing_noon.taken = True
                existing_noon.requested_for_night = False
                existing_noon.save()
                meal_record = existing_noon
            else:
                # Create new record
                meal_record = MealRecord.objects.create(
                    user=request.user,
                    date=date,
                    meal_type='noon',
                    taken=True,
                    requested_for_night=False,
                    meal_count=1.0
                )
            
            messages.success(request, 'Noon meal recorded successfully!')
            
        elif meal_type == 'dinner':
            # Check if dinner already taken
            existing_dinner = MealRecord.objects.filter(
                user=request.user,
                date=date,
                meal_type='dinner',
                taken=True
            ).first()
            
            if existing_dinner:
                messages.warning(request, 'Dinner already taken today.')
                return redirect('dashboard')
            
            # Check if noon meal was requested for night pickup
            noon_meal_requested = MealRecord.objects.filter(
                user=request.user,
                date=date,
                meal_type='noon',
                requested_for_night=True,
                taken=False
            ).first()
            
            if noon_meal_requested:
                # Mark both noon and dinner as taken
                noon_meal_requested.taken = True
                noon_meal_requested.requested_for_night = False
                noon_meal_requested.save()
                
                dinner_meal = MealRecord.objects.create(
                    user=request.user,
                    date=date,
                    meal_type='dinner',
                    taken=True,
                    meal_count=1.0
                )
                
                # Deduct cost for both meals (2 portions)
                meal_rate = profile.get_meal_rate()
                cost = 2.0 * meal_rate
                
                if profile.balance >= cost:
                    profile.balance -= cost
                    profile.save()
                    
                    Transaction.objects.create(
                        user=request.user,
                        amount=cost,
                        transaction_type='meal_deduction',
                        description='Noon (night pickup) + Dinner - 2 portions',
                        created_by=request.user
                    )
                    
                    messages.success(request, f'Both noon (dinner pickup) and dinner recorded! ৳{cost} deducted.')
                else:
                    messages.error(request, 'Insufficient balance for meal deduction.')
                
            else:
                # Regular dinner recording
                dinner_meal = MealRecord.objects.create(
                    user=request.user,
                    date=date,
                    meal_type='dinner',
                    taken=True,
                    meal_count=1.0
                )
                
                # Check if both meals are taken for today (regular flow)
                noon_meal_taken = MealRecord.objects.filter(
                    user=request.user,
                    date=date,
                    meal_type='noon',
                    taken=True
                ).first()
                
                if noon_meal_taken:
                    # Both meals taken - deduct for full day (1 portion)
                    meal_rate = profile.get_meal_rate()
                    cost = 1.0 * meal_rate
                    
                    if profile.balance >= cost:
                        profile.balance -= cost
                        profile.save()
                        
                        Transaction.objects.create(
                            user=request.user,
                            amount=cost,
                            transaction_type='meal_deduction',
                            description='Full day meal (Noon + Dinner)',
                            created_by=request.user
                        )
                        
                        messages.success(request, f'Both meals recorded! ৳{cost} deducted for full day meal.')
                    else:
                        messages.error(request, 'Insufficient balance for meal deduction.')
                else:
                    # Only dinner taken - no deduction yet
                    messages.success(request, 'Dinner recorded. Mark noon meal to complete your daily meal.')
        
        return redirect('dashboard')

@login_required
def financial_summary(request):
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
    
    # Manager's current balance (recharges - expenses - meal deductions)
    manager_balance = total_recharges - total_expenses - total_meal_deductions
    
    # User balances
    total_user_balances = UserProfile.objects.aggregate(
        total=Sum('balance')
    )['total'] or Decimal('0.00')
    
    # Recent transactions
    recent_transactions = Transaction.objects.all().order_by('-created_at')[:10]
    
    # User balances list
    user_balances = UserProfile.objects.select_related('user').order_by('-balance')[:10]
    
    context = {
        'total_recharges': total_recharges,
        'total_meal_deductions': total_meal_deductions,
        'total_expenses': total_expenses,
        'manager_balance': manager_balance,
        'total_user_balances': total_user_balances,
        'recent_transactions': recent_transactions,
        'user_balances': user_balances,
    }
    
    return render(request, 'dining/financial_summary.html', context)

# Auto meal deactivation cron job (to be called daily)
def auto_deactivate_meals():
    users = UserProfile.objects.filter(meal_active=True, balance__lte=0)
    for user in users:
        user.meal_active = False
        user.save()
    print(f"Auto-deactivated meals for {users.count()} users")

# Update User Profile with meal type
@login_required
def update_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
        today = timezone.now().date()
        current_rates = MealRate.objects.filter(effective_from__lte=today).order_by('-effective_from').first()
    return render(request, 'dining/update_profile.html', {
        'form': form,
        'current_rates': current_rates,

    })

@login_required
def get_user_details(request, user_id):
    try:
        user_obj = User.objects.get(id=user_id)
        user_profile = user_obj.userprofile
        
        # Calculate monthly meals
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        monthly_meals = user_obj.mealrecord_set.filter(
            date__gte=month_start, 
            taken=True
        )
        monthly_meals_count = monthly_meals.count()
        monthly_meals_cost = user_profile.get_meal_rate() * monthly_meals_count
        
        user_data = {
            'room_number': user_profile.room_number,
            'mobile_number': user_profile.mobile_number,
            'email': user_obj.email,
            'balance': float(user_profile.balance),
            'meal_type': user_profile.meal_type.title(),
            'meal_active': user_profile.meal_active,
            'meal_rate': float(user_profile.get_meal_rate()),
            'monthly_meals_count': monthly_meals_count,
            'monthly_meals_cost': float(monthly_meals_cost),
        }
        
        return JsonResponse({
            'success': True,
            'user_data': user_data
        })
        
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'User not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
    


@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')