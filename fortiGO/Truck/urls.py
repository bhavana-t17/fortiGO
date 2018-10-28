from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Truck-home'),
    path('signup/',views.signup,name = 'Truck-signup'),
    path('register/',views.register,name = 'Truck-register')
]
