from django.urls import path
from .views import CategoryView, CategoryDetailView, CartView, CartDetailView, CartItemView, CartItemDetailView, \
    CommentDetailView, OrderView, OrderDetailView, ProductView, ProductDetailView, UserRegisterAPIView, CommentView

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="categories-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="categories-detail"),
    path("products/", ProductView.as_view(), name="products-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path("comments/", CommentView.as_view(), name="comments-list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comments-detail"),
    path("carts/", CartView.as_view(), name="carts-list"),
    path("carts/<int:pk>", CartDetailView.as_view(), name="carts-detail"),
    path("carts-item/", CartItemView.as_view(), name="carts-item-detail"),
    path("carts-item/<int:pk>/", CartItemDetailView.as_view(), name="carts-item-detail"),
    path("orders/", OrderView.as_view(), name="orders-list"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="orders-detail"),
    path("register/", UserRegisterAPIView.as_view(), name="registration"),
]
