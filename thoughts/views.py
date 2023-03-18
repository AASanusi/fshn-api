from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Thought
from .serializers import ThoughtSerializer


class ThoughtList(APIView):
    serializer_class = ThoughtSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        thoughts = Thought.objects.all()
        serializer = ThoughtSerializer(
            thoughts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def thought(self, request):
        serializer = ThoughtSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
