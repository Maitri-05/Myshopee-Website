from django.urls import path
from .views import PortalClass
prd = PortalClass()
urlpatterns = [
    path('register-portal',prd.portal_register,name="register-portal"), 
    path('client_registration',prd.client_register,name="client_registration"),
    path('login-portal',prd.portal_login,name="login-login"), 
    path('client_login',prd.client_login,name="client_login"),
    path('client_logout',prd.client_logout,name="client_logout"),
    path('client-product',prd.client_product,name="client-product"),
    path('add_product',prd.add_product,name="add_product"),
    path('show_products',prd.show_products,name="show_products"),
    path('edit-product',prd.edit_product,name="edit-product"),
    path('update_product',prd.update_product,name='update_product'),
    path('delete_product/<int:product_id>',prd.delete_product,name="delete_product"),
]
