from django.db import models

class Feedback(models.Model):
    course_id = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    rating = models.IntegerField()
    feedback_text = models.TextField()  # Store raw feedback
    processed_feedback = models.TextField(null=True, blank=True)  # Store processed feedback
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when feedback is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when feedback is updated
    processed = models.BooleanField(default=False)  # To track if the feedback has been processed
    processed_data = models.JSONField(null=True, blank=True)  # Store processed feedback data
    category = models.CharField(max_length=100, null=True, blank=True)  # Store feedback category

    def __str__(self):
        return f"Feedback for {self.course_id} by {self.instructor}"