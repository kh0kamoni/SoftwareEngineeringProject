from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile, MealRecord, Transaction, MealSchedule, 
    Notice, Feast, GuestFeastRequest, Complaint, MealRate
)
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    meal_rate = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'room_number', 'mobile_number', 'balance', 
                 'meal_active', 'is_dining_manager', 'meal_type', 'meal_rate']
    
    def get_meal_rate(self, obj):
        return obj.get_meal_rate()

class MealRecordSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = MealRecord
        fields = ['id', 'user', 'date', 'meal_type', 'taken', 
                 'requested_for_night', 'meal_count']

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'transaction_type', 
                 'description', 'created_by', 'created_at']

class MealScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealSchedule
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Notice
        fields = ['id', 'title', 'description', 'date', 'attachment', 
                 'attachment_url', 'file_name']
    
    def get_attachment_url(self, obj):
        if obj.attachment:
            return obj.attachment.url
        return None
    
    def get_file_name(self, obj):
        return obj.get_file_name()

class FeastSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Feast
        fields = ['id', 'title', 'description', 'date', 'meal_time', 
                 'created_by', 'created_at']

class GuestFeastRequestSerializer(serializers.ModelSerializer):
    feast = FeastSerializer(read_only=True)
    
    class Meta:
        model = GuestFeastRequest
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Complaint
        fields = '__all__'

class MealRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealRate
        fields = '__all__'

# Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    room_number = serializers.CharField(required=True, max_length=10)
    mobile_number = serializers.CharField(required=True, max_length=15)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 
                 'last_name', 'room_number', 'mobile_number')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Create user profile
        UserProfile.objects.create(
            user=user,
            room_number=validated_data['room_number'],
            mobile_number=validated_data['mobile_number']
        )
        
        return user

# Update Profile Serializer
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['room_number', 'mobile_number', 'meal_type']

# Toggle Meal Status Serializer
class ToggleMealSerializer(serializers.Serializer):
    meal_active = serializers.BooleanField()

# Recharge Account Serializer
class RechargeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(required=False, allow_blank=True)

# Update Meal Count Serializer
class UpdateMealCountSerializer(serializers.Serializer):
    meal_type = serializers.ChoiceField(choices=MealRecord.MEAL_TYPES)
    meal_count = serializers.DecimalField(max_digits=4, decimal_places=2, min_value=0)
    date = serializers.DateField(required=False)

# Create Guest Feast Request Serializer
class CreateGuestFeastRequestSerializer(serializers.Serializer):
    guest_name = serializers.CharField(max_length=100)
    guest_mobile = serializers.CharField(max_length=15)
    requested_by_name = serializers.CharField(max_length=100)
    requested_by_mobile = serializers.CharField(max_length=15)

# Create Complaint Serializer
class CreateComplaintSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()

# Update Complaint Status Serializer
class UpdateComplaintStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Complaint._meta.get_field('status').choices)
    response = serializers.CharField(required=False, allow_blank=True)