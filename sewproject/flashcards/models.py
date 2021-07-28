from django.db import models


class Collection(models.Model):
    collection_name = models.CharField(max_length=50)


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
