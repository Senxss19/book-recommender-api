import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):

    help = "Import books CSV"

    def handle(self, *args, **kwargs):

        df = pd.read_csv(
            "data/books.csv",
            on_bad_lines="skip",
            engine="python"
        )

        for _, row in df.iterrows():

            try:

                pub_date = datetime.strptime(
                    str(row["publication_date"]),
                    "%m/%d/%Y"
                ).date()

            except:
                pub_date = None

            try:
                rating = float(row["average_rating"])
            except:
                rating = None

            try:
                pages = int(row["num_pages"])
            except:
                pages = None

            Book.objects.update_or_create(

                book_id=int(row["bookID"]),

                defaults={

                    "title": str(row["title"]),

                    "authors": str(row["authors"]),

                    "average_rating": rating,

                    "isbn": str(row["isbn"]),

                    "isbn13": str(row["isbn13"]),

                    "language_code": str(row["language_code"]),

                    "num_pages": pages,

                    "ratings_count": int(row["ratings_count"]),

                    "text_reviews_count": int(row["text_reviews_count"]),

                    "publication_date": pub_date,

                    "publisher": str(row["publisher"]),
                },
            )

        self.stdout.write(self.style.SUCCESS("Books imported"))