from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    Model for the direct messages.
    """
    owner = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name='receiver', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.receiver} {self.text}'
