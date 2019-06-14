from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import MyUser
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if request.user.is_admin or request.user.is_staff:
        return render(request, 'dashboard.html')
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def display_product(request):
    if request.user.is_admin or request.user.is_staff or request.user.is_confirm:
        display_product = Product.objects.all()
        context = {
            'display_product': display_product,
            'header': 'Product',
        }
        return render(request, 'display_product.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def add_product(request):
    if request.user.is_admin or request.user.is_staff:
        if request.method == "POST":
            prod_form = ProductForm(request.POST)

            if prod_form.is_valid():
                prod_form.save()
            return redirect('inv_man:display_product')

        else:
            prod_form = ProductForm()
        context={
            'prod_form' : prod_form
        }
        return render(request, 'add_product.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def edit_product(request, id):
    if request.user.is_admin or request.user.is_staff:
        product = get_object_or_404(Product, id=id)

        if request.method == "POST":
            prod_form = ProductForm(request.POST, instance=product)
            if prod_form.is_valid():
                prod_form.save()
                return redirect('inv_man:display_product')
        else:
            prod_form = ProductForm(instance=product)
        context={
            'prod_form' : prod_form
        }
        return render(request, 'edit_product.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def display_order(request):
    if request.user.is_admin or request.user.is_staff or request.user.is_confirm:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_order.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def add_order(request):
    if request.user.is_admin or request.user.is_staff or request.user.is_confirm:
        if request.method == "POST":
            order_form = OrderForm(request.POST)

            if order_form.is_valid():
                order_form.save()
            return redirect('inv_man:display_order')

        else:
            order_form = OrderForm()
        context={
            'order_form' : order_form
        }
        return render(request, 'add_order.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def edit_order(request, id):
    if request.user.is_admin or request.user.is_staff or request.user.is_confirm:
        order = get_object_or_404(Order, id=id)

        if request.method == "POST":
            order_form = OrderForm(request.POST, instance=order)
            if order_form.is_valid():
                order_form.save()
                return redirect('inv_man:display_order')
        else:
            order_form = OrderForm(instance=order)
        context={
            'order_form' : order_form
        }
        return render(request, 'edit_order.html', context)
    else:
        display_order = Order.objects.all()
        context = {
            'display_order': display_order,
            'header': 'Order',
        }
        return render(request, 'display_deliv.html', context)

@login_required
def display_delivery(request):

    display_order = Order.objects.all()
    context = {
        'display_order': display_order,
        'header': 'Order',
    }
    return render(request, 'display_deliv.html', context)

@login_required
def del_edit_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order_form = DelEditOrder(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('inv_man:display_delivery')
    else:
        order_form = DelEditOrder(instance=order)
    context={
        'order_form' : order_form
    }
    return render(request, 'edit_order.html', context)



@login_required
def create_myClass(request):
    packed = request.POST.get('packed')== 'on'
    toSave = models.Order(packed=packed)
    toSave.save()


# def livr_edit_order(request, id):
#     order = get_object_or_404(Order, id=id)

#     if request.method == "POST":
#         order_form = OrderForm(request.POST, instance=order)
#         if order_form.is_valid():
#             order_form.save()
#             return redirect('inv_man:display_delivery')
#     else:
#         order_form = OrderForm(instance=order)
#     context={
#         'order_form' : order_form
#     }
#     return render(request, 'edit_order.html', context)
