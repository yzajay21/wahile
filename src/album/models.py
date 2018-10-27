from django.db import models
from wahile.utils import unique_slug_generator
from django.db.models.signals import post_save,pre_save
from django.utils.text import slugify
# Create your models here.

def image_upload_to(instance, filename):
	title = instance.title
	#slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(title, instance.id, file_extension)
	return "flims/%s/%s" %(title, new_filename)

class Album(models.Model):
	#flim = models.ForeignKey(Flims,on_delete=models.CASCADE)
	title = models.CharField(max_length =100)
	image = models.ImageField(upload_to=image_upload_to)


	def __str__(self):
		return self.title

#def product_pre_save_receiver(sender,instance,*args,**kwargs):
	#if not instance.slug:
#		instance.slug =  unique_slug_generator(instance)
#pre_save.connect(product_pre_save_receiver,sender=Flims)