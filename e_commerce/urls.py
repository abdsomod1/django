from django.urls import path
from .views import create_product_2, home, create_product, product_detail, update_product_detail
urlpatterns =[
    path('', home),
    path("new-product", create_product, name="create_product"),
    path("new-product2", create_product_2, name="create_product_2"),
    path("product-detail/<pk>", product_detail, name="product_detail"),
    path("update_product_detail/<pk>/", update_product_detail, name="update_product_detail")
]