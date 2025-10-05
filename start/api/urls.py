from django.urls import path, include

urlpatterns = [
    path('email/', include('api.email.urls'))
]
