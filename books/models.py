from django.db import models


class Book(models.Model):

    book_id = models.IntegerField(unique=True)

    title = models.CharField(max_length=500)

    authors = models.CharField(max_length=300)

    average_rating = models.FloatField()

    isbn = models.CharField(max_length=20, null=True)

    isbn13 = models.CharField(max_length=20, null=True)

    language_code = models.CharField(max_length=10)

    num_pages = models.IntegerField(null=True)

    ratings_count = models.IntegerField()

    text_reviews_count = models.IntegerField()

    publication_date = models.DateField(null=True)

    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.title