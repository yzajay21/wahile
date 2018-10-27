from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Flims,FlimsImage,Category
from pagedown.widgets import AdminPagedownWidget
class FlimsAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'title','actor','slug','director']
	prepopulated_fields = {'slug':('title',),}
	#list_editable = ['price', 'active','featured']
	#inlines = [
		#ProductImageInline,
		#VariationInline,
	#]
	ordering = ['title',]
	search_fields = ['title']
	formfield_overrides = {
		models.TextField:{'widget':AdminPagedownWidget},
	}
	class Meta:
		model = Flims

admin.site.register(Flims,FlimsAdmin)

admin.site.register(FlimsImage)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}
	
admin.site.register(Category,CategoryAdmin)


#class CommentAdmin(admin.ModelAdmin):
	#list_display = ('name','email','created','updated',)
	#list_filter	 = ('active','created','updated',)
	#search_fields = ('name','email','body',)



#admin.site.register(Comments,CommentAdmin)