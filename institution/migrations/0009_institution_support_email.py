# Generated by Django 2.0.2 on 2018-10-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0008_auto_20180626_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='support_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
