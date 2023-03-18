
from rest_framework import generics, permissions
from fshn_api.permissions import IsOwnerOrReadOnly
from .models import Thought
from .serializers import ThoughttSerializer


class ThoughtList(generics.ListCreateAPIView):
    """
    List thoughts or create a thought if logged in
    """
    serializer_class = ThoughtsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Thoughts.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ThoughtDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a thought and edit or delete it if you own it.
    """
    serializer_class = ThoughtsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Thoughts.objects.all()
