from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Sum
from django.utils import timezone
from decimal import Decimal
import json
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
    
    context = {
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
    
    # Today's meal records
    today = timezone.now().date()
    active_users = UserProfile.objects.filter(meal_active=True)
    
    # Statistics for dashboard
    pending_guest_requests = GuestFeastRequest.objects.filter(status='pending').count()
    pending_complaints = Complaint.objects.filter(status='pending').count()
    
    # Today's meals taken
    today_meals_taken = MealRecord.objects.filter(date=today, taken=True).count()
    
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
            meal_record, created = MealRecord.objects.get_or_create(
                user=user,
                date=today,
                meal_type=meal_type
            )
            
            if action == 'toggle':
                meal_record.taken = not meal_record.taken
            elif action == 'set_taken':
                meal_record.taken = True
            elif action == 'set_not_taken':
                meal_record.taken = False
                
            meal_record.save()
    
    context = {
        'users': users,
        'active_users': active_users,
        'today': today,
        'query': query,
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

# Multiple Meal Support
@login_required
def update_meal_count(request):
    if request.method == 'POST':
        meal_type = request.POST.get('meal_type')
        meal_count = Decimal(request.POST.get('meal_count', '1.0'))
        date = timezone.now().date()
        
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
        
        # Deduct meal cost
        profile = request.user.userprofile
        meal_rate = profile.get_meal_rate()
        cost = meal_count * meal_rate
        
        if profile.balance >= cost:
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
            
            messages.success(request, f'Meal recorded successfully! ৳{cost} deducted.')
        else:
            messages.error(request, 'Insufficient balance for this meal.')
        
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