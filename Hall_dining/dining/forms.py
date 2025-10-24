from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Transaction, MealSchedule, Notice, Feast, GuestFeastRequest, Complaint, MealRate

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    room_number = forms.CharField(max_length=10, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'room_number', 'mobile_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Create user profile
            UserProfile.objects.create(
                user=user,
                room_number=self.cleaned_data['room_number'],
                mobile_number=self.cleaned_data['mobile_number']
            )
        return user

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['room_number', 'mobile_number']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['room_number', 'mobile_number', 'meal_type']

class RechargeForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class MealScheduleForm(forms.ModelForm):
    class Meta:
        model = MealSchedule
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'noon_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'noon_end_time': forms.TimeInput(attrs={'type': 'time'}),
            'dinner_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'dinner_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter notice title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter notice description'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Notice Title',
            'description': 'Description',
            'attachment': 'Attachment File',
        }

class MealRateForm(forms.ModelForm):
    class Meta:
        model = MealRate
        fields = ['full_meal_rate', 'half_meal_rate', 'effective_from']
        widgets = {
            'effective_from': forms.DateInput(attrs={'type': 'date'}),
        }

class FeastForm(forms.ModelForm):
    class Meta:
        model = Feast
        fields = ['title', 'description', 'date', 'meal_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class GuestFeastRequestForm(forms.ModelForm):
    class Meta:
        model = GuestFeastRequest
        fields = ['guest_name', 'guest_mobile', 'requested_by_name', 'requested_by_mobile']
        widgets = {
            'guest_name': forms.TextInput(attrs={'placeholder': 'Enter guest name'}),
            'guest_mobile': forms.TextInput(attrs={'placeholder': 'Enter guest mobile number'}),
            'requested_by_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'requested_by_mobile': forms.TextInput(attrs={'placeholder': 'Your mobile number'}),
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter complaint title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your complaint in detail'}),
        }