from django.urls import path
from .views import EmailAPIView,EmailStatusAPIView,EmailListView
urlpatterns = [
    path('sync', EmailAPIView.as_view(), name='sync-email'),
    path('status', EmailStatusAPIView.as_view(), name='email-status'),
    path('show', EmailListView.as_view(), name='show-email'),
]