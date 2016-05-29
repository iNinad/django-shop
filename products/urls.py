from django.conf.urls import url
from django.contrib import admin

from .views import(
		products_home,
		product_details,
		product_form,
		product_edit,
		product_delete
	)

urlpatterns = [
    url(r'^$',products_home),
    url(r'^(?P<id>\d+)/$',product_details, name = 'detail'),
    url(r'^(?P<id>\d+)/edit/$',product_edit, name = 'edit'),
    url(r'^(?P<id>\d+)/delete/$',product_delete, name = 'delete'),
    url(r'^create/$',product_form)

]
 