from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=700)
    price = models.FloatField(blank=True)
    image_url = models.CharField(max_length=2300, blank=True)
    availability = models.BooleanField()
    star = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(Customer, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.address
