from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('success/', views.success_view, name='success'),  # Define the success view
]
