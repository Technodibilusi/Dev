from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .serializers import CommentSerializer
from .models import Comment
from permissions.permissions import IsAuthor


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method in ['DELETE', 'PATCH', 'PUT']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()