from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os
from decimal import Decimal


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     room_number = models.CharField(max_length=10)
#     mobile_number = models.CharField(max_length=15)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     meal_active = models.BooleanField(default=True)
#     is_dining_manager = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.user.get_full_name()} - Room {self.room_number}"
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     room_number = models.CharField(max_length=10)
#     mobile_number = models.CharField(max_length=15)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     meal_active = models.BooleanField(default=True)
#     is_dining_manager = models.BooleanField(default=False)
#     meal_type = models.CharField(max_length=10, choices=[
#         ('full', 'Full Meal'),
#         ('half', 'Half Meal')
#     ], default='full')
    
#     def __str__(self):
#         return f"{self.user.get_full_name()} - Room {self.room_number}"
    
#     def get_meal_rate(self):
#         current_rate = MealRate.objects.filter(effective_from__lte=timezone.now().date()).first()
#         if not current_rate:
#             current_rate = MealRate.objects.create(full_meal_rate=50.00, half_meal_rate=25.00)
        
#         if self.meal_type == 'half':
#             return current_rate.half_meal_rate
#         return current_rate.full_meal_rate

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    meal_active = models.BooleanField(default=True)
    is_dining_manager = models.BooleanField(default=False)
    meal_type = models.CharField(max_length=10, choices=[
        ('full', 'Full Meal'),
        ('half', 'Half Meal')
    ], default='full')
    
    def __str__(self):
        return f"{self.user.get_full_name()} - Room {self.room_number}"
    
    def get_meal_rate(self):
        # Get the most recent effective rate
        current_rate = MealRate.objects.filter(
            effective_from__lte=timezone.now().date()
        ).order_by('-effective_from').first()
        
        if not current_rate:
            # Return sensible defaults instead of creating objects
            # Or raise an exception to alert admins
            return Decimal('50.00') if self.meal_type == 'full' else Decimal('25.00')
        
        if self.meal_type == 'half':
            return current_rate.half_meal_rate
        return current_rate.full_meal_rate

# class MealRecord(models.Model):
#     MEAL_TYPES = [
#         ('noon', 'Noon Meal'),
#         ('dinner', 'Dinner'),
#     ]
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(default=timezone.now)
#     meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
#     taken = models.BooleanField(default=False)
#     requested_for_night = models.BooleanField(default=False)
    
#     class Meta:
#         unique_together = ['user', 'date', 'meal_type']
    
#     def __str__(self):
#         return f"{self.user.username} - {self.date} - {self.meal_type}"

class MealRecord(models.Model):
    MEAL_TYPES = [
        ('noon', 'Noon Meal'),
        ('dinner', 'Dinner'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    taken = models.BooleanField(default=False)
    requested_for_night = models.BooleanField(default=False)
    meal_count = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)  # 1.0, 2.0, 0.5 etc.
    
    class Meta:
        unique_together = ['user', 'date', 'meal_type']
    
    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.meal_type}"
    
class MealRate(models.Model):
    full_meal_rate = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    half_meal_rate = models.DecimalField(max_digits=10, decimal_places=2, default=25.00)
    effective_from = models.DateField(default=timezone.now)
    
    class Meta:
        verbose_name = "Meal Rate"
        verbose_name_plural = "Meal Rates"
        ordering = ['-effective_from']
    
    def __str__(self):
        return f"Full: ৳{self.full_meal_rate}, Half: ৳{self.half_meal_rate}"

# class Transaction(models.Model):
#     TRANSACTION_TYPES = [
#         ('recharge', 'Recharge'),
#         ('meal_deduction', 'Meal Deduction'),
#     ]
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
#     description = models.TextField(blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_transactions')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user.username} - {self.transaction_type} - {self.amount}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('recharge', 'Recharge'),
        ('meal_deduction', 'Meal Deduction'),
        ('expense', 'Expense'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username if self.user else 'System'} - {self.transaction_type} - {self.amount}"

class MealSchedule(models.Model):
    date = models.DateField(unique=True)
    noon_meal_items = models.TextField()
    dinner_meal_items = models.TextField()
    noon_start_time = models.TimeField()
    noon_end_time = models.TimeField()
    dinner_start_time = models.TimeField()
    dinner_end_time = models.TimeField()
    
    def __str__(self):
        return f"Meal Schedule - {self.date}"
    
class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    attachment = models.FileField(upload_to='notices/attachments/', blank=True, null=True, verbose_name="Attachment")
    
    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
    def get_file_name(self):
        return os.path.basename(self.attachment.name) if self.attachment else None
    
class Feast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    meal_time = models.CharField(max_length=10, choices=[('noon', 'Noon'), ('dinner', 'Dinner')])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Feast"
        verbose_name_plural = "Feasts"
        ordering = ['-date']
    
    def __str__(self):
        return self.title

class GuestFeastRequest(models.Model):
    feast = models.ForeignKey(Feast, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    guest_mobile = models.CharField(max_length=15)
    requested_by_name = models.CharField(max_length=100)
    requested_by_mobile = models.CharField(max_length=15)
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    
    class Meta:
        verbose_name = "Guest Feast Request"
        verbose_name_plural = "Guest Feast Requests"
    
    def __str__(self):
        return f"{self.guest_name} - {self.feast.title}"

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected')
    ], default='pending')
    response = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title