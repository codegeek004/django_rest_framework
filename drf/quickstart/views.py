from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quickstart.models import Quickstart


@csrf_exempt
def snippet_list(request):
	#List all snippets or create a new one
	if request.method == 'GET':
		#this serializes all the data in the database into json format
		snippets = Quickstart.objects.all()
		serializer = QuickstartSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		#this first take the data from the user in json format
		#parses the input into python datatype
		#deserialize the data into the database
		#saves the instance and serialize again to return the data in json format
		data = JSONParser().parse(request)
		serializer = QuickstartSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)