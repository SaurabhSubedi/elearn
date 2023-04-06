from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginUser,name='login'),
    path('signup/',views.signupUser,name='signup'),
    path('logout/',views.logoutUser,name='logout'),
    path('reset-password/',auth_view.PasswordResetView.as_view(template_name = "password_reset.html"),name='reset_password'),
    path('reset-password-sent/',auth_view.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"),name='password_reset_done'),
    path('reset-password/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset-password-complete',auth_view.PasswordResetCompleteView.as_view(template_name = "password_reset_complete.html"),name='password_reset_complete'),
]