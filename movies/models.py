from django.db import models
from users.models import User


class RatingMovie(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, null=True)
    rating = models.CharField(
        max_length=20, choices=RatingMovie.choices, default=RatingMovie.G
    )
    synopsis = models.TextField(default=None, null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    users = models.ManyToManyField(
        "users.User",
        through="MovieOrder",
        related_name="movies_order",
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
