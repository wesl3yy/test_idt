from django.urls import path
from users.users import RegisterApi, LoginAPI
from users.store import UserStoreAPIView, StoreAPIView


urlpatterns = [
    path('register', view=RegisterApi.as_view()),
    path('login', view=LoginAPI.as_view()),
    path('users/store/<int:user_id>', view=UserStoreAPIView.as_view()),
    path('store/product/<int:store_id>', view=StoreAPIView.as_view())
]
