from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        instructor = request.POST.get('instructor')
        rating = request.POST.get('rating')
        feedback_text = request.POST.get('feedback_text')

        # Check for duplicates
        if Feedback.objects.filter(course_id=course_id, instructor=instructor).exists():
            error_message = "Feedback for this course and instructor already exists."
            return render(request, 'feedback/feedback_form.html', {'error_message': error_message})

        # Save feedback to the database
        Feedback.objects.create(
            course_id=course_id,
            instructor=instructor,
            rating=rating,
            feedback_text=feedback_text
        )

        # Redirect to the success page
        return redirect('success')  # This redirects to the success page

    return render(request, 'feedback/feedback_form.html')
    

def success_view(request):
    return render(request, 'feedback/success.html')
