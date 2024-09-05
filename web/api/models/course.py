import uuid
from django.db import models
from .career import Career


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title
