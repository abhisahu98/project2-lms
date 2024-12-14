from django.urls import path
from feedback import views  # Adjust import if needed

urlpatterns = [
    path('', views.feedback_view, name='feedback'),  # Map the root URL to the feedback form
    path('success/', views.success_view, name='success'),  # Success page after form submission
    path('processed_feedback/', views.processed_feedback_view, name='processed_feedback'),
    path('', views.home, name='home'),
]
