from django.contrib import admin
from .model import PricingConfig

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'enabled', 'created_at', 'updated_at')
    list_filter = ('enabled', 'created_at', 'updated_at')
    search_fields = ('name', 'distance_base_price', 'distance_additional_price', 'time_multiplier_factor')
