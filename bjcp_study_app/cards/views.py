# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Subcategory
from django.forms.models import model_to_dict
from django.core import serializers
import json
from random import randint
from django.core.mail import send_mail

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

	category = Subcategory.objects.all().order_by('?')[0]

	return render(request, 'cards/json_viewer.html', context = {"data": category})

def navbar_example(request):
	category = Subcategory.objects.all().order_by('?')[0]
	return render(request, 'cards/navbar_example.html', context = {"data": category})



def email_example(request):

	send_mail(
	    'Subject here',
	    'Here is the message.',
	    'gustavo.lagos.flores@gmail.com',
	    ['gustavo.lagos.flores@gmail.com'],
	    fail_silently=False,
	)
	return HttpResponse('<h2>Mail enviado!</h2>')


def fill_db(request):
	# Read file 
	f = open('10_15.json')
	json_string = f.read()
	f.close()

	# Convert json string to python object
	data = json.loads(json_string)
	print type(data)
	print type(data[0])
	for j in data:
		# print j
		try:
			code = j['code'].encode('utf-8')
		except:
			code = ''

		try:
			name = j["nombre"].encode('utf-8')
		except:
			name = ''

		try:
			impresion_general = j["Impresión General"].encode('utf-8')
		except:
			impresion_general = ''

		try:
			aroma = j["Aroma"].encode('utf-8')
		except:
			aroma = ''

		try:
			apariencia = j["Apariencia"].encode('utf-8')
		except:
			apariencia = ''

		try:
			sabor = j["Sabor"].encode('utf-8')
		except:
			sabor = ''

		try:
			sensacion = j["Sensación en Boca"].encode('utf-8')
		except:
			sensacion = ''

		try:
			comentarios = j["Comentarios"].encode('utf-8')
		except:
			comentarios = ''

		try:
			historia = j["Historia"].encode('utf-8')
		except:
			historia = ''

		try:
			ingredientes = j["Ingredientes Característicos"].encode('utf-8')
		except:
			ingredientes = ''

		try:
			comparacion = j["Comparación de Estilos"].encode('utf-8')
		except:
			comparacion = ''

		try:
			estadisticas = j["Estadísticas Vitales"].encode('utf-8')
		except:
			estadisticas = ''

		try:
			ejemplos = j["Ejemplos Comerciales"].encode('utf-8')
		except:
			ejemplos = ''
		try:
			etiquetas = j["Etiquetas"].encode('utf-8')
		except:
			etiquetas = ''

		try:
			instrucciones = j["Instrucciones de Entrada"].encode('utf-8')
		except:
			instrucciones = ''

		curr_category = Subcategory(code=code,name=name,impresion_general=impresion_general,
			aroma=aroma,apariencia=apariencia,sabor=sabor,sensacion=sensacion,ingredientes=ingredientes,
			comentarios=comentarios,comparacion=comparacion,historia=historia,estadisticas=estadisticas,
			ejemplos=ejemplos,etiquetas=etiquetas,instrucciones=instrucciones)
		#curr_category.save()
		print len(j.keys())

		# print "CODE: " + code
		# print "NOMBRE: " + name
		# print "IMPRESION: " + impresion_general
		# print "AROMA: " + aroma
		# print "APARIENCIA: " + apariencia
		# print "SABOR: " + sabor
		# print "SENSACION: " + sensacion


	return HttpResponse('<h1> hola! Todo ok :) </h1>')