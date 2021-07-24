from rest_framework import serializers
from .models import Student
class StudentSr(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']