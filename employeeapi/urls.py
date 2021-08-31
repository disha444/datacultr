from django.urls import path
from . import views

urlpatterns = [
    path('empp/', views.find_data)
    ]


