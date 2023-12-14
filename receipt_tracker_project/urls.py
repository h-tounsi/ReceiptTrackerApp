from django.contrib import admin
from django.urls import path , include  
from django.contrib.auth import views as auth_views
from app_receipt import views as app_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("app_receipt.urls")),  
    path('accounts/signup/', app_views.register_page, name='register'),
    path('accounts/login/', app_views.login_page, name='login'),
    path('accounts/logout/', app_views.logout_page, name='logout'),
]