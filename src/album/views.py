from django.shortcuts import render

# Create your views here.
from .models import Album




def photo_list(request):
    queryset =Album.objects.all()
    context = {
            "photos":queryset,      
    }
    return render(request,"album/album.html",context)