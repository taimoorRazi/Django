from django.urls import path
from .views import calculate_total_cost

urlpatterns = [
    path('calculate_total_cost/<int:customer_id>/<int:usage>/',
         calculate_total_cost, name='calculate_total_cost'),
]
