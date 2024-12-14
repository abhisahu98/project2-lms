from celery import shared_task
from .models import Feedback
from .preprocessing import preprocess_feedback
from .gpt_integration import send_to_gpt
from feedback.preprocessing import preprocess_feedback


@shared_task
def process_feedback_task():
    feedbacks = Feedback.objects.filter(processed=False)
    for feedback in feedbacks:
        # Preprocess feedback
        preprocessed_data = preprocess_feedback(feedback.content)
        # Send to GPT
        gpt_response = send_to_gpt(preprocessed_data)
        # Save the processed feedback
        feedback.processed_data = gpt_response
        feedback.processed = True
        feedback.save()

# feedback/tasks.py

@shared_task
def process_feedback_task():
    # Your task logic to process feedback
    print("Processing feedback...")
    # Example: Fetch feedback data, process it, and save it back

