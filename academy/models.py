from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    course_image = models.ImageField(upload_to="course/", blank=True, null=True)

    def __str__(self):
        return f"{self.course_name}"

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=50)
    trainer_photo = models.ImageField(upload_to="trainer_photos/", blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
