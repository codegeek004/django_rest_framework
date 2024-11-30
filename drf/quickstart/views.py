
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer


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


@csrf_exempt
def snippet_detail(request, pk):
	#retrieve, update or delete a code snippet

	try:
		print('snippet wale tr mai gaya')
		snippet = Quickstart.objects.get(pk=pk)
	except Quickstart.DoesNotExist:
		print('does not exist wale except mai gaya')
		return HttpResponse(status=404)

	if request.method == 'GET':
		print('get mai gaya')
		serializer = QuickstartSerializer(snippet)
		return JsonResponse(serializer.data)
	
	elif request.method == 'PUT':
		print('put mai gaya')
		#put method is used when you want to save or replace everything in a resource.
		#it will update all existing fields of the database or create a new one if not existings
		data = JSONParser().parse(request)
		serializer = QuickstartSerializer(snippet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)
	
	elif request.method == 'DELETE':
		print('delete mai gya')
		#delete the resource from the server
		snippet.delete()
		return HttpResponse(status=204)










