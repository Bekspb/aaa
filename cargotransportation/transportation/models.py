from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Order(models.Model):
    departure_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    cargo_type = models.CharField(max_length=255)
    weight = models.FloatField()
    volume = models.FloatField()
    delivery_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Добавлено поле price
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'Order {self.id}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received')
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(choices=(('customer', 'Customer'), ('carrier', 'Carrier')), max_length=10, default='customer')

    def __str__(self):
        return f'Review {self.id}'
