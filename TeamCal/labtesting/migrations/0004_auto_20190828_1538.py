# Generated by Django 2.2 on 2019-08-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0003_auto_20190828_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikiarticle',
            old_name='name',
            new_name='wikiname',
        ),
        migrations.AlterField(
            model_name='grouptask',
            name='assigned_member',
            field=models.CharField(choices=[('William', 'William'), ('David', 'David'), ('Rodolphe', 'Rodolphe'), ('Hamid', 'Hamid'), ('Guillaume', 'Guillaume'), ('None', 'None'), ('Florian', 'Florian')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('David', 'David'), ('Rodolphe', 'Rodolphe'), ('Hamid', 'Hamid'), ('Guillaume', 'Guillaume'), ('Florian', 'Florian')], default='David', max_length=200),
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='field',
            field=models.CharField(choices=[('BACK END WEB', 'BACK END WEB'), ('SOFTWARE', 'SOFTWARE'), ('FRONT END WEB', 'FRONT END WEB'), ('MANAGEMENT', 'MANAGEMENT'), ('HARDWARE', 'HARDWARE'), ('IA', 'IA')], default='SOFTWARE', max_length=200),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_type',
            field=models.CharField(choices=[('FINAL PART', 'FINAL PART'), ('PRE FOLLOW UP', 'PRE FOLLOW UP'), ('INTER SPRINT', 'INTER SPRINT')], default='INTER SPRINT', max_length=200),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('David', 'David'), ('Rodolphe', 'Rodolphe'), ('Hamid', 'Hamid'), ('Guillaume', 'Guillaume'), ('Florian', 'Florian')], default='David', max_length=200),
        ),
    ]