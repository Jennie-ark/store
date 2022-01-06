from django.urls import path

from user.views import login, register, profile, logout

app_name = 'login'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
