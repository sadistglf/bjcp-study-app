from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^/view_json$',views.json_viewer, name='index'),
	url(r'^/random_cards$',views.random_cards, name='index'),
]