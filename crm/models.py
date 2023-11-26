from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveSmallIntegerField()
    email=models.EmailField()
    contact=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

