# Generated by Django 2.2 on 2019-06-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0008_remove_devicenames_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentdefinition',
            name='device_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='instrumentdefinition',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
