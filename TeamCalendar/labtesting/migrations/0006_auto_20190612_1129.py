# Generated by Django 2.2 on 2019-06-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0005_auto_20190612_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelinedays',
            name='lvl_nbr',
            field=models.CharField(default='0', max_length=500),
        ),
    ]
