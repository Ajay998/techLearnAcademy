from django.forms import ModelForm
from .models import Course, Trainer


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'