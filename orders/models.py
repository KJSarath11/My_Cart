from django.db import models
from customers.models import Customers
from products.models import Products

#! Order Model
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,"Live"),(DELETE,"Delete"))

    CART_STAGE=1
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=(
        (ORDER_PROCESSED,"ORDER_PROCESSED"),
        (ORDER_DELIVERED,"ORDER_DELIVERED"),
        (ORDER_REJECTED,"ORDER_REJECTED")
        )
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)

    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name="orders")
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)#automatic date 
    updated_at=models.DateField(auto_now_add=True)

#! Ordered Items model
class OrderedItems(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True, related_name="added_carts")
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="added_items")

