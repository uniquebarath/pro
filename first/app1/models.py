from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    name=models.CharField(max_length=55)
    email=models.CharField(max_length=77,default="")
    number=models.CharField(max_length=70,default="")
    place=models.CharField(max_length=50,default="")
    college=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=200,default="")


class form(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=77,default="")
    number=models.CharField(max_length=70,default="")
    place=models.CharField(max_length=50,default="")
    college=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name

