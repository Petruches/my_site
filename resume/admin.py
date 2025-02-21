from django.contrib import admin
from .models import Experience

# admin.site.register(Experience)
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_Experience = ('title', 'content', 'is_published')
