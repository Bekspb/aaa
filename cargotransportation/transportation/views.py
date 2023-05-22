from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Order, Review
from .forms import OrderForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def base(request):
    return render(request, 'transportation/base.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'transportation/registration.html', {'form': form})


@login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user
            form.save()
            return redirect('base')
    else:
        form = OrderForm()
    return render(request, 'transportation/create_order.html', {'form': form})

@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def create_review(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = ReviewForm(request.user.user_type, request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.order = order
            review.reviewer = request.user
            review.save()
            return redirect('track_order', order_id=order_id)
    else:
        form = ReviewForm(request.user.user_type)
    return render(request, 'create_review.html', {'form': form})


@login_required
def login_view(request):
    return render(request, 'transportation/login.html')



def home(request):
    # Логика для обработки запроса главной страницы
    # ...
    return render(request, 'transportation/home.html')
