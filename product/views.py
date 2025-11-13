from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from . import serializers


@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    data = serializers.CategoryListSerializer(categories, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)



@api_view(['GET'])
def category_detail_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    data = serializers.CategoryDetailSerializer(category).data
    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = serializers.ProductListSerializer(products, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    data = serializers.ProductDetailSerializer(product).data
    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = serializers.ReviewListSerializer(reviews, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    data = serializers.ReviewDetailSerializer(review).data
    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def product_review_list_view(request):
    products = Product.objects.all()
    data = serializers.ProductReviewListSerializer(products, many=True).data

    return Response(data=data)
