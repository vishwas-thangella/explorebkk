# Generated by Django 5.1 on 2024-08-25 10:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_packagemodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemodel',
            name='id',
            field=models.CharField(default=uuid.UUID('2ee6c91d-3ce0-49e3-9c31-9df8b74274bc'), max_length=1000, primary_key=True, serialize=False),
        ),
    ]
