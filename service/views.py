from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, renderers
from rest_framework.viewsets import ModelViewSet
from .serialization import StudentSerializer,TeacherSerializer,SubjectSerializer
from .models import *
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
"""
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(StudentView, self).list(request, *args, **kwargs)
        print(response.data)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='home.html')
        return response
"""

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer






