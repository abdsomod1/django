from django.urls import path

from .views import index, product, books, create_book, product_details


urlpatterns = [
    #to configure a route to a view
    path("", index, name='home'),
    path ("product", product, name ='products'),
    path('books', books, name = 'books'),
    path('new_book', create_book, name='create_books'),
    path('products/<int:id>', product_details, name='product_details')
]