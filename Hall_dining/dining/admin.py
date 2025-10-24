from django.contrib import admin
from .models import UserProfile, MealRecord, Transaction, MealSchedule, Notice, MealRate, Feast, GuestFeastRequest, Complaint

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'room_number', 'mobile_number', 'balance', 'meal_active', 'is_dining_manager']
    list_filter = ['meal_active', 'is_dining_manager']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'room_number']

@admin.register(MealRecord)
class MealRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'meal_type', 'taken', 'requested_for_night']
    list_filter = ['date', 'meal_type', 'taken']
    search_fields = ['user__username', 'user__first_name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'created_by', 'created_at']
    list_filter = ['transaction_type', 'created_at']
    search_fields = ['user__username']

@admin.register(MealSchedule)
class MealScheduleAdmin(admin.ModelAdmin):
    list_display = ['date', 'noon_start_time', 'noon_end_time', 'dinner_start_time', 'dinner_end_time']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'get_file_name']
    list_filter = ['date']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'

@admin.register(MealRate)
class MealRateAdmin(admin.ModelAdmin):
    list_display = ['full_meal_rate', 'half_meal_rate', 'effective_from']
    list_filter = ['effective_from']

@admin.register(Feast)
class FeastAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'meal_time', 'created_by']
    list_filter = ['date', 'meal_time']

@admin.register(GuestFeastRequest)
class GuestFeastRequestAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'feast', 'status', 'requested_at']
    list_filter = ['status', 'feast']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description']