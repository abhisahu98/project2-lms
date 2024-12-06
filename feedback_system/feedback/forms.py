from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text', 'rating', 'course_id', 'assessment_id']

# feedback/forms.py
def get_feedback_model():
    from .models import Feedback  # Local import to avoid circular imports
    return Feedback
