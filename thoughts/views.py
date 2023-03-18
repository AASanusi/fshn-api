from rest_framework import generics, permissions
from fshn_api.permissions import IsOwnerOrReadOnly
from .models import Thought
from .serializers import ThoughtSerializer


class ThoughtList(generics.ListCreateAPIView):
    """
    List thoughts or create a thought
    """
    serializer_class = ThoughtSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Thought.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ThoughtDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a thought and edit or delete if owned by you.
    """
    serializer_class = ThoughtSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Thought.objects.all()
