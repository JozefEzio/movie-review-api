from rest_framework import serializers
from .models import Movie, Genre, Review, Like

# Genre serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

# Movie serializer (show genres by name)
class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", read_only=True
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_date", "genres"]

# Review serializer (show movies by title, allow selecting movie)
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())


    class Meta:
        model = Review
        fields = ["id", "user", "movie", "rating", "comment", "created_at"]

# Like serializer
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    review = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all()
    )

    class Meta:
        model = Like
        fields = ["id", "user", "review"]
