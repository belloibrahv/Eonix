# Generated by Django 5.1 on 2024-09-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
