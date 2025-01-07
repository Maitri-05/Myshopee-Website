from django.urls import path
from .views import UserCls
prd = UserCls()
urlpatterns = [
    path('registerLogin-user',prd.registerLogin,name="registerLogin-user"),
    path('user_registration',prd.register_user,name='user_registration'),
    path('user_login',prd.login_user,name='user_login'),
]
