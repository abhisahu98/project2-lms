from django.db import models
from django.utils.timezone import now

class Feedback(models.Model):
    course_id = models.CharField(max_length=100, default='default_course')  # Default for existing records
    instructor = models.CharField(max_length=100, default='Unknown Instructor')  # Default value for existing records
    rating = models.IntegerField()  # Rating for the course
    content = models.TextField()  # Feedback content
    processed = models.BooleanField(default=False)  # Processing status
    processed_data = models.TextField(null=True, blank=True)  # Processed feedback data
    created_at = models.DateTimeField(default=now)  # Default timestamp for existing records

    def __str__(self):
        return f"Feedback for {self.course_id} by {self.instructor}"
