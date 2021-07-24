from django.shortcuts import render
from .models import Student
from .serializers import StudentSr
from rest_framework import viewsets
# Create your views here.
class Studentmvs(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSr