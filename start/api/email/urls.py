from django.urls import path
from .views import EmailAPIView
urlpatterns = [
    path('sync', EmailAPIView.as_view(), name='sync-email'),
]