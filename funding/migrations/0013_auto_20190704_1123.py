# Generated by Django 2.2.2 on 2019-07-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0012_auto_20190704_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribution',
            name='associated_to',
        ),
        migrations.RemoveField(
            model_name='historicalattribution',
            name='associated_to',
        ),
        migrations.RemoveField(
            model_name='historicalfundingsource',
            name='associated_to',
        ),
        migrations.RemoveField(
            model_name='historicalpublication',
            name='associated_to',
        ),
    ]