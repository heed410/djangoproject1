from django.urls import path
from . import views

#http://localhost/user
app_name='user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout,name='logout'),
]