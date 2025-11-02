from django.urls import path, include,re_path
from .views import frontend_index

from django.views.generic import TemplateView

urlpatterns = [
    path('email/', include('api.email.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
