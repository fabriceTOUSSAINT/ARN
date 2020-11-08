from arn.models import Arn
from arn.serializers import ArnSerializer, UserSerializer
from rest_framework import generics, permissions, viewsets, renderers
from django.contrib.auth.models import User
from arn.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-lists', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetViewSet(viewsets.ModelViewSet):
    """
    this viewset automatically provides `list`, `create`, `retrieve`, 
    `update` and `destroy` actions

    additionally we also provide an extra `highlight` action.
    """
    queryset = Arn.objects.all()
    serializer_class = ArnSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    this viewset qutomatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer