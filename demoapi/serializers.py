from rest_framework import serializers
from SMS.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','age','address']
        