# Generated by Django 5.0.5 on 2024-05-10 17:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
