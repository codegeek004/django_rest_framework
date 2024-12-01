from django.contrib.auth.models import User
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer, UserSerializer
from rest_framework import generics, permissions
from django.views.decorators.csrf import csrf_protect


#most consise code. Other approaches are in the views_tutorial file.
# @csrf_protect
class SnippetList(generics.ListCreateAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
# @csrf_protect
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer	
# @csrf_protect
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
# @csrf_protect
class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
