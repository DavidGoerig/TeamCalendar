# Generated by Django 2.2 on 2019-06-11 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequences',
            old_name='seq_def',
            new_name='seq',
        ),
    ]