from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import now



class Product(models.Model):
    title  =  models.CharField(max_length = 200, blank = False)
    category  =  models.CharField(max_length = 200, blank = True)
    size  =  models.CharField(max_length = 200, blank = True)
    code  =  models.CharField(max_length = 100, blank = True)
    price  =  models.CharField(max_length = 100, blank = True)
    quantity  =  models.CharField(max_length = 100, blank = True)
    packed  =  models.CharField(max_length = 100, blank = True)
    seller  =  models.CharField(max_length = 200, blank = True)
    date  =  models.DateTimeField(default = timezone.now)


    def __str__(self):
        return 'title: {0} size: {1} code: {2} quantity: {3} packed: {4}'.format(self.title, self.size, self.code, self.quantity, self.packed)

class Order(models.Model):
    store_name  =  models.CharField(max_length = 200, blank = False)
    order_date =  models.CharField(max_length = 200, blank = False)
    order_number =  models.CharField(max_length = 200, blank = False)
    sku =  models.CharField(max_length = 200, blank = False)
    product =  models.CharField(max_length = 200, blank = False)
    client_name =  models.CharField(max_length = 200, blank = False)
    phone =  models.CharField(max_length = 200, blank = False)
    address =  models.CharField(max_length = 200, blank = False)
    city =  models.CharField(max_length = 200, blank = False)
    price =  models.CharField(max_length = 200, blank = False)
    packed =  models.BooleanField(default = False)
    confirmed =  models.BooleanField(default = False)
    sent =  models.BooleanField(default = False)
    delivered =  models.BooleanField(default = False)

    def __str__(self):

        return 'store_name: {0}   order_date: {1}  order_number: {2}  sku: {3}  product: {4}  client_name: {5}  phone: {6}  address: {7}  city: {8}  price: {9}    packed: {10} confirmed: {11} sent: {12} delivered: {13} '.format(self.store_name   , self.order_date  , self.order_number  , self.sku  , self.product  , self.client_name  , self.phone  , self.address  , self.city  , self.price    , self.packed   , self.confirmed , self.sent   , self.delivered)

