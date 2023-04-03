from django.urls import path
from users.users import RegisterApi, LoginAPI
from users.store import UserStoreAPIView


urlpatterns = [
    path('register/', view=RegisterApi.as_view()),
    path('login/', view=LoginAPI.as_view()),
    path('users/<int:user_id>/', view=UserStoreAPIView.as_view())
]
