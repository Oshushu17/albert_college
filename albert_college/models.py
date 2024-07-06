from django.db import models

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class ClassRoom(models.Model):
    name = models.CharField(max_length=12)
    def __str__(self):
        return f'{self.name}'
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    parent =models.ForeignKey(Parent, on_delete=models.CASCADE)
    classroom = models.OneToOneField(ClassRoom, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'



    