from rest_framework import viewsets
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(description='Get a list of all categories'),
    retrieve=extend_schema(description='Get details of a specific category'),
    create=extend_schema(description='Create a new category'),
    update=extend_schema(description='Update an existing category'),
    destroy=extend_schema(description='Delete a category')
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema_view(
    list=extend_schema(
        description='Get a list of all blog posts',
        responses={200: PostSerializer(many=True)}
    ),
    retrieve=extend_schema(
        description='Get details of a specific blog post including comments',
        responses={200: PostSerializer}
    ),
    create=extend_schema(
        description='Create a new blog post',
        responses={201: PostSerializer}
    ),
    update=extend_schema(
        description='Update an existing blog post',
        responses={200: PostSerializer}
    ),
    destroy=extend_schema(
        description='Delete a blog post',
        responses={204: None}
    )
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@extend_schema_view(
    list=extend_schema(description='Get a list of all comments'),
    retrieve=extend_schema(description='Get details of a specific comment'),
    create=extend_schema(description='Create a new comment on a post'),
    update=extend_schema(description='Update an existing comment'),
    destroy=extend_schema(description='Delete a comment')
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)