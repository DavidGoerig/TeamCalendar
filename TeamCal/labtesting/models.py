from django.db import models
from .choices import *
from django.utils import timezone

"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Task(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    desc = models.TextField()
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Todo(models.Model):
    title = models.CharField(max_length=200)
    todo = models.ManyToManyField(Task)
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Meeting(models.Model):
    mail_alert = models.BooleanField(default=False)
    title  = models.CharField(max_length=200)
    date = models.DateField()
    descriptif = models.CharField(max_length=2000)
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class WikiArticle(models.Model):
    links = models.CharField(max_length=500)
    descriptif = models.TextField()
    wikiname = models.CharField(max_length=200)
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Rapport(models.Model):
    auteur = models.CharField(choices=TEAM_CHOICES, default="David", max_length=200)
    nbr_of_points_todo = models.IntegerField(default=0)
    nbr_of_points_done = models.IntegerField(default=0)
    descriptif_done = models.TextField()
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class KnowledgeArticle(models.Model):
    auteur = models.CharField(choices=TEAM_CHOICES, default="David", max_length=200)
    title = models.CharField(max_length=200, default="Title")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    field = models.CharField(choices=FIELD_CHOICES, default="SOFTWARE", max_length=200)
    descriptif = models.TextField()
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Part(models.Model):
    part_type = models.CharField(choices=PART_CHOICES, default="INTER SPRINT", max_length=200)
    meetings = models.ManyToManyField(Meeting)
    rapport_mensuel = models.ManyToManyField(Rapport)
    date_start = models.DateField()
    date_end = models.DateField()
    is_pld_update = models.BooleanField(default=False)
    is_meeting_ready = models.BooleanField(default=False)
"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Sprint(models.Model):
    sprint_name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField(default=0)
    date_start = models.DateField()
    date_end = models.DateField()
    descriptif = models.CharField(max_length=2000)
    sprint_part = models.ManyToManyField(Part)

"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class GroupTask(models.Model):
    assigned_member = models.CharField(choices=TASK_CHOICES, default="None", max_length=100)
    task_name = models.CharField(max_length=200)
    task_desc = models.TextField()