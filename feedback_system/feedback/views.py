from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        instructor = request.POST.get('instructor')
        rating = request.POST.get('rating')
        feedback_text = request.POST.get('feedback_text')

        # Save feedback to the database
        Feedback.objects.create(
            course_id=course_id,
            instructor=instructor,
            rating=rating,
            feedback_text=feedback_text
        )
        # Redirect to success page after form submission
        return redirect('success')  # You need to define 'success' URL pattern in your urls.py
    return render(request, 'feedback/feedback_form.html')

def success_view(request):
    return render(request, 'feedback/success.html')
