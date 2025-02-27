# Generated by Django 5.0.4 on 2024-09-26 10:10

import django.utils.timezone
import home.models
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('rating', models.CharField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], max_length=255)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=home.models.testimony_image_path)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonies',
            },
        ),
    ]
