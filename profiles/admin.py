"""
Register Profile model so that it appears in admin panel.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
