from django.urls import path
from . import views


urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/flashcard/', views.FlashcardList.as_view()),
    path('collections/<int:pk>', views.CollectionDetail.as_view()),
]