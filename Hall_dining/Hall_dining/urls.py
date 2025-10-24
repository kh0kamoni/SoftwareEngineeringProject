from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dining import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dining.api_urls')),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
     # Notice URLs
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notices/create/', views.create_notice, name='create_notice'),
    path('notices/<int:notice_id>/edit/', views.edit_notice, name='edit_notice'),
    path('notices/<int:notice_id>/delete/', views.delete_notice, name='delete_notice'),
    
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('active-users/', views.active_users_view, name='active_users'),
    path('meal-schedule/', views.meal_schedule, name='meal_schedule'),
    
    # Auth URLs - explicitly define them
    path('login/', auth_views.LoginView.as_view(template_name='dining/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # Dining app URLs
    path('toggle-meal-status/', views.toggle_meal_status, name='toggle_meal_status'),
    path('request-meal-for-night/', views.request_meal_for_night, name='request_meal_for_night'),
    path('recharge/<int:user_id>/', views.recharge_account, name='recharge_account'),
    path('toggle-user-meal/<int:user_id>/', views.toggle_user_meal_status, name='toggle_user_meal_status'),

     # New URLs for additional features
    path('feasts/', views.feast_list, name='feast_list'),
    path('feasts/create/', views.create_feast, name='create_feast'),
    path('feasts/<int:feast_id>/request-guest/', views.request_guest_feast, name='request_guest_feast'),
    path('guest-requests/', views.guest_feast_requests, name='guest_feast_requests'),
    path('guest-requests/<int:request_id>/<str:status>/', views.update_guest_request_status, name='update_guest_request_status'),
    
    path('meal-rate/', views.set_meal_rate, name='set_meal_rate'),
    
    path('complaints/', views.complaint_list, name='complaint_list'),
    path('complaints/create/', views.create_complaint, name='create_complaint'),
    path('complaints/<int:complaint_id>/update/', views.update_complaint_status, name='update_complaint_status'),
    
    path('update-meal-count/', views.update_meal_count, name='update_meal_count'),
    path('financial-summary/', views.financial_summary, name='financial_summary'),
    path('update-profile/', views.update_profile, name='update_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)