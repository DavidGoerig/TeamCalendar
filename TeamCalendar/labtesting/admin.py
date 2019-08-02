from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Levels, Information, Content, Checks, TimelineDays, LevelDefinition, SequenceDefinition, DeviceNames, ParametersNames, Setup, InstrumentDefinition, Instrument,Project, Sequences

"""
    The aim of that is to add all this OMR to the admin site.
    
    admin.site.register(ORM name)
"""


admin.site.register(Levels)
admin.site.register(Project)
admin.site.register(Information)
admin.site.register(Checks)
admin.site.register(TimelineDays)
admin.site.register(LevelDefinition)
admin.site.register(SequenceDefinition)
admin.site.register(DeviceNames)
admin.site.register(ParametersNames)
admin.site.register(Setup)
admin.site.register(InstrumentDefinition)
admin.site.register(Instrument)
admin.site.register(Sequences)

class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}
    }

admin.site.register(Content, ContentAdmin)