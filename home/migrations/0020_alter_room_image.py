# Generated by Django 5.0.4 on 2024-10-06 15:46

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_setting_second_email_alter_setting_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='room_images/'),
        ),
    ]
