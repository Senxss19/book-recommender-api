from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    BookViewSet,
    rating_stats,
    recommend,
    publisher_trend
)

router = DefaultRouter()

router.register("books", BookViewSet)

urlpatterns = [

    path("", include(router.urls)),

    path("analytics/ratings/", rating_stats),

    path("analytics/recommend/", recommend),

    path("analytics/publishers/", publisher_trend),

]