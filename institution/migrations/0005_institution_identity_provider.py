# Generated by Django 2.0.2 on 2018-05-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20180326_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='identity_provider',
            field=models.URLField(blank=True),
        ),
    ]