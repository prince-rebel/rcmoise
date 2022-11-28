from django.urls import path
from re import template
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout',views.logout_view,name='logout_view'),
    path('password_forget/',
        auth_views.PasswordResetView.as_view(template_name='index.html') ,
         name="password_forget"),

    path('password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='index.html'),
        name="password_reset_done"),   

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='index.html'),
        name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='index.html') ,
        name="password_reset_complete"),
    path('edit_password/',
        auth_views.PasswordChangeView.as_view(template_name='index.html'),name="password_change"
    ),

]