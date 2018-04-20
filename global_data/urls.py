# global_data/urls.py

from django.urls import path
from . import views

app_name = 'global_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
