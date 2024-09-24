import os
import random
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"

def room_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'rooms/room_{slugify(instance.name)}_{instance.created_at}{file_extension}'

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField()
    size = models.CharField(max_length=255, null=True, blank=True)
    image = ProcessedImageField(
        upload_to=room_image_path,
        # processors=[ResizeToFill(1340, 894)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    amenities = models.ManyToManyField(Amenity, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def _name_has_changed(self):
        if self.id:
            original = Room.objects.get(id=self.id)
            return original.name != self.name
        return False

    def _generate_unique_slug(self):
        base_slug = slugify(self.name)
        unique_slug = base_slug
        num = 1
        while Room.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{num}"
            num += 1
        return unique_slug

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rooms"

def room_add_on_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    random_number = random.randint(1000, 9999)
    return f'rooms/add_on/{random_number}_{instance.created_at}{file_extension}'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to=room_add_on_image_path,
        # processors=[ResizeToFill(1340, 894)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.room.name} - {self.created_at}"

    class Meta:
        verbose_name_plural = "Room Images"

class RoomReview(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    location = models.IntegerField(default=5, null=True, blank=True)
    staff = models.IntegerField(default=5, null=True, blank=True)
    cleanliness = models.IntegerField(default=5, null=True, blank=True)
    value_for_money = models.IntegerField(default=5, null=True, blank=True)
    comfort = models.IntegerField(default=5, null=True, blank=True)
    facilities = models.IntegerField(default=5, null=True, blank=True)
    free_wifi = models.IntegerField(default=5, null=True, blank=True)
    status = models.BooleanField(default=1, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.name} for {self.room.name}"

    class Meta:
        verbose_name_plural = "Room Reviews"