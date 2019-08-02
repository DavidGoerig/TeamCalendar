from django import forms
from .models import Project, Information, Content, Checks, TimelineDays, LevelDefinition, SequenceDefinition, DeviceNames, ParametersNames, Setup, InstrumentDefinition, Instrument, Levels, Sequences
from homensettings.models import DevicesTypes, Area

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)

"""
    All class for creating ORM's forms.
    
    class Meta define:
        which model is used
        which fields are used
"""

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class InformationForm(forms.ModelForm):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), empty_label=None)
    class Meta:
        model = Information
        fields = '__all__'

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

class ChecksForm(forms.ModelForm):
    class Meta:
        model = Checks
        fields = '__all__'

class TimelineDaysForm(forms.ModelForm):
    class Meta:
        model = TimelineDays
        fields = '__all__'

class LevelDefinitionForm(forms.ModelForm):
    class Meta:
        model = LevelDefinition
        fields = '__all__'

class SequenceDefinitionForm(forms.ModelForm):
    break_def = forms.CharField(required=False)
    class Meta:
        model = SequenceDefinition
        fields = ('pause_time','break_def',)

class DeviceNamesForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=DevicesTypes.objects.all(), empty_label=None)
    class Meta:
        model = DeviceNames
        fields = '__all__'

class ParametersLevelForm(forms.ModelForm):
    class Meta:
        model = Levels
        fields = ('param',)

class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = ('project_type','sample_prep_method')

class InstrumentDefinitionForm(forms.ModelForm):
    class Meta:
        model = InstrumentDefinition
        fields = '__all__'

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'

class SequencesForm(forms.ModelForm):
    class Meta:
        model = Sequences
        fields = ('name', 'sample_matrix', 'sample_type',)