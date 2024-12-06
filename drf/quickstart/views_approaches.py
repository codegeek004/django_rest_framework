# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# ##using mixins##
# from rest_framework import mixins
# class SnipperList(mixins.ListModelMixin,
# 				  mixins.CreateModelMixin,
# 				  mixins.GenericAPIView):
# #the listmodelmixin returns the list of dictionaries for serializing the queryset of objects
# #th createmodelmixin is builtin method for handling post requests.
# 	queryset = Quickstart.objects.all()
# 	serializer_class = QuickstartSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)


# class SnipperDetail(mixins.RetrieveModelMixin,
# 					mixins.DestroyModelMixin,
# 					mixins.UpdateModelMixin):
# 	queryset = Quickstart.objects.all()
# 	serializer_class = QuickstartSerializer
# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


############class based view##############
# from rest_framework import status
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework.views import APIView
# class SnippetList(APIView):
# 	#List all snippets or create a new one
# 	def get(self, request, format=None):
# 		snippets = Quickstart.objects.all()
# 		serializer = QuickstartSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = QuickstartSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
# 	def get_object(self, pk):
# 		#Retrieve, update or delete an instance
# 		try:
# 			return Quickstart.objects.get(pk=pk)
# 		except Quickstart.DoesNotExist:
# 			raise Http404

# 	def get(self, request, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = QuickstartSerializer(snippet)
# 		return Response(serializer.data)

# 	def put(self, request, format=None):
# 		snippet = self.get_object(pk)
# 		serializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)









#############API USING FUNCTION BASED VIEWS#############################
# from rest_framework.decorators import api_view
# @api_view(['GET','POST'])
# # @csrf_exempt
# def snippet_list(request, format=None):
# 	#List all snippets or create a new one
# 	if request.method == 'GET':
# 		#this serializes all the data in the database into json format
# 		snippets = Quickstart.objects.all()
# 		serializer = QuickstartSerializer(snippets, many=True)
# 		# return JsonResponse(serializer.data, safe=False)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		#this first take the data from the user in json format
# 		#parses the input into python datatype
# 		#deserialize the data into the database
# 		#saves the instance and serialize again to return the data in json format
		
# 		# data = JSONParser().parse(request)
# 		serializer = QuickstartSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JsonResponse(serializer.data, status=201)
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		# return JsonResponse(serializer.errors, status=400)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# # @csrf_exempt
# def snippet_detail(request, pk, format=None):
# 	#retrieve, update or delete a code snippet

# 	try:
# 		snippet = Quickstart.objects.get(pk=pk)
# 	except Quickstart.DoesNotExist:
# 		# return HttpResponse(status=404)
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = QuickstartSerializer(snippet)
# 		# return JsonResponse(serializer.data)
# 		return Response(serializer.data)
	
# 	elif request.method == 'PUT':
# 		#put method is used when you want to save or replace everything in a resource.
# 		#it will update all existing fields of the database or create a new one if not existings
# 		# data = JSONParser().parse(request)
# 		serializer = QuickstartSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JsonResponse(serializer.data)
# 			return Response(serializer.data)
# 		# return JsonResponse(serializer.errors, status=400)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
# 	elif request.method == 'DELETE':
# 		#delete the resource from the server
# 		snippet.delete()
# 		# return HttpResponse(status=204)
# 		return Response(status=status.HTTP_204_NO_CONTENT)








# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Quickstart.objects.all()
# 	serializer_class = QuickstartSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Quickstart.objects.all()
# 	serializer_class = QuickstartSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# #creating endpoint for highlighted snippets
# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Quickstart.objects.all()
# 	renderer_class = [renderers.StaticHTMLRenderer]

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)






#Replaced this 2 classes with single viewset
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer






