from django.contrib import admin
from .models import *


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    
class workExperienceInline(admin.TabularInline):
    model = workExperience
    extra = 1
    
class AcademicInline(admin.TabularInline):
    model = Academic
    extra = 1
    
class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1
    
class RefereeInline(admin.TabularInline):
    model = Referee
    extra = 1 
    
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1   
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email')
    inlines= [ LanguageInline, AcademicInline, HobbyInline, workExperienceInline, 
            RefereeInline, ProjectInline, SkillInline]
    fieldsets = (("Basic Info", {"name", "bio", "photo", "email", "linkedin"}),)
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('name','email','subject', 'message', 'created_at')
    
    
admin.site.register(Profile)
admin.site.register(workExperience)
admin.site.register(Hobby)
admin.site.register(Referee)
admin.site.register(Academic)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Language)