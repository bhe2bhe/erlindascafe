# Generated by Django 5.0.5 on 2024-05-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('beverages', 'Beverages'), ('meals', 'Meals'), ('snacks', 'Snacks')], default='meals', max_length=20),
        ),
    ]
