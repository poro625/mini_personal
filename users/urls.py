from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views


urlpatterns = [

    path('signup/', views.UserView.as_view(), name='user_signup'), #회원가입

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),

]
    
    

