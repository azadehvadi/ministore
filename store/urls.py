from django.urls import path
from . import views
urlpatterns=[
  #  path('',views.product,name='product'),
     path('products/',views.product,name="products"),
     path('',views.home,name="home")
    ]