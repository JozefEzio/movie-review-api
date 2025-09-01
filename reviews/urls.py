from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers
from .views import MovieViewSet, ReviewViewSet, LikeViewSet, GenreViewSet, RegisterView

# Create the main router
router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"reviews", ReviewViewSet)
router.register(r"likes", LikeViewSet)
router.register(r"genres", GenreViewSet)

# Create nested router for reviews under movies
movies_router = routers.NestedDefaultRouter(router, r"movies", lookup="movie")
movies_router.register(r"reviews", ReviewViewSet, basename="movie-reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(movies_router.urls)),  # Include nested routes
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/token/", obtain_auth_token, name="token"),  # 👈 token endpoint
    path("api-auth/", include("rest_framework.urls")),  # DRF login/logout
]