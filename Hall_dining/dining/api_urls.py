from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import *

router = DefaultRouter()
router.register('user-profiles', UserProfileViewSet, basename='userprofile')
router.register('meal-records', MealRecordViewSet, basename='mealrecord')
router.register('transactions', TransactionViewSet, basename='transaction')
router.register('notices', NoticeViewSet, basename='notice')
router.register('feasts', FeastViewSet, basename='feast')
router.register('guest-requests', GuestFeastRequestViewSet, basename='guestfeastrequest')
router.register('complaints', ComplaintViewSet, basename='complaint')
router.register('meal-rates', MealRateViewSet, basename='mealrate')

urlpatterns = [
    # Authentication
    path('auth/login/', LoginView.as_view(), name='login'),  # Add this line
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('manager-dashboard/', ManagerDashboardView.as_view(), name='manager_dashboard'),
    path('financial-summary/', FinancialSummaryView.as_view(), name='financial_summary'),
    path('public-data/', PublicDataView.as_view(), name='public_data'),
    
    # API routes
    path('', include(router.urls)),
]