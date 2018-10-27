from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from wahile.utils import unique_slug_generator
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
# Create your models here.

class Flims(models.Model):
	title 				= models.CharField(max_length=100)
	slug	    		= models.SlugField(blank=True)
	categories  		=  models.ManyToManyField('Category', blank=True)
	video       		= EmbedVideoField()
	description 		= models.TextField()
	
	actor       		= models.CharField(max_length=50,null=True,blank=True)
	director    		= models.CharField(max_length=50)
	production  	 	= models.CharField(max_length=100)
	client     			= models.CharField(max_length=50,null=True,blank=True)
	assistant_camera 	= models.CharField(max_length=50,null=True,blank=True)
	actress       		= models.CharField(max_length=50,null=True,blank=True)
	
	class Meta:
		ordering = ["title"]
	class Meta:
		verbose_name_plural = "Flims"
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("flims:detail", kwargs={"slug": self.slug})

	def get_image_url(self):
		img = self.flimsimage_set.first()
		if img:
			return img.image.url
		return img #None


def image_upload_to(instance, filename):
	title = instance.flim.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "flims/%s/%s" %(slug, new_filename)

class FlimsImage(models.Model):
	flim = models.ForeignKey(Flims,on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload_to)


	def __str__(self):
		return self.flim.title

def product_pre_save_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug =  unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver,sender=Flims)





class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug": self.slug })


class Comments(models.Model):
	films 	= models.ForeignKey(Flims,on_delete=models.CASCADE,related_name='comments')
	name  	= models.CharField(max_length=20)
	email 	= models.EmailField()
	body  	= models.TextField()
	created = models.DateTimeField(auto_now_add=True,)
	updated = models.DateTimeField(auto_now=True)
	parent  = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
	active 	= models.BooleanField(default=True)


	class Meta:
		ordering = ('created',)


	def __str__(self):
		return 'Comment by {} on {} '.format(self.name,self.post)

	def children(self):
		return Comments.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True
