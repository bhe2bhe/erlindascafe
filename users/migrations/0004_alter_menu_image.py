# Generated by Django 5.0.5 on 2024-05-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_employee_image_alter_quote_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='default-menu.webp', upload_to='menu_pictures'),
        ),
    ]