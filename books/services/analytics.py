from django.db.models import Count
from django.db.models.functions import Round
from books.models import Book


def rating_distribution():
    """
    Rating distribution statistics
    """

    qs = (
        Book.objects
        .annotate(rating_round=Round("average_rating"))
        .values("rating_round")
        .annotate(count=Count("id"))
        .order_by("-rating_round")
    )

    result = []

    for item in qs:
        result.append({
            "rating": item["rating_round"],
            "count": item["count"]
        })

    return result


def publisher_stats():
    """
    Publisher statistics
    """

    qs = (
        Book.objects
        .values("publisher")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    result = []

    for item in qs:
        result.append({
            "publisher": item["publisher"],
            "count": item["count"]
        })

    return result