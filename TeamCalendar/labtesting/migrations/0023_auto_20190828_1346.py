# Generated by Django 2.2 on 2019-08-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtesting', '0022_auto_20190827_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_member', models.CharField(choices=[('William', 'William'), ('Florian', 'Florian'), ('Hamid', 'Hamid'), ('David', 'David'), ('Guillaume', 'Guillaume'), ('Rodolphe', 'Rodolphe'), ('None', 'None')], default='None', max_length=100)),
                ('task_name', models.CharField(max_length=200)),
                ('task_desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('Florian', 'Florian'), ('David', 'David'), ('Hamid', 'Hamid'), ('Guillaume', 'Guillaume'), ('Rodolphe', 'Rodolphe')], default='David', max_length=200),
        ),
        migrations.AlterField(
            model_name='knowledgearticle',
            name='field',
            field=models.CharField(choices=[('BACK END WEB', 'BACK END WEB'), ('MANAGEMENT', 'MANAGEMENT'), ('SOFTWARE', 'SOFTWARE'), ('FRONT END WEB', 'FRONT END WEB'), ('HARDWARE', 'HARDWARE'), ('IA', 'IA')], default='SOFTWARE', max_length=200),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='auteur',
            field=models.CharField(choices=[('William', 'William'), ('Florian', 'Florian'), ('David', 'David'), ('Hamid', 'Hamid'), ('Guillaume', 'Guillaume'), ('Rodolphe', 'Rodolphe')], default='David', max_length=200),
        ),
    ]