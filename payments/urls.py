from django.urls import path
from payments import views

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payments'),
    path('create/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('update/<pk>/', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('delete/<pk>/', views.PaymentDeleteView.as_view(), name='payment-delete'),
]
