# Generated by Django 4.2.5 on 2024-05-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_disaster_type_alter_report_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_legitimate',
            field=models.BooleanField(default=False),
        ),
    ]