
from django.urls import path

from . import views

urlpatterns = [

    path('', views.allproducts, name='allproducts'),
    # path('<int:product_id>/', views.productdetails, name='productdetails')
]
