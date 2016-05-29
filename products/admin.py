from django.contrib import admin

# Register your models here.
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated']
	list_filter = ['updated','timestamp']
	search_fields = ['title','description']
	class Meta:
		model = Product

admin.site.register(Product,ProductModelAdmin)