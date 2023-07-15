from django.urls import path
from bookstore_app import views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name="register"),
    path('login/', views.LoginAPI.as_view(), name="login"),
    path('profile/', views.WebsiteUserAPI.as_view(), name='profile'),
    path('logout/', views.LogoutAPI.as_view(), name='logout'),
    path('update/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('credit-card/', views.CreateCreditCard.as_view(), name='credit_card'),
]
