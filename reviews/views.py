from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Movie, Genre, Review, Like
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    ReviewSerializer,
    LikeSerializer,
)


# ----------------------
# Custom Permissions
# ----------------------


class IsAdminOrReadOnly(permissions.BasePermission):
    """Only admins can create/update/delete movies"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsReviewOwnerOrReadOnly(permissions.BasePermission):
    """Only review owner can edit/delete"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# ----------------------
# ViewSets
# ----------------------


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view genres


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=["get"])
    def reviews(self, request, pk=None):
        """Custom endpoint: /api/movies/<id>/reviews/"""
        movie = self.get_object()
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsReviewOwnerOrReadOnly,
    ]

    def get_queryset(self):
        """Optionally filter reviews by movie if 'movie_id' is in the URL"""
        movie_id = self.kwargs.get("movie_pk")  # nested route
        if movie_id:
            return self.queryset.filter(movie_id=movie_id)
        return self.queryset


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ----------------------
# Authentication
# ----------------------


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        Token.objects.create(user=user)  # auto-generate token
        return user


class RegisterView(generics.CreateAPIView):
    """POST /api/auth/register/"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
