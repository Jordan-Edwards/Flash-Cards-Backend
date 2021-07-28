from django.shortcuts import render
from models import Collection, Flashcard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CollectionSerializer
from .serializers import FlashcardSerializer


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


class FlashcardList(APIView):
    def get(self, request):
        pass
