from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from . import models
from .models import Flims,Category
# Create your views here.

def films(request):
	flims = Flims.objects.all()
	context = {
		'flims': flims,
	}

	return render(request,'flims/flims_detail.html',context)


class FlimsListView(ListView):
	queryset = Flims.objects.all()
	template_name = "flims/flims_list.html"

	def get_context_data(self,*args,**kwargs):
		context = super(FlimsListView,self).get_context_data(*args,**kwargs)

	
		return context

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Flims.objects.all()

class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "products/category_list1.html"



class FlimsDetailSlugView(DetailView):
	queryset = Flims.objects.all()
	template_name = "flims/flims_detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(FlimsDetailSlugView, self).get_context_data(*args, **kwargs)
        
		instance = self.get_object()
		context['films'] = Flims.objects.all()
		#context['films']   = instance.Category.objects.all()
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
		try:
			instance = Flims.objects.get(slug=slug)
		except Flims.DoesNotExist:
			raise Http404("Not found..")
		except Flims.MultipleObjectsReturned:
			qs = Flims.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404("Uhhmmm ")
		return instance
