# Generated by Django 3.0.3 on 2020-08-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0005_auto_20200808_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
