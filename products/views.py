from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from rest_framework import viewsets 

from .serializers import ProductSerializer


# view all products
def allproducts(request):

    allproduct = Product.objects.all()
    context = {
        'allproduct': allproduct
        
    }
    # return HttpResponse('<h1>All Products</h1>')
    return render(request, 'allproducts.html', context)


# view API endpoint ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer




