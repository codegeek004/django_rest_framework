
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer
from rest_framework import generics

#most consise code. Other approaches are in the views_tutorial file.
class SnippetList(generics.ListCreateAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Quickstart.objects.all()
	serializer_class = QuickstartSerializer	


