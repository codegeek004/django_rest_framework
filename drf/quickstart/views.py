from django.contrib.auth.models import User
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from quickstart.permissions import IsOwnerOrReadOnly
from django.contrib import messages


class SnippetViewSet(viewsets.ModelViewSet):
    # This ViewSet automatically provides `list`, `create`, `retrieve`,
    # `update` and `destroy` actions.

    # Additionally we will also provide an extra `highlight` action.
    if User.is_authenticated:
        queryset = Quickstart.objects.all()
        serializer_class = QuickstartSerializer
        permission_classes = [
            permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

        @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
        def highlight(self, request, *args, **kwargs):
            snippet = self.get_object()
            return Response(snippet.highlighted)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # This viewset automatically provides list and retrieve actions
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Creating endpoint for the root of our api(entry point or base of the url)
@api_view([''])
def api_root(request, format=None):
    # reverse redirects you to the url dynamically.
    return Response({
        'users': reverse('user-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)
    })