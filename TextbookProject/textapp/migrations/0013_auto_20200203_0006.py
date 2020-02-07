# Generated by Django 3.0 on 2020-02-02 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textapp', '0012_chatmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='receiver',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='sender',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Chatroommodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=30)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='textapp.Textbookmodel')),
            ],
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='target',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='textapp.Chatroommodel'),
            preserve_default=False,
        ),
    ]
