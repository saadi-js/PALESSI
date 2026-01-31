class Cart():
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart=cart

    def add(self, product, quantity=1):
        product_id=str(product.id)
        # Use sale price if product is on sale
        if product.is_sale and product.sale_price:
            price = str(product.sale_price)
        else:
            price = str(product.price)
            
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'name': product.name, 
                'quantity': quantity,
                'price': price,
                'image': product.image.url
            }
        
        self.session.modified = True
    
    def get_prods(self):
        return self.cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values()) 