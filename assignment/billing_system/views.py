from django.shortcuts import render
from .models import Customer, PricingTier


def calculate_total_cost(request, customer_id, usage):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return render(request, 'error.html', {'message': 'Customer not found'})
    pricing_tiers = PricingTier.objects.filter(customer=customer)
    total_cost = 0
    for tier in pricing_tiers:
        if tier.min_storage <= usage <= tier.max_storage:
            cost_for_tier = (usage - tier.min_storage + 1) * tier.price
            usage -= (tier.max_storage - tier.min_storage + 1)
            total_cost += cost_for_tier
    return render(request, 'total_cost.html', {'total_cost': total_cost, 'customer_name': customer.name, 'usage': usage})
