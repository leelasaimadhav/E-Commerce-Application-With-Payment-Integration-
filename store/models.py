from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = Models.CharField(max_length=100)
    last_name = Models.CharField(max_length=100)

    def _unicode_(self):
        return "%s, %s % (self.last_name, self.fist_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)


class Review(models.Model):
    Book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publish_date = mdoels.DateField(default - timezone.now)
    text = models.TextField