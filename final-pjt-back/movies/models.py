from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    genreid = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="top_movies", blank=True)
    year = models.IntegerField()
    ranking = models.IntegerField()
    isPicked = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")


    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    # score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Top_Movie(models.Model):
#     title = models.CharField(max_length=100)
#     release_date = models.DateField()
#     popularity = models.FloatField()
#     vote_count = models.IntegerField()
#     vote_average = models.FloatField()
#     overview = models.TextField()
#     poster_path = models.CharField(max_length=200)
#     backdrop_path = models.CharField(max_length=200)
#     genres = models.ManyToManyField(Genre, related_name="top_movies", blank=True)
#     year = models.IntegerField()
#     ranking = models.IntegerField()

# class Now_Movie(models.Model):
#     title = models.CharField(max_length=100)
#     release_date = models.DateField()
#     popularity = models.FloatField()
#     vote_count = models.IntegerField()
#     vote_average = models.FloatField()
#     overview = models.TextField()
#     poster_path = models.CharField(max_length=200)
#     backdrop_path = models.CharField(max_length=200)
#     genres = models.ManyToManyField(Genre, related_name="now_movies", blank=True)
#     year = models.IntegerField()
#     ranking = models.IntegerField()
