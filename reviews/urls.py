from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieViewSet, ReviewViewSet, LikeViewSet, GenreViewSet, RegisterView

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"reviews", ReviewViewSet)
router.register(r"likes", LikeViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/token/", obtain_auth_token, name="token"),  # 👈 token endpoint
    path("api-auth/", include("rest_framework.urls")),  # DRF login/logout
]