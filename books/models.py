from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='own_books')
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    condition = models.ForeignKey(Condition, related_name='books',
                                  on_delete=models.SET_NULL, blank=True, null=True)
    retrieval_info = models.TextField()
    image = models.ImageField(upload_to='Images/', blank=True, null=True)
    interested_users = models.ManyToManyField(User, related_name="wanted_books", blank=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name="receiving_books")

    def __str__(self):
        return f"{self.pk} - {self.title}"
