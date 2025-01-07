from django.urls import path
from .views import ProductClass
prd = ProductClass()
urlpatterns = [
    path('',prd.productPage,name="prd_page"),
    path('product_detail/<int:id>/', prd.product_detail, name="product_detail"),
    path('client-category-page',prd.client_category_page,name="client-category-page"),
    path('add_category',prd.add_category,name="add_category"),
    path('show_category',prd.show_category,name="show_category"),
    path('delete_category/<int:category_id>',prd.delete_category,name="delete_category"),
]
