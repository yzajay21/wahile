
from django.urls import path
from flims.views import films,FlimsListView,FlimsDetailSlugView

app_name = 'flims'
urlpatterns = [
	#path('',films,),
	path('list/',FlimsListView.as_view(),name='list'),
	path('<slug:slug>/',FlimsDetailSlugView.as_view(),name='detail'),
    
]
