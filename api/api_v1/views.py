from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.api_v1.serializers import (ProductCategorySerializer,
                                    ProductSerializer, UserSerializer)
from products.models import Product, ProductCategory
from users.models import User


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(methods=['GET'], detail=False)
    def categories(self, request):
        categories = ProductCategory.objects.all()
        return Response(ProductCategorySerializer(categories, many=True).data)
    
    @action(methods=['GET'], detail=True)
    def category(self, request, pk):
        products = Product.objects.filter(category=pk)
        return Response(ProductSerializer(products, many=True).data)


class UsersViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
