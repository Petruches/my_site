from django.contrib import admin
from .models import Experience, Me

# admin.site.register(Experience)
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_Experience = ('title', 'content', 'is_published')

@admin.register(Me)
class ExperienceAdmin(admin.ModelAdmin):
    list_Experience = ('title', 'content', 'is_published')
