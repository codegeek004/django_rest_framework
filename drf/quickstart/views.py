# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
# @csrf_exempt
def snippet_list(request, format=None):
	#List all snippets or create a new one
	if request.method == 'GET':
		#this serializes all the data in the database into json format
		snippets = Quickstart.objects.all()
		serializer = QuickstartSerializer(snippets, many=True)
		# return JsonResponse(serializer.data, safe=False)
		return Response(serializer.data)

	elif request.method == 'POST':
		#this first take the data from the user in json format
		#parses the input into python datatype
		#deserialize the data into the database
		#saves the instance and serialize again to return the data in json format
		
		# data = JSONParser().parse(request)
		serializer = QuickstartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data, status=201)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		# return JsonResponse(serializer.errors, status=400)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
# @csrf_exempt
def snippet_detail(request, pk, format=None):
	#retrieve, update or delete a code snippet

	try:
		snippet = Quickstart.objects.get(pk=pk)
	except Quickstart.DoesNotExist:
		# return HttpResponse(status=404)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = QuickstartSerializer(snippet)
		# return JsonResponse(serializer.data)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		#put method is used when you want to save or replace everything in a resource.
		#it will update all existing fields of the database or create a new one if not existings
		# data = JSONParser().parse(request)
		serializer = QuickstartSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data)
			return Response(serializer.data)
		# return JsonResponse(serializer.errors, status=400)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		#delete the resource from the server
		snippet.delete()
		# return HttpResponse(status=204)
		return Response(status=status.HTTP_204_NO_CONTENT)










