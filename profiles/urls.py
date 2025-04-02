from django.urls import path

from profiles import views
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import PasswordResetComplete

urlpatterns = [

    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    #ath("login_error/", views.login_error, name='login_error'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registrations\password_reset_done.html '), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registrations\password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    ]