from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path, include
from rest_framework import routers

from cinema import views


app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", views.CinemaHallViewSet)
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("movies", views.MovieViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)
urlpatterns = [
    path("/", include(router.urls)),
] + debug_toolbar_urls()
