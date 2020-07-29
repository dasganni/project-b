from django.urls import path
#from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    #path('change-user/<slug:username_slug>/', views.changeUser.as_view(), name="changeUser"),
    path('user_change/', views.changeUser.as_view(), name="user_change"),

    ]





    
 
    # path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),

    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # path('signup/', views.SignUp.as_view(), name="signup"),

    # path('password_change/', auth_views.PasswordChangeView.as_view(
    #     success_url = reverse_lazy("account_password_change_done"), 
    #     template_name = "accounts/changeUserPassword.html"
    # ), name="password_change"),

    # path('password_change/done/', auth_views.PasswordChangeView.as_view(
    #     template_name = "accounts/password_change_done.html"
    # ), name='password_change_done'),

    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #     success_url = reverse_lazy("account_login"), 
    #     template_name = "accounts/reset_password.html",
    #     email_template_name = "accounts/password_reset_email.html"
    # ), name='password_reset'),

    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name = "accounts/password_mail_send.html"
    # ), name='password_reset_done'),

    # path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     success_url = reverse_lazy("account_password_reset_complete"), 
    #     template_name = "accounts/reset_password.html"
    # ), name='password_reset_complete'),

    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name = "accounts/password_reset_complete.html"
    # ), name='password_reset_complete'),
 
