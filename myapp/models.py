from django.db import models
import uuid

# Create your models here.

class PackageModel(models.Model):

    choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    # id = models.AutoField(default=uuid.uuid4(),editable=False,unique=True,primary_key=True)
    id = models.CharField(primary_key=True,max_length=1000,default=uuid.uuid4()) 
    name = models.CharField(max_length=50,null=False)
    primary_image = models.ImageField(upload_to='uploads',null=False)
    img2 = models.ImageField(upload_to='uploads',null=False)
    img3 = models.ImageField(upload_to='uploads',null=False)
    img4 = models.ImageField(upload_to='uploads',null=False)
    img5 = models.ImageField(upload_to='uploads',null=False)
    short_description = models.CharField(max_length=300,null=False)
    long_description = models.CharField(max_length=10000,null=False)
    location = models.CharField(max_length=100,null=False)
    price = models.CharField(max_length=8,null=False)
    rating = models.CharField(max_length=1,choices=choices)


class CarouselModel(models.Model):
    image = models.ImageField(upload_to='uploads',null=False)
    title = models.CharField(null=False,max_length=50)
    description = models.CharField(null=False,max_length=100)


class MobileViewImage(models.Model):
    image = models.ImageField(upload_to='uploads',null=False)
    desc = models.CharField(max_length=30)