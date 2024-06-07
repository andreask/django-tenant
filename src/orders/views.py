from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from orders.models import Order


# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
