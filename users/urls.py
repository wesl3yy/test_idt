from django.urls import path
from users.api import RegisterApi, LoginAPI


urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', LoginAPI.as_view())
]
