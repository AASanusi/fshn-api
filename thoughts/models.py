from django.db import models
from django.contrib.auth.models import User


class Thought(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    current_location = models.TextField(max_length=25, blank=True)
    mood_choices = [
        ('normal', 'Normal'),
        ('sad', 'Sad'),
        ('happy', 'Happy'),
        ('anxious', 'Anxious'),
        ('romantic', 'Romantic'),
        ('hopeful', 'Hopeful'),
        ('angry', 'Angry'),
        ('lonely', 'Lonely'),
        ('cheerful', 'Cheerful'),
        ('excited', 'Excited')
    ]
    mood_selector = models.CharField(
        max_length=32, choices=mood_choices, default=''
    )
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
