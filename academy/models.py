from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    course_image = models.ImageField(upload_to="course/", blank=True, null=True)

    def __str__(self):
        return f"{self.course_name}"
