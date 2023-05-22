from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import User, Order, Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'is_company']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'departure_location',
            'destination_location',
            'cargo_type',
            'weight',
            'volume',
            'delivery_date',
            'price'
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'text')

    def __init__(self, user_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_type = user_type

        if self.user_type == 'carrier':
            self.fields['text'].widget = forms.HiddenInput()
        elif self.user_type == 'shipper':
            self.fields['rating'].validators.append(MinValueValidator(1))
            self.fields['rating'].validators.append(MaxValueValidator(5))
            self.fields['rating'].widget = forms.NumberInput(attrs={'min': '1', 'max': '5'})

