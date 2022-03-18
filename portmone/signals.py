from django.dispatch import Signal

# providing_args: "orderId", "payedAmount"
result_authorized = Signal()
