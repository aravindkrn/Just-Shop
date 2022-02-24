from .models import Cart


def get_active_cart_id(request):
    # cart id mapped to current active session key
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def get_active_cart(request):
    cart_id = get_active_cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id)
    return cart
