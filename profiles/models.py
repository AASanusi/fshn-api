from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Parts taken from DRF-API walkthrough tutorial


class Profile(models.Model):
    """
    Model containing Profile information.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, default='About you')
    image = models.ImageField(
        upload_to='images/', default='../default_profile_bnyfgy'
    )

    class Meta:
        """
        Return Profile instances in reverse order (Recently created is first).
        """
        ordering = ['-created_at']

        """
        Return information on who Profile owner is.
        """
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a Profile when a new User is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
