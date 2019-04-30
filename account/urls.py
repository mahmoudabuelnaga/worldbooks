from django.urls import path,include
from .views import SignUpView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/' , SignUpView.as_view(),name='signup'),
    path('password_change/',include('django.contrib.auth.urls'),name='password_change'),
    path('password_reset/' , include('django.contrib.auth.urls'), name='password_reset'),

]
