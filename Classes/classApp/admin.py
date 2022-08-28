from django.contrib import admin
# importing specific model from model.py so it can be registering within the page
from .models import UniversityClasses

# registering model
admin.site.register(UniversityClasses)
