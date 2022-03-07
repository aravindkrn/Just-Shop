# from constance import config

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from store.models import Product
from .models import Cart, CartItem
from .utils import get_active_cart, get_active_cart_id


def cart(request, cart_items=None):
    if not cart_items:
        try:
            cart_id = get_active_cart_id(request)
            cart_items = CartItem.objects.filter(cart__cart_id=cart_id)
        except CartItem.DoesNotExist:
            pass
    total, quantity = 0, 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.product_quantity)
        quantity += cart_item.product_quantity
    tax = 0.02 * total
    tax = float(f"{tax:.2f}")
    grand_total = total + tax
    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_active_cart(request)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.product_quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(product=product, cart=cart, product_quantity=1)
    return redirect('cart')


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_active_cart(request)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.product_quantity > 1:
        cart_item.product_quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def delete_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_active_cart(request)
    CartItem.objects.filter(product=product, cart=cart).delete()
    return redirect('cart')
