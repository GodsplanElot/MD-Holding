from django.urls import path
from .views import CustomLoginView, dashboard_view, signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to home after logout
    
]