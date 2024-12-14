from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Feedback
from .preprocessing import clean_feedback, validate_feedback, summarize_feedback

def feedback_view(request):
    if request.method == 'POST':
        # Extract feedback data
        feedback_data = {
            'course_id': request.POST.get('course_id'),
            'instructor': request.POST.get('instructor'),
            'rating': request.POST.get('rating'),
            'feedback_text': request.POST.get('feedback_text'),
        }

        # Validate feedback
        is_valid, message = validate_feedback(feedback_data)
        if not is_valid:
            return render(request, 'feedback/error.html', {'error': message})

        # Check for duplicates
        if Feedback.objects.filter(course_id=feedback_data['course_id'], instructor=feedback_data['instructor']).exists():
            return render(request, 'feedback/error.html', {'error': "Feedback already exists for this course and instructor."})

        # Clean and save feedback
        feedback_data['feedback_text'] = clean_feedback(feedback_data['feedback_text'])
        feedback = Feedback.objects.create(
            course_id=feedback_data['course_id'],
            instructor=feedback_data['instructor'],
            rating=feedback_data['rating'],
            content=feedback_data['feedback_text'],
            processed=False
        )

        # Process and summarize feedback
        feedback.processed_data = summarize_feedback(feedback_data['feedback_text'])
        feedback.processed = True
        feedback.save()

        return redirect('success')

    return render(request, 'feedback/feedback_form.html')

def success_view(request):
    return render(request, 'feedback/success.html')

def processed_feedback_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/processed_feedback.html', {'feedbacks': feedbacks})

def home(request):
    sample_feedback = "   This is a sample feedback for testing.   "
    cleaned = clean_feedback(sample_feedback)
    is_valid, message = validate_feedback({
        "feedback_text": cleaned,
        "course_id": "test_course",
        "instructor": "test_instructor",
        "rating": 5,
    })
    summary = summarize_feedback(cleaned)

    return JsonResponse({
        "original_feedback": sample_feedback,
        "cleaned_feedback": cleaned,
        "is_valid": is_valid,
        "validation_message": message,
        "summary": summary,
    })
