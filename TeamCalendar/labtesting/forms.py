from django import forms
from .models import GroupTask, Sprint, Part, Meeting, WikiArticle, KnowledgeArticle, Rapport, Task, Todo

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)

"""
    All class for creating ORM's forms.
    
    class Meta define:
        which model is used
        which fields are used
"""


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'


class WikiArticleForm(forms.ModelForm):
    class Meta:
        model = WikiArticle
        fields = '__all__'


class KnowledgeArticleForm(forms.ModelForm):
    class Meta:
        model = KnowledgeArticle
        fields = '__all__'

class RapportForm(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = '__all__'

class GrouptaskForm(forms.ModelForm):
    class Meta:
        model = GroupTask
        fields = ('task_name', 'task_desc',)