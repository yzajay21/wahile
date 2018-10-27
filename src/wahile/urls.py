"""wahile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from home.views import home,about
from flims.views import films,DetailView
from album.views import photo_list
from contact.views import contact
urlpatterns = [
	path('',home,name='home'),
    path('about/',about,name='about'),
	#path('flims/',flims,name='flim'),
	path('films/',include("flims.urls",namespace='films')),
    path('contact/',contact,name='contact'),
    path('banners/',photo_list,name='photo_list'),
    path('newsletter/',include("news.urls",namespace='newsletter')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'WahileProductions'
admin.site.site_title = 'WahileProductions'