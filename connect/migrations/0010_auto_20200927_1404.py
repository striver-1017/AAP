# Generated by Django 3.1 on 2020-09-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0009_webinar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='Link',
            field=models.TextField(blank=True, null=True),
        ),
    ]