from django.urls import path
from users.users import RegisterApi, LoginAPI
from users.store import StoreAPIView, OrderAPIView, ListProductAPIView


urlpatterns = [
    path('register', view=RegisterApi.as_view()),
    path('login', view=LoginAPI.as_view()),
    path('store/<int:user_id>', view=StoreAPIView.as_view()),
    path('store/product/<int:store_id>', view=ListProductAPIView.as_view()),
    path('user/order/<int:order_id>', view=OrderAPIView.as_view())
]
