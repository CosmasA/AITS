# Generated by Django 5.1.7 on 2025-04-06 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_issue_lecturer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='assigned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='IssueAssignmentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reassigned_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_history', to='api.issue')),
                ('new_lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_assignments', to=settings.AUTH_USER_MODEL)),
                ('old_lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='old_assignments', to=settings.AUTH_USER_MODEL)),
                ('reassigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reassignments_made', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
