from rest_framework import serializers
from .models import Collection, Flashcard


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['collection_name']


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['collection', 'question', 'answer', 'id']