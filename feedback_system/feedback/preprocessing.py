def clean_feedback(feedback):
    """Cleans the feedback text by trimming whitespace and removing invalid characters."""
    return feedback.strip()

def validate_feedback(feedback_data):
    """Validates feedback fields for completeness and accuracy."""
    if len(feedback_data.get('feedback_text', '')) <= 10:
        return False, "Feedback text must be longer than 10 characters."
    if not feedback_data.get('course_id') or not feedback_data.get('instructor'):
        return False, "Course ID and Instructor fields are required."
    return True, "Feedback is valid."

def summarize_feedback(feedback):
    """Generates a summary of the feedback text."""
    return feedback[:50]  # Summarizes to the first 50 characters
