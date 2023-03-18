from django.urls import path
from thoughts import views

urlpatterns = [
    path('thoughts/', views.ThoughtList.as_view()),
    path('thoughts/<int:pk>/', views.ThoughtDetail.as_view()),
]
