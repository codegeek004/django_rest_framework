from django.contrib.auth.models import User
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer, UserSerializer
from rest_framework import generics

#most consise code. Other approaches are in the views_tutorial file.
class SnippetList(generics.ListCreateAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer	

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
