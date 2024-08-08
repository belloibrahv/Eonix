# Generated by Django 5.1 on 2024-08-08 03:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_assessment_user_career_created_at_career_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='career',
            new_name='career_id',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='topic',
            new_name='topic_id',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='file',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='format',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='type',
        ),
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
