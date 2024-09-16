from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('calculo_pago/', views.calculo_pago_view, name='calculo_pago'),
    ]