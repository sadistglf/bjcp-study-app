from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^/view_json$',views.json_viewer, name='index'),
	url(r'^/random_cards$',views.random_cards, name='index'),
	url(r'^/fill_db$',views.fill_db, name='index'),
	url(r'^/navbar_example$',views.navbar_example, name='index'),
	url(r'^/email_example$',views.email_example, name='index'),
]
