import uuid
from django.db import models
from .career import Career


class Course(models.Model):
    """
    Represents a course within a specific career path.
    Each course belongs to a career and tracks completion status.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        """Returns the string representation of the course (its title)."""
        return self.title
