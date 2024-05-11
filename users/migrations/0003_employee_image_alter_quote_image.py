# Generated by Django 5.0.5 on 2024-05-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_menu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='waiter.png', upload_to='employee_pictures'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.ImageField(default='erlinda-crew.jpg', upload_to='quote_pictures'),
        ),
    ]