from django.shortcuts import render

# Create your views here.
from app.models import *
 
def display_topic(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('Topic_name')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all().order_by('Name')
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    Webpage.objects.filter(Topic_name='cricket').delete()
    DOW=Webpage.objects.all()
    d={'Webpage':DOW}
    return render(request,'display_webpage.html',d)