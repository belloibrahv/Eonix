import uuid
from django.db import models

from .course import Course

class Topic(models.Model):
    """
    Represents a topic within a course. Topics can have subtopics, and each
    topic is associated with a course.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subtopics')

    def __str__(self):
        """Returns the string representation of the topic (its title)."""
        return self.title
