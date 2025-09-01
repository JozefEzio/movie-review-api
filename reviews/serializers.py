from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Genre, Review, Like

# Genre serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

# Movie serializer (show genres by name)
class MovieSerializer(serializers.ModelSerializer):
    # For reading: show genre names
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", read_only=True
    )
    # For writing: allow selecting genres by ID
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Genre.objects.all(), 
        source='genres',
        required=False
    )
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_date", "genres", "genre_ids", "created_at", "updated_at", "average_rating", "review_count"]
        read_only_fields = ["genres", "created_at", "updated_at", "average_rating", "review_count"]

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return round(sum(review.rating for review in reviews) / len(reviews), 1)
        return None

    def get_review_count(self, obj):
        return obj.reviews.count()

    def to_representation(self, instance):
        """Custom representation to handle both read and write scenarios"""
        data = super().to_representation(instance)
        # Remove genre_ids from read response since we have genres
        if 'genre_ids' in data:
            del data['genre_ids']
        return data

# Review serializer (show movies by title, allow selecting movie)
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Review
        fields = ["id", "user", "user_id", "movie", "rating", "comment", "created_at", "updated_at"]
        read_only_fields = ["user", "user_id", "created_at", "updated_at"]

    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

# Like serializer
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    review = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all()
    )
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Like
        fields = ["id", "user", "user_id", "review", "created_at"]
        read_only_fields = ["user", "user_id", "created_at"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

# User serializer for registration
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password_confirm"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
