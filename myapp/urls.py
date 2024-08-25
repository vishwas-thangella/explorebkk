from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.Home,name="Homepage"),
    path('packages',view=views.Packages,name="Packages"),
    path('packageDetails/<slug:id>',view=views.PackageDetails,name="Package Details")
]