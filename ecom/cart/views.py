from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'cart_summary.html', {'cart': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))  # Get quantity from request
        prod = get_object_or_404(product, id=product_id)
        cart.add(product=prod, quantity=quantity)  # Pass quantity to cart
        response = JsonResponse({'Product Name': prod.name, 'quantity': quantity})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') and request.POST.get('product_id'):
        product_id = str(request.POST.get('product_id'))
        action = request.POST.get('action')
        
        if action == 'increase':
            cart.cart[product_id]['quantity'] += 1
        elif action == 'decrease' and cart.cart[product_id]['quantity'] > 1:
            cart.cart[product_id]['quantity'] -= 1
        
        cart.session.modified = True
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('product_id'):
        product_id = str(request.POST.get('product_id'))
        cart.delete(product=product_id)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})