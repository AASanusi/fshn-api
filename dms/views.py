from rest_framework import generics, permissions
from fshn_api.permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    """
    List all messages
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a message
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
