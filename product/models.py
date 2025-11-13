from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    @property
    def products_count(self):
        return self.product.filter(category=self.id).count()


class Product(models.Model):

    def get_default_category(self):
        return Category.objects.get_or_create(name='Uncategorized')[0].id

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(Category,
                                on_delete=models.SET_DEFAULT,
                                default=get_default_category,
                                related_name='product')
    
    def __str__(self):
        return self.title
    
    @property
    def average_stars(self):
        reviews = self.review.all()
        if reviews.exists():
            return reviews.aggregate(models.Avg('stars'))['stars__avg']
        return 0
    
    @property
    def average_stars_display(self):
        avg = self.average_stars
        if avg:
            return "* " * round(avg)
        return 'Нет оценок'
    

STARS = (
    (i, "* " * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField(blank=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='review')
    stars = models.IntegerField(choices=STARS, null=True)
    
    def __str__(self):
        return self.text
