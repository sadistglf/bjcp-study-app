# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Subcategory
from django.forms.models import model_to_dict
from django.core import serializers
import json
from random import randint


def index(request):
	subcategory = Subcategory.objects.all()

	random_category = Subcategory.objects.order_by('?')[0]
	dict_category = model_to_dict(random_category)

	query_category = Subcategory.objects.none()
	query_category = query_category | random_category

	serial_category = serializers.serialize( "python", subcategory)
	print type(subcategory)
	print type(query_category)
	query_category = serializers.serialize( "python", [query_category])

	return render(request, 'index.html', context = {'subcategories': subcategory,
	 'random_category': random_category, 'dict_category': dict_category,
	 'serial_category': serial_category,
	 'query_category': query_category
	 })

def json_viewer(request):
	# subcategory = Subcategory.objects.all()

	# random_category = Subcategory.objects.order_by('?')[0]
	# dict_category = model_to_dict(random_category)

	# query_category = Subcategory.objects.none()
	# query_category = query_category | random_category

	# serial_category = serializers.serialize( "python", subcategory)
	# print type(subcategory)
	# print type(query_category)
	# query_category = serializers.serialize( "python", [query_category])
	# Read file 
	f = open('1_9.json')
	json_string = f.read()
	f.close()

	# Convert json string to python object
	data = json.loads(json_string)

	return render(request, 'cards/json_viewer.html', context = {"data": data})

def random_cards(request):

	# Read file 
	f = open('1_9.json')
	json_string = f.read()
	f.close()

	# Convert json string to python object
	data = json.loads(json_string)
	print json_string
	print len(data)
	random_card = randint(0,len(data)-1)
	print data[random_card]

	return render(request, 'cards/navbar_example.html', context = {"data": serializers.serialize("json", data)})