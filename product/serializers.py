from rest_framework import serializers
from .models import Category, Product, Review


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']



class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['text', 'product', 'stars']
        

class ProductReviewListSerializer(serializers.ModelSerializer):
    review = ReviewDetailSerializer(many=True, read_only=True)
    average_stars_display = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'category', 'price', 'review', 'average_stars_display']

    def get_average_stars_display(self, product):
        return product.average_stars_display