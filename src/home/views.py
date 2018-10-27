from django.contrib import messages
from django.shortcuts import render
from album.models import Album
from flims.models import Flims,FlimsImage
from news.models import Newsletters
from news.forms import NewsletterUserSignUpForm

def home(request):
	flims  = Flims.objects.all().order_by("?")[:1]
	photos = Album.objects.all()
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if Newsletters.objects.filter(email=instance.email).exists():
			messages.warning(request,'Your Email Already exists in our database',"alert alert-warning alert-dismissible")
		else:
			instance.save()
			messages.success(request,'Your Email has been  submitted to WahileProduction',
				"alert alert-success alert-dismissible")
	

	context = {
	 'photos' : photos,
	 'flims'  : flims,
	 'form': form,
	}
	return render(request,"index.html",context)


def about(request):
	return render(request,"about.html",{})