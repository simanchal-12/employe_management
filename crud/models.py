from django.db import models

# Create your models here.
class Employe(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    desig=models.CharField(max_length=25, blank=False, null=False)
    age=models.IntegerField()
    number=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    address=models.CharField(max_length=25,blank=False,null=False)

    
    def __str__(self) :
        return self.name