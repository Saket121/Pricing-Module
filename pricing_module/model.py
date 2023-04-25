from pyexpat import model


class PricingConfig(model.Model):
    name = model.CharField(max_length=100)
    distance_base_price = model.DecimalField(max_digits=10, decimal_places=2)
    distance_additional_price = model.DecimalField(max_digits=10, decimal_places=2)
    time_multiplier_factor = model.DecimalField(max_digits=10, decimal_places=2)
    enabled = model.BooleanField(default=True)
    created_at = model.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)
