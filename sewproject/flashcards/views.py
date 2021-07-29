from django.shortcuts import render
from .models import Collection, Flashcard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CollectionSerializer
from .serializers import FlashcardSerializer
from django.http import Http404


# Create your views here.
class CollectionList(APIView):
    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  for testing purposes
class CollectionDetail(APIView):

    def get_Collection(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_Collection(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)


class FlashcardList(APIView):

    def get_objects(self):
        try:
            return Flashcard.objects.all()
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flashcard = Flashcard.objects.filter(collection_id=pk)
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):

    def put(self, request, pk, fk):
        flashcard = Flashcard.objects.get(collection_id=fk, id=pk)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)