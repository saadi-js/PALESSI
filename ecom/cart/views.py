from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import product, CheckoutOrder, OrderItem
from django.http import JsonResponse
from django.contrib import messages
from decimal import Decimal

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


def checkout(request):
    cart = Cart(request)
    cart_items = cart.get_prods()
    
    # Redirect to cart if empty
    if not cart_items:
        messages.warning(request, "Your cart is empty. Please add items before checkout.")
        return redirect('cart_summary')
    
    # Calculate totals
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart_items.values())
    tax = subtotal * 0.10
    shipping = 5.00 if subtotal > 0 else 0.00
    total = subtotal + tax + shipping
    
    if request.method == 'POST':
        # Get form data
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address_line1 = request.POST.get('address_line1', '').strip()
        address_line2 = request.POST.get('address_line2', '').strip()
        city = request.POST.get('city', '').strip()
        state = request.POST.get('state', '').strip()
        postal_code = request.POST.get('postal_code', '').strip()
        country = request.POST.get('country', 'United States').strip()
        payment_method = request.POST.get('payment_method', 'cod')
        notes = request.POST.get('notes', '').strip()
        
        # Validation
        if not all([full_name, email, phone, address_line1, city, state, postal_code]):
            messages.error(request, "Please fill in all required fields.")
            return redirect('checkout')
        
        # Create order
        order = CheckoutOrder.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            phone=phone,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            subtotal=Decimal(str(subtotal)),
            tax=Decimal(str(tax)),
            shipping_cost=Decimal(str(shipping)),
            total=Decimal(str(total)),
            payment_method='Cash on Delivery' if payment_method == 'cod' else payment_method,
            notes=notes
        )
        
        # Create order items
        for product_id, item in cart_items.items():
            try:
                prod = product.objects.get(id=int(product_id))
            except:
                prod = None
            
            OrderItem.objects.create(
                order=order,
                product=prod,
                product_name=item['name'],
                product_image=item.get('image', ''),
                quantity=item['quantity'],
                price=Decimal(str(item['price']))
            )
        
        # Clear cart
        cart.clear()
        
        # Redirect to confirmation
        return redirect('order_confirmation', order_number=order.order_number)
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'tax': tax,
        'shipping': shipping,
        'total': total,
    }
    return render(request, 'checkout.html', context)


def order_confirmation(request, order_number):
    try:
        order = CheckoutOrder.objects.get(order_number=order_number)
    except CheckoutOrder.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('index')
    
    return render(request, 'order_confirmation.html', {'order': order})