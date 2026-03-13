from .models import Book


def rating_distribution():

    result = {
        "0-1": 0,
        "1-2": 0,
        "2-3": 0,
        "3-4": 0,
        "4-5": 0
    }

    for book in Book.objects.all():

        r = book.average_rating

        if r < 1:
            result["0-1"] += 1
        elif r < 2:
            result["1-2"] += 1
        elif r < 3:
            result["2-3"] += 1
        elif r < 4:
            result["3-4"] += 1
        else:
            result["4-5"] += 1

    return result


def recommend_books(author=None):

    qs = Book.objects.all()

    if author:
        qs = qs.filter(authors__icontains=author)

    return qs.order_by("-average_rating")[:10]


def publisher_stats():

    stats = {}

    for book in Book.objects.all():

        pub = book.publisher

        if pub not in stats:
            stats[pub] = []

        stats[pub].append(book.average_rating)

    result = {}

    for pub, ratings in stats.items():
        result[pub] = sum(ratings) / len(ratings)

    return result