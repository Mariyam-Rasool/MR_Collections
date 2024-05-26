from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/',views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]