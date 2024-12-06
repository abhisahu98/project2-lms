from django.db import models

class Feedback(models.Model):
    course_id = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255, default="Unknown")  # Default value added
    rating = models.IntegerField()
    feedback_text = models.TextField()

    def __str__(self):
        return f"{self.course_id} - {self.instructor}"
