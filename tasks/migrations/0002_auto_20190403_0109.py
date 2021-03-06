# Generated by Django 2.0.5 on 2019-04-02 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
        ('projects', '0002_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='projects.Project'),
        ),
    ]
