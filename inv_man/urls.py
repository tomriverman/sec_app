from django.conf.urls import url
from .views import *

app_name='inv_man'

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^dashboard$', dashboard, name='dashboard'),

    url(r'^product$', display_product, name="display_product"),
    url(r'^(?P<id>\d+)$', edit_product, name='product'),
    url(r'^add_product$', add_product, name="add_product"),
    url(r'^edit_product/(?P<id>\d+)$', edit_product, name="edit_product"),


    url(r'^order$', display_order, name="display_order"),
    url(r'^(?P<id>\d+)$', edit_order, name='order'),
    url(r'^add_order$', add_order, name="add_order"),
    url(r'^edit_order/(?P<id>\d+)$', edit_order, name="edit_order"),


    url(r'^delivery$', display_delivery, name="display_delivery"),
    url(r'^del_edit_order/(?P<id>\d+)$', del_edit_order, name="del_edit_order"),


    # url(r'^livr_edit_order/(?P<id>\d+)$', livr_edit_order, name="livr_edit_order"),
    # url(r'^livr_delivery/(?P<id>\d+)$', livr_delivery, name="livr_delivery"),


    # url(r'^order$', display_order, name="display_order"),
    # url(r'^staff$', display_staff, name="display_staff"),

    # url(r'^add_product$', add_product, name="add_product"),
    # url(r'^add_order$', add_order, name="add_order"),
    # url(r'^add_staff$', add_staff, name="add_staff"),

    # url(r'^product/edit_item/(?P<pk>\d+)$', edit_product, name="edit_product"),
    # url(r'^order/edit_item/(?P<pk>\d+)$', edit_order, name="edit_order"),
    # url(r'^staff/edit_item/(?P<pk>\d+)$', edit_staff, name="edit_staff"),

    # url(r'^product/delete/(?P<pk>\d+)$', delete_product, name="delete_product"),
    # url(r'^order/delete/(?P<pk>\d+)$', delete_order, name="delete_order"),
    # url(r'^staff/delete/(?P<pk>\d+)$', delete_staff, name="delete_staff")

]
