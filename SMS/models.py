from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    pic=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name