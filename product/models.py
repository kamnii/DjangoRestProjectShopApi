from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    def get_deffault_category():
        return Category.objects.get_or_create(name='Uncategorized')[0].id

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(Category,
                                on_delete=models.SET_DEFAULT,
                                default=get_deffault_category)
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    text = models.TextField(blank=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text