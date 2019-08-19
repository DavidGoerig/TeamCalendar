from django.db import models
from .choices import *
from django.utils import timezone

"""
    Database overview: https://drive.google.com/file/d/1iw1gKdBEAN5TSqEFqOGTkbSYH6brO5IE/view?usp=sharing
"""

class Information(models.Model):
    project_nbr = models.IntegerField()
    area = models.CharField(max_length=200, default="None")
    test_plan = models.CharField(max_length=200)
    responsable_name = models.CharField(max_length=200)
    eln_number = models.IntegerField()
    test_report = models.CharField(max_length=200)

"""
    Stores all project content.
    related to :model:`labtesting.Project`
"""
class Content(models.Model):
    experiment_goal = models.TextField()
    experiment_desc = models.TextField()
    experiment_focus = models.CharField(choices=FOCUS_CHOICES, default="All system", max_length=200)
    def __str__(self):
        return self.experiment_desc

"""
    Stores all project check field.
    related to :model:`labtesting.Project`
"""
class Checks(models.Model):
    check_test_setup = models.BooleanField(default=False)
    sample_prep_check = models.BooleanField(default=False)
    project_approval = models.BooleanField(default=False)

"""
    Define a Timeline day
    related to :model:`labtesting.Timeline`
"""
class TimelineDays(models.Model):
    day_nbr = models.IntegerField(default=0)
    measurment_comment = models.CharField(choices=MEASUREMENT_COMMENT_CHOICES, default="None", max_length=200)
    seq_name = models.CharField(max_length=200, default="Sequence")
    lvl_nbr = models.CharField(max_length=500, default="0")
    param = models.CharField(choices=PARAMETERS_CHOICES, default="pH", max_length=200)
    measurement_nbr = models.IntegerField(default=0)
    target_value = models.FloatField(default=0)
    acceptance_criteria = models.CharField(max_length=500, default="")
    sample_type = models.CharField(choices=SAMPLE_TYPE_CHOICES, default="Capillary", max_length=200)
    sample_matrix = models.CharField(choices=SAMPLE_MATRIX_CHOICES, default="Whole blood", max_length=200)
    pause_time = models.IntegerField(default=0)
    break_def = models.CharField(max_length=50, default="")

"""
    Define a level
    related to :model:`labtesting.Setup`
"""
class LevelDefinition(models.Model):
    lvl_nbr = models.IntegerField(default=0)
    measurement_nbr = models.IntegerField()
    target_value = models.FloatField()
    acceptance_criteria = models.CharField(max_length=500)

class Levels(models.Model):
    param = models.CharField(choices=PARAMETERS_CHOICES, default="pH", max_length=200)
    lvl_def = models.ManyToManyField(LevelDefinition, blank=True)
    def __str__(self):
        return self.param
"""
    Define a sequence
    related to :model:`labtesting.Setup`
"""
class SequenceDefinition(models.Model):
    order_number = models.IntegerField(default=0)
    param = models.CharField(max_length=50)
    level = models.CharField(max_length=500)
    pause_time = models.IntegerField(default=0)
    break_def = models.CharField(max_length=50, default="")
    def __str__(self):
        return (self.level + self.param)

class Sequences(models.Model):
    name = models.CharField(max_length=200, default="Sequence")
    sample_type = models.CharField(choices=SAMPLE_TYPE_CHOICES, default="Capillary", max_length=200)
    sample_matrix = models.CharField(choices=SAMPLE_MATRIX_CHOICES, default="Whole blood", max_length=200)
    seq = models.ManyToManyField(SequenceDefinition, blank=True)
    def __str__(self):
        return self.name

"""
    Define devices names
    related to :model:`labtesting.Setup`
"""
class DeviceNames(models.Model):
    name = models.CharField(max_length=200, default="None")
    is_reference = models.BooleanField(default=False)
    def __str__(self):
        return self.name


"""
    #TODO: delete it
"""
class ParametersNames(models.Model):
    name = models.CharField(choices=PARAMETERS_CHOICES, default="pH", max_length=200)
    def __str__(self):
        return self.name

"""
    Stores all project setup.
    related to :model:`labtesting.Project`
"""
class Setup(models.Model):
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=100, default="None")
    sample_prep_method = models.CharField(max_length=200, default="None")
    devices_names = models.ManyToManyField(DeviceNames, blank=True)
    seq_def = models.ManyToManyField(Sequences)
    levels = models.ManyToManyField(Levels)


"""
    Define name of instruments.
    related to :model:`labtesting.Instrument`
"""
class InstrumentDefinition(models.Model):
    name = models.CharField(max_length=150)
    device_id = models.IntegerField(default=0)
    def __str__(self):
        return self.name

"""
    Store the Instrument reservation.
    related to :model:`labtesting.Project`
"""
class Instrument(models.Model):
    confirmed_reservation = models.BooleanField(default=False)
    instruments = models.ManyToManyField(InstrumentDefinition)

"""
    Define the entire project.
"""
class Project(models.Model):
    is_template = models.BooleanField(default=False)
    project_name = models.CharField(max_length=200, unique=True)
    information = models.ForeignKey(Information, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE, blank=True, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True)
    timeline = models.ManyToManyField(TimelineDays)
    checks = models.ForeignKey(Checks, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.project_name

##################################################################

class Task(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Todo(models.Model):
    title = models.CharField(max_length=200)
    todo = models.ManyToManyField(Task)

class Meeting(models.Model):
    mail_alert = models.BooleanField(default=False)
    title  = models.CharField(max_length=200)
    date = models.DateField()
    descriptif = models.CharField(max_length=2000)

class WikiArticle(models.Model):
    links = models.CharField(max_length=500)
    descriptif = models.CharField(max_length=2000)

class Rapport(models.Model):
    auteur = models.CharField(choices=TEAM_CHOICES, default="David", max_length=200)
    nbr_of_points_todo = models.IntegerField(default=0)
    nbr_of_points_done = models.IntegerField(default=0)
    descriptif_done = models.TextField()

class KnowledgeArticle(models.Model):
    auteur = models.CharField(choices=TEAM_CHOICES, default="David", max_length=200)
    title = models.CharField(max_length=200, default="Title")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    field = models.CharField(choices=FIELD_CHOICES, default="SOFTWARE", max_length=200)
    descriptif = models.TextField()

class Part(models.Model):
    part_type = models.CharField(choices=PART_CHOICES, default="INTER SPRINT", max_length=200)
    meetings = models.ManyToManyField(Meeting)
    rapport_mensuel = models.ManyToManyField(Rapport)
    date_start = models.DateField()
    date_end = models.DateField()
    is_pld_update = models.BooleanField(default=False)
    is_meeting_ready = models.BooleanField(default=False)

class Sprint(models.Model):
    sprint_name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField(default=0)
    date_start = models.DateField()
    date_end = models.DateField()
    descriptif = models.CharField(max_length=2000)
    sprint_part = models.ManyToManyField(Part)