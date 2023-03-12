from django.urls import path
from dms import views


urlpatterns = [
    path('dms/', views.MessageList.as_view()),
    path('dms/<int:pk>/', views.MessageDetail.as_view()),
]
