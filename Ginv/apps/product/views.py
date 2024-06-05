from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


# view-set tell backend what we are going to get from serialier

# view-set for getting latest product
class LatestProducts(APIView):
   def get(self, request, format=None):
      products = Product.objects.all()[0:4]
      serialier = ProductSerializer(products, many=True)
      return Response(serialier.data)


class ProductDetail(APIView):
   def get_object(self, category_slug, product_slug):
      try:
         return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
      except Product.DoesNotExist:
         raise Http404
      
   
   def get(self, request, category_slug, product_slug, format=None):
      product = self.get_object(category_slug, product_slug)
      serializer = ProductSerializer(product)
      return Response(serializer.data)