# Generated by Django 2.0.2 on 2018-02-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20180215_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.TextField(blank=True, max_length=512),
        ),
    ]
