# Generated by Django 2.2.2 on 2019-07-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0058_auto_20190702_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='attributions',
            field=models.ManyToManyField(blank=True, limit_choices_to={'Attribution.Asociated_project': None}, to='funding.Attribution'),
        ),
    ]
