# Generated by Django 3.0 on 2020-01-31 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textapp', '0005_auto_20200130_0456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='textbookmodel',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='textbookmodel',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textbookmodel',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
