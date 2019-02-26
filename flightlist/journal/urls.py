from django.conf.urls import url
from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    path('journal', views.landing_page, name='landing_page'),
    path('login', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
]