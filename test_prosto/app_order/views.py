from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView
from django.views.generic.list import ListView

from .models import Order
from .forms import OrderForm


class OrderList(ListView):
    """
    Cписок заказов.
    """
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        date_begin = self.request.GET.get('date_begin')
        date_end = self.request.GET.get('date_end')

        if date_begin and date_end:
            date = self.model.objects.filter(date_order__range=(date_begin, date_end)).order_by('-number_order')
        elif date_begin:
            date = self.model.objects.filter(date_order__icontains=date_begin).order_by('-number_order')
        else:
            date = self.model.objects.all().order_by('-number_order')
        return date


class CreateOrder(CreateView):
    """
    Добавить заказ.
    """
    model = Order
    template_name = 'create_page.html'
    form_class = OrderForm


class UpdateOrder(UpdateView):
    """
    Изменить заказ.
    """
    model = Order
    template_name = 'update_page.html'
    form_class = OrderForm


class DetailOrder(DetailView):
    """
    Детали заказа.
    """
    model = Order
    template_name = 'detail_page.html'


class DeleteOrder(DeleteView):
    """
    Удалить заказ.
    """
    model = Order
    template_name = 'delete_page.html'
    success_url = reverse_lazy('order_list_url')
