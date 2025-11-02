from django.urls import path
from .views import EmailAPIView,EmailStatusAPIView,EmailListView,EmailOneView
urlpatterns = [
    path('sync', EmailAPIView.as_view(), name='sync-email'),
    path('status', EmailStatusAPIView.as_view(), name='email-status'),
    path('show', EmailListView.as_view(), name='show-email'),
    path('show/<int:id>', EmailOneView.as_view(), name='show-one-email'),
]