from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'owner__username',
        'current_location',
        'mood_selector',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ThoughtDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a thought and edit or delete if owned by you.
    """
    serializer_class = ThoughtSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Thought.objects.all()
