from django.shortcuts import render
from myapp.models import PackageModel,CarouselModel,MobileViewImage

# Create your views here.

def Home(request):

    packages = PackageModel.objects.all()
    carousel_items = CarouselModel.objects.all()
    mobile_view_img = MobileViewImage.objects.all()

    data = {
        'top_packages':packages[:4],
        'main_packages':packages[3:7],
        'carousel_items':carousel_items[1:],
        'initial':carousel_items[1],
        'mobile':mobile_view_img[0]
    }

    return render(request,'home.html',data)

def Packages(request):
    data = PackageModel.objects.all()
    context = {
        'data':data
    }
    return render(request,'packages.html',context)

def PackageDetails(request,id):
    data = {
        'data':PackageModel.objects.get(id=id)
    }
    return render(request,'packageDetails.html',data)