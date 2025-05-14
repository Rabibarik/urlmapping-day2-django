from django.urls import path
from employee.views import *

urlpatterns = [
  path('', home, name='home'),
  path('home/', home, name='home'),
  path('login/', login, name='login')
]