from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from . import serializers


@api_view(['GET', 'POST'])
def category_list_view(request):
    categories = Category.objects.all()
    data = serializers.CategoryListSerializer(categories, many=True).data

    if request.method == 'GET':
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        category_validation = serializers.CategoryValidatorSerializer(data=request.data)
        category_validation.is_valid(raise_exception=True)

        name = category_validation.validated_data.get('name')
        category = Category.objects.create(
            name=name
        )
        return Response(data=serializers.CategoryDetailSerializer(category).data,
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        data = serializers.CategoryDetailSerializer(category).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        category_validation = serializers.CategoryValidatorSerializer(data=request.data)
        category_validation.is_valid(raise_exception=True)

        category.name = category_validation.validated_data.get('name')
        category.save()
        return Response(data=serializers.CategoryDetailSerializer(category).data,
                        status=status.HTTP_201_CREATED)


    elif request.method == "DELETE":
        category.delete()
        categories = Category.objects.all()
        return Response(data=serializers.CategoryListSerializer(categories, many=True).data,
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_view(request):
    products = Product.objects.all()
    data = serializers.ProductListSerializer(products, many=True).data

    if request.method == "GET":
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        product_validation = serializers.ProductValidatorSerializer(data=request.data)
        product_validation.is_valid(raise_exception=True)

        title = product_validation.validated_data.get('title')
        description = product_validation.validated_data.get('description')
        price = product_validation.validated_data.get('price')
        category_id = product_validation.validated_data.get('category')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )
        return Response(data=serializers.ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        data = serializers.ProductDetailSerializer(product).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        product_validation = serializers.ProductValidatorSerializer(data=request.data)
        product_validation.is_valid(raise_exception=True)

        product.title = product_validation.validated_data.get('title')
        product.description = product_validation.validated_data.get('description')
        product.price = product_validation.validated_data.get('price')
        product.category_id = product_validation.validated_data.get('category_id')
        product.save()
        return Response(data=serializers.ProductDetailSerializer(product).data,
                        status=status.HTTP_201_CREATED)
    
    elif request.method == "DELETE":
        product.delete()
        products = Product.objects.all()
        return Response(data=serializers.ProductListSerializer(products, many=True).data,
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_view(request):
    reviews = Review.objects.all()

    if request.method == "GET":
        data = serializers.ReviewListSerializer(reviews, many=True).data
        return Response(data=data,
                        status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        reveiw_validation = serializers.ReviewValidatorSerializer(data=request.data)
        reveiw_validation.is_valid(raise_exception=True)

        text = reveiw_validation.validated_data.get('text')
        product_id = reveiw_validation.validated_data.get('product_id')
        stars = reveiw_validation.validated_data.get('stars')

        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(data=serializers.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review Not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        data = serializers.ReviewDetailSerializer(review).data
        return Response(data=data,
                        status=status.HTTP_200_OK)

    elif request.method == "PUT":
        reveiw_validation = serializers.ReviewValidatorSerializer(data=request.data)
        reveiw_validation.is_valid(raise_exception=True)

        review.text = reveiw_validation.validated_data.get('text')
        review.product_id = reveiw_validation.validated_data.get('product_id')
        review.stars = reveiw_validation.validated_data.get('stars')
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    
    elif request.method == "DELETE":
        review.delete()
        reviews = Review.objects.all()
        return Response(data=serializers.ReviewListSerializer(reviews, many=True).data,
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_review_list_view(request):
    products = Product.objects.all()
    data = serializers.ProductReviewListSerializer(products, many=True).data

    return Response(data=data)
