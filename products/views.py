from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
# Create your views here.

def products_home(request):
	object_list = Product.objects.all()
	context = {
		"objects" : object_list
	}
	return render(request,"products.html",context)


def product_details(request, id=None):
	#print("DEBUG ",id)
	product_object = get_object_or_404(Product, id=id)
	context = {
		"product_object" : product_object
	}
	return render(request,"product_detail.html",context)