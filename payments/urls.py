from django.urls import path
from payments import views

app_name = 'payments'
urlpatterns = [
    path('payments/', views.PaymentListView.as_view(), name='payments'),
    path('payments/create/', views.PaymentCreateView.as_view(), name='payments-create'),
    path('payments/update/<pk>/', views.PaymentUpdateView.as_view(), name='payments-update'),
    path('payments/delete/<pk>/', views.PaymentDeleteView.as_view(), name='payments-delete'),
]
