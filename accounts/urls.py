from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # path('login/', views.login_view, name='login'),
    path('profile/',views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]