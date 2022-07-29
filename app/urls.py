from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.forms import CustomerLoginForm, CustomerPasswordChangeForm, CustomerPasswordResetForm, CustomerSetPasswordForm
urlpatterns = [
    path('', views.home),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.CustomerRegistration.as_view(),
         name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                authentication_form=CustomerLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='app/changepassword.html', form_class=CustomerPasswordChangeForm, success_url='/login/'), name='changepassword'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='app/password-reset.html', form_class=CustomerPasswordResetForm), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password-reset-confirm.html', form_class=CustomerSetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password-reset-complete.html'), name='password_reset_complete'),

]
