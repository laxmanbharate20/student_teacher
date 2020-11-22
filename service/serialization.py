from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import Subject,Teacher,Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','teacher']
        depth = 2

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','subject']


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']
        depth=2


