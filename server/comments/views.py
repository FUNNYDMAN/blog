from rest_framework import viewsets, permissions

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
