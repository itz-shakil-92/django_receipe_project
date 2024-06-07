from django.db import migrations,models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()  #automatic fill s.n primary key
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    # image=models.ImageField()
    # file=models.FileField()
    

class Product(models.Model): 
    password=models.TextField()
     
class Car(models.Model):
    car_name=models.TextField(max_length=50)
    speed=models.IntegerField(default=50)      
    
    def __str__(self) -> str:
        return self.car_name