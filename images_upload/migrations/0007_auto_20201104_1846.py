# Generated by Django 3.1.2 on 2020-11-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_upload', '0006_images_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]