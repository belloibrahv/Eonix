import uuid
from django.db import models


class Career(models.Model):
    """
    Represents a career path that users can follow. Each career
    has a title and description and tracks when it was created and updated.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the string representation of the career (its title)."""
        return self.title
