from django.contrib.auth.models import User
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer, UserSerializer
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from quickstart.permissions import IsOwnerOrReadOnly


#most consise code. Other approaches are in the views_tutorial file.
# @csrf_protect
class SnippetList(generics.ListCreateAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]	

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


#Creating endpoint for the root of our api(entry point or base of the url)
@api_view
def api_root(request, format=None):
	#reverse redirects you to the url dynamically.
	return Response({
		'users':reverse('user-list', request=request, format=format),
		'snippets':reverse('snippet-list', request=request, format=format)
		})


#creating endpoint for highlighted snippets
class SnippetHighlight(generics.GenericAPIView):
	queryset = Quickstart.objects.all()
	renderer_class = [renderers.StaticHTMLRenderer]

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

















