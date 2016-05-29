from django.conf.urls import url
from django.contrib import admin

from .views import(
	products_home,
	product_details
	)

urlpatterns = [
    url(r'^$',products_home),
    url(r'^(?P<id>\d+)/$',product_details, name = 'details')

]
 