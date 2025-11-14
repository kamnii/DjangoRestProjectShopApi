from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
    

class CategoryValidatorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class ProductValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=11, decimal_places=2)
    category_id = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')


class ReviewValidatorSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.Serializer(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)


    def validate_product_id(self, product_id):
        try:
            Product.objects.get(product_id)
        except Product.DoesNotExist:
            raise ValidationError('Poduct does not exist')
