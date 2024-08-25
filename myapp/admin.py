from django.contrib import admin
from myapp import models

# Register your models here.

@admin.register(models.PackageModel)
class Package(admin.ModelAdmin):
    list_display = ('name','primary_image','img2','img3','img4','img5','short_description','long_description','location','price','rating')

@admin.register(models.CarouselModel)
class Carousel(admin.ModelAdmin):
    list_display = ('image','title','description')

@admin.register(models.MobileViewImage)
class MobileImage(admin.ModelAdmin):
    list_display = ('image','desc')