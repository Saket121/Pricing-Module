from django.http import JsonResponse
from .model import PricingConfig

def calculate_price(request):
    distance_traveled = float(request.GET.get('distance_traveled'))
    time_duration = float(request.GET.get('time_duration'))

    pricing_config = PricingConfig.objects.filter(enabled=True).first()

    if not pricing_config:
        return JsonResponse({'error': 'No pricing config found.'}, status=400)

    distance_base_price = pricing_config.distance_base_price
    distance_additional_price = pricing_config.distance_additional_price
    time_multiplier_factor = pricing_config.time_multiplier_factor

    additional_distance = max(distance_traveled - N, 0)
    additional_cost = additional_distance * distance_additional_price

    total_price = (distance_base_price + additional_cost) * time_multiplier_factor

    return JsonResponse({'price': total_price})
