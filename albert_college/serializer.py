from rest_framework import serializers
from .models import Parent, Student, ClassRoom




class ParentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'home_address', 'email']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom', 'parent']
        
class ClassRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'name']