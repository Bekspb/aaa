from django.contrib import admin
from django.urls import include, path
from transportation.views import base, create_order, order_list, create_review, home
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from transportation import views

urlpatterns = [
    path('', home),
    path('create_order/', create_order, name='create_order'),
    path('order_list/', order_list, name='order_list'),
    path('create_review/<int:order_id>/', create_review, name='create_review'),
    path('login/', LoginView.as_view(template_name='transportation/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('transportation/', include('transportation.urls')),  # Включение URL-шаблонов приложения transportation
    path('registration/', views.registration, name='registration'),
]
