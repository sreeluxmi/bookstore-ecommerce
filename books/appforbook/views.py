import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.context_processors import request
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import Q


# Create your views here.

class BookList(ListView):
    model = Book
    template_name = 'booklist.html'


class BookDetail(LoginRequiredMixin,DetailView):
    model = Book
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class Account(DetailView):
    model = Book
    template_name = 'detail.html'


# def PaymentComplete(request):
#     body = json.loads(request.body)
#     print('BODY:', body)
#     product = Book.objects.get(id=body['productId'])
#     Order.objects.create(product=product)
#     return JsonResponse('Payment Completed', safe=False)


class SearchResult(ListView):
    model = Book
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


def checkOut(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_toatl': 0, 'get_cart_item': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cart_detail.html', context)
