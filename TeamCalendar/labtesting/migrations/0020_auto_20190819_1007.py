# Generated by Django 2.2 on 2019-08-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0019_auto_20190816_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgearticle',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('Guillaume', 'Guillaume'), ('Hamid', 'Hamid'), ('David', 'David'), ('Florian', 'Florian'), ('Rodolphe', 'Rodolphe')], default='David', max_length=200),
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='descriptif',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='field',
            field=models.CharField(choices=[('BACK END WEB', 'BACK END WEB'), ('IA', 'IA'), ('MANAGEMENT', 'MANAGEMENT'), ('FRONT END WEB', 'FRONT END WEB'), ('SOFTWARE', 'SOFTWARE'), ('HARDWARE', 'HARDWARE')], default='SOFTWARE', max_length=200),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('Guillaume', 'Guillaume'), ('Hamid', 'Hamid'), ('David', 'David'), ('Florian', 'Florian'), ('Rodolphe', 'Rodolphe')], default='David', max_length=200),
        ),
        migrations.AlterField(
            model_name='sequences',
            name='sample_type',
            field=models.CharField(choices=[('Syringe', 'Syringe'), ('Capillary', 'Capillary')], default='Capillary', max_length=200),
        ),
        migrations.AlterField(
            model_name='setup',
            name='project_type',
            field=models.CharField(choices=[('Linearity', 'Linearity'), ('Method comparison', 'Method comparison'), ('Precision', 'Precision'), ('Software verification', 'Software verification'), ('Throughput', 'Throughput'), ('Interference', 'Interference')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='timelinedays',
            name='sample_type',
            field=models.CharField(choices=[('Syringe', 'Syringe'), ('Capillary', 'Capillary')], default='Capillary', max_length=200),
        ),
    ]
