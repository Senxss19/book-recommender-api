from rest_framework import viewsets
from rest_framework.decorators import api_view


from books.models import Book
from books.serializers import BookSerializer, RatingStatsSerializer, PublisherStatsSerializer

from books.services.analytics import rating_distribution
from books.services.recommendation import recommend_books
from books.services.analytics import publisher_stats

from books.pagination import StandardPagination
from books.utils.response import success

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Books
    """

    queryset = Book.objects.all().order_by("id")

    serializer_class = BookSerializer

    pagination_class = StandardPagination

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()

        paginator = StandardPagination()

        page = paginator.paginate_queryset(queryset, request)

        serializer = BookSerializer(page, many=True)

        return success({
            "count": paginator.page.paginator.count,
            "results": serializer.data
        })

@extend_schema(
    summary="Rating Distribution",
    responses=RatingStatsSerializer(many=True)
)
@api_view(["GET"])
def rating_stats(request):
    """
    Rating distribution statistics
    """

    data = rating_distribution()

    paginator = StandardPagination()

    page = paginator.paginate_queryset(data, request)

    return success({
        "count": len(data),
        "results": page
    })


@extend_schema(
    summary="Book Recommendation",
    description="Recommend books by author or title (minimum 3 characters)",
    parameters=[
        OpenApiParameter(
            name="q",
            description="Author name or book title (at least 3 characters)",
            required=True,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        )
    ],
    responses=BookSerializer(many=True)
)
@api_view(["GET"])
def recommend(request):

    keyword = request.GET.get("q")

    if not keyword or len(keyword) < 3:
        return success([], message="keyword must be at least 3 characters")

    books = recommend_books(keyword)

    paginator = StandardPagination()

    page = paginator.paginate_queryset(books, request)

    serializer = BookSerializer(page, many=True)

    return success({
        "count": books.count(),
        "results": serializer.data
    })


@extend_schema(
    summary="Publisher Statistics",
    responses=PublisherStatsSerializer(many=True)
)
@api_view(["GET"])
def publisher_trend(request):
    """
    Publisher statistics
    """

    data = publisher_stats()

    paginator = StandardPagination()

    page = paginator.paginate_queryset(data, request)

    return success({
        "count": len(data),
        "results": page
    })