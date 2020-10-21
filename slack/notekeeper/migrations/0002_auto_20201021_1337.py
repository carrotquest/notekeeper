# Generated by Django 3.1.2 on 2020-10-21 13:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='user_id',
            field=models.CharField(editable=False, max_length=128),
        ),
    ]
