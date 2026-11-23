
from django.db import models


class Sweet(models.Model):

    CATEGORY_CHOICES = [
        ('Traditional', 'Traditional Sweets'),
        ('Milk Sweets', 'Milk Sweets'),
        ('Dry Fruits', 'Dry Fruit Sweets'),
        ('Festival', 'Festival Specials'),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price_per_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    image = models.URLField(max_length=1000)

    stock = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Cake(models.Model):

    CATEGORY_CHOICES = [
        ('Birthday', 'Birthday Cakes'),
        ('Chocolate', 'Chocolate Cakes'),
        ('Wedding', 'Wedding Cakes'),
        ('Special', 'Special Cakes'),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price_per_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    image = models.URLField(max_length=1000)

    stock = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Namkeen(models.Model):

    CATEGORY_CHOICES = [
        ('Mixtures', 'Mixtures'),
        ('Sev', 'Sev and Bhujia'),
        ('Chips', 'Chips and Crisps'),
        ('Traditional', 'Traditional Namkeens'),
        ('Festival', 'Festival Specials'),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price_per_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    image = models.URLField(max_length=1000)

    stock = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
