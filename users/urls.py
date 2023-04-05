from django.urls import path
from users.users import RegisterApi, LoginAPI
from users.store import StoreAPIView, OrderAPIView


urlpatterns = [
    path('register', view=RegisterApi.as_view()),
    path('login', view=LoginAPI.as_view()),
    path('store/product/<int:store_id>', view=StoreAPIView.as_view()),
    path('user/order/<int:order_id>', view=OrderAPIView.as_view())
]
