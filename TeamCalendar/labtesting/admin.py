from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Sprint, Part, Meeting, WikiArticle, KnowledgeArticle, Rapport, Task, Todo, GroupTask
"""
    The aim of that is to add all this OMR to the admin site.
    
    admin.site.register(ORM name)
"""
################################
admin.site.register(Sprint)
admin.site.register(Part)
admin.site.register(Meeting)
admin.site.register(WikiArticle)
admin.site.register(KnowledgeArticle)
admin.site.register(Todo)
admin.site.register(GroupTask)

class TaskAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':80})}
    }

admin.site.register(Task, TaskAdmin)

class RapportAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':80})}
    }
admin.site.register(Rapport, RapportAdmin)