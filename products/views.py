from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
# Create your views here.

def products_home(request):
	object_list = Product.objects.all()
	context = {
		"objects" : object_list
	}
	return render(request,"products.html",context)


def product_details(request, id=None):
	product_object = get_object_or_404(Product, id=id)
	context = {
		"product_object" : product_object
	}
	return render(request,"product_detail.html",context)


def product_form(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request,"Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form
	}
	return render(request,"product_form.html",context)

def product_edit(request, id=None):
	instance = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form
	}

	return render(request,"product_form.html",context)


def product_delete(request,id=None):
	instance = get_object_or_404(Product, id=id)
	instance.delete()
	messages.success(request,"Item deleted")
	context = {
		"product_object" : instance
	}
	return render(request,"product_detail.html",context)