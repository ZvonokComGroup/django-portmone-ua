from django.dispatch import Signal

result_authorized = Signal(providing_args=["orderId", "payedAmount"])
