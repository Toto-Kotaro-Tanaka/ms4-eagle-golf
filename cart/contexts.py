from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if not product.is_discount:
                total += item_data * product.price
                product_count += item_data
            else:
                total += item_data * product.discount_price
                product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            if product.has_sizes:
                for size, quantity in item_data['items_by_size'].items():
                    if not product.is_discount:
                        total += quantity * product.price
                        product_count += quantity
                    else:
                        total += quantity * product.discount_price
                        product_count += quantity 
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })
            elif product.is_club:
                for club, quantity in item_data['items_by_club'].items():
                    if not product.is_discount:
                        total += quantity * product.price
                        product_count += quantity
                    else:
                        total += quantity * product.discount_price
                        product_count += quantity 
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'club': club,
                    })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if total < settings.FREE_GOLF_BALLS_THRESHOLD:
        free_golf_balls_delta = settings.FREE_GOLF_BALLS_THRESHOLD - total
    else:
        free_golf_balls_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_golf_balls_delta': free_golf_balls_delta,
        'free_golf_balls_threshold': settings.FREE_GOLF_BALLS_THRESHOLD,
        'grand_total': grand_total,
    }

    return context