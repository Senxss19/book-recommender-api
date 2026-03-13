from django.db.models import Q
from books.models import Book


def recommend_books(keyword=None):
    """
    Recommend books by author or title.

    Rules:
    - keyword must be at least 3 characters
    - fuzzy search on author or title
    - order by average_rating
    - return top 50
    """

    if not keyword or len(keyword.strip()) < 3:
        return Book.objects.none()

    keyword = keyword.strip()

    qs = (
        Book.objects
        .filter(
            Q(authors__icontains=keyword) |
            Q(title__icontains=keyword)
        )
        .order_by("-average_rating")
    )

    return qs[:50]