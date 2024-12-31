from django.shortcuts import render
from apps.main.models import Home,AboutUs,Artist,Reviews
# Create your views here.

#Главная страницы
def index(request):
    home = Home.objects.latest('id')
    aboutus = AboutUs.objects.latest('id')
    artist = Artist.objects.all()
    reviews = Reviews.objects.all()
    return render(request,'index.html',locals())