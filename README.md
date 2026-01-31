# PALESSI - E-Commerce Platform

A full-featured e-commerce web application built with Django 6.0, featuring product browsing, user authentication, shopping cart, checkout system, and order management.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Models](#database-models)
- [URL Routes](#url-routes)
- [Templates](#templates)
- [Static Files](#static-files)
- [Admin Panel](#admin-panel)
- [Security Notes](#security-notes)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🎯 Overview

This is a modern e-commerce platform developed using Django 6.0 that provides a complete online shopping experience. The application allows users to browse products by categories, add items to their cart, proceed through checkout, and receive order confirmations. It includes a robust authentication system and an admin panel for managing products, categories, customers, and orders.

## ✨ Features

### User Features
- **User Authentication**
  - User registration with email validation
  - Login with username or email
  - Password validation (minimum 8 characters)
  - Session-based authentication
  - Secure logout functionality

- **Product Browsing**
  - View all products on the homepage
  - Browse products by category
  - View detailed product pages
  - See related products from the same category
  - Product search and filtering
  - Sale products with discount pricing

- **Shopping Cart**
  - Add products to cart with quantity selection
  - Update product quantities in cart
  - Remove items from cart
  - Session-based cart persistence
  - Real-time cart total calculation
  - Cart accessible across all pages via context processor

- **Checkout & Orders**
  - Complete checkout flow with shipping form
  - Multiple payment method options (Cash on Delivery)
  - Order summary with tax and shipping calculation
  - Auto-generated unique order numbers (PAL-XXXXXXXX)
  - Order confirmation page with order details
  - Order status tracking (Pending → Processing → Shipped → Delivered)

- **Product Management**
  - Product images with media upload
  - Product descriptions
  - Category organization
  - Sale/discount functionality
  - Price display

### Admin Features
- Django admin panel for complete site management
- Manage categories, products, customers, and orders
- Product image uploads
- Order status tracking with inline order items
- Checkout order management with full details
- Customer management
- Enhanced admin with filters, search, and image previews

## 🛠 Technology Stack

### Backend
- **Django 6.0** - Python web framework
- **Python 3.x** - Programming language
- **SQLite** - Database (default, can be changed to PostgreSQL/MySQL)

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling (Bootstrap-based)
- **JavaScript** - Interactive features
- **Bootstrap 5.2.3** - CSS framework
- **AJAX/jQuery** - Asynchronous requests

### Dependencies
```
asgiref==3.11.0
Django==6.0
pillow==12.0.0
sqlparse==0.5.5
tzdata==2025.3
```

## 📁 Project Structure

```
ecom/
├── ecom/                      # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
│
├── store/                     # Store app (products & categories)
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── navbar.html      # Navigation bar
│   │   ├── index.html       # Homepage
│   │   ├── product.html     # Product detail page
│   │   ├── category.html    # Category page
│   │   ├── all_products.html # All products page
│   │   ├── login.html       # Login page
│   │   ├── signup.html      # Registration page
│   │   └── about.html       # About page
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # Store URL patterns
│   ├── admin.py              # Admin configuration
│   ├── context_processors.py # Context processors
│   └── apps.py               # App configuration
│
├── cart/                      # Shopping cart app
│   ├── migrations/           # Database migrations
│   ├── templates/            # Cart templates
│   │   ├── cart_summary.html # Cart page
│   │   ├── checkout.html     # Checkout page
│   │   └── order_confirmation.html # Order confirmation
│   ├── cart.py               # Cart class logic
│   ├── views.py              # Cart views
│   ├── urls.py               # Cart URL patterns
│   ├── context_processors.py # Cart context processor
│   └── apps.py               # App configuration
│
├── static/                    # Static files (development)
│   ├── css/
│   │   └── styles.css        # Main stylesheet (Bootstrap)
│   ├── js/
│   │   └── scripts.js        # JavaScript files
│   └── assets/               # Images and other assets
│
├── staticfiles/              # Collected static files (production)
│   └── admin/                # Django admin static files
│
├── media/                     # User-uploaded files
│   └── uploads/
│       └── products/         # Product images
│
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone or download the project**
   ```bash
   cd c:\Users\user\PALESSI\ecom
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

7. **Collect static files** (for production)
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## ⚙️ Configuration

### Settings Overview (`ecom/settings.py`)

#### Debug Mode
```python
DEBUG = True  # Set to False in production
```

#### Allowed Hosts
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your domain in production
```

#### Installed Apps
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',      # Product and category management
    'cart',       # Shopping cart functionality
]
```

#### Database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
*For production, consider using PostgreSQL or MySQL*

#### Static & Media Files
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Context Processors
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',  # Makes categories available globally
                'cart.context_processors.cart',         # Makes cart available globally
            ],
        },
    },
]
```

## 📖 Usage

### For Users

1. **Browse Products**
   - Visit the homepage to see all products
   - Click on categories in the navigation to filter products
   - Click "View All Products" to see the complete catalog

2. **View Product Details**
   - Click on any product to see its details
   - View product images, description, price, and category
   - See related products from the same category

3. **Register an Account**
   - Click "Sign Up" in the navigation
   - Fill in: First Name, Last Name, Username, Email, Password
   - Password must be at least 8 characters
   - Email must be unique and valid

4. **Login**
   - Click "Login" in the navigation
   - Enter username or email and password
   - Session persists until logout

5. **Shopping Cart**
   - Click "Add to Cart" on product pages
   - Select quantity before adding
   - View cart by clicking the cart icon
   - Update quantities with +/- buttons
   - Remove items with the delete button
   - Cart persists in session

### For Administrators

1. **Access Admin Panel**
   - Navigate to http://127.0.0.1:8000/admin/
   - Login with superuser credentials

2. **Manage Categories**
   - Add/edit/delete product categories
   - Categories appear in navigation automatically

3. **Manage Products**
   - Add new products with images
   - Set product name, price, description
   - Assign to categories
   - Enable sale pricing
   - Upload product images

4. **Manage Orders**
   - View all customer orders
   - Update order status
   - Track customer information

5. **Manage Customers**
   - View registered customers
   - Edit customer information

## 🗄️ Database Models

### Category Model
```python
class Category(models.Model):
    name = models.CharField(max_length=100)
```
- Stores product categories
- Used for product organization and filtering
- Plural name: "Categories"

### Customer Model
```python
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_No = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
```
- Stores customer information (legacy model)
- *Note: Currently using Django's built-in User model for authentication*

### Product Model
```python
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=500, default='', blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0, blank=True)
```
- Core product model
- Supports regular and sale pricing
- Images stored in `media/uploads/products/`
- Linked to categories via foreign key

### Order Model (Legacy)
```python
class Order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
```
- Legacy order model
- Links products to customers
- Stores delivery information

### CheckoutOrder Model
```python
class CheckoutOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_number = models.CharField(max_length=20, unique=True)  # Auto-generated: PAL-XXXXXXXX
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='United States')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=50, default='Cash on Delivery')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- Main checkout order model
- Auto-generates unique order numbers
- Stores complete shipping address
- Tracks order status through fulfillment
- Calculates and stores order totals

### OrderItem Model
```python
class OrderItem(models.Model):
    order = models.ForeignKey(CheckoutOrder, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    product_image = models.CharField(max_length=500, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```
- Individual items in each order
- Stores product snapshot (name, image, price at time of purchase)
- Linked to CheckoutOrder via foreign key

### ShippingAddress Model
```python
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='United States')
```
- Stores saved shipping addresses for users

## 🌐 URL Routes

### Main URLs (`ecom/urls.py`)
```
/                   - Store homepage (includes store.urls)
/admin/            - Django admin panel
/cart/             - Shopping cart (includes cart.urls)
/media/<path>      - Media files (product images)
```

### Store URLs (`store/urls.py`)
```
/                              - Homepage with all products
/about/                        - About page
/login/                        - User login
/logout/                       - User logout
/register/                     - User registration
/product/<int:pk>/            - Product detail page
/category/<str:category_name>/ - Category filtered products
/all-products/                 - All products page
```

### Cart URLs (`cart/urls.py`)
```
/cart/                                    - Cart summary page
/cart/add/                                - Add item to cart (AJAX)
/cart/update/                             - Update cart quantities (AJAX)
/cart/delete/                             - Remove item from cart (AJAX)
/cart/checkout/                           - Checkout page with shipping form
/cart/order-confirmation/<order_number>/  - Order confirmation page
```

## 🎨 Templates

### Base Templates
- **base.html** - Main layout template with header, navbar, and footer
- **navbar.html** - Navigation bar with categories and cart

### Store Templates
- **index.html** - Homepage displaying all products in a grid
- **product.html** - Detailed product view with related products
- **category.html** - Products filtered by category
- **all_products.html** - Complete product catalog
- **login.html** - User login form
- **signup.html** - User registration form
- **about.html** - About page

### Cart Templates
- **cart_summary.html** - Shopping cart with item management
- **checkout.html** - Checkout page with shipping form and order summary
- **order_confirmation.html** - Order success page with details

### Template Features
- Bootstrap 5.2.3 responsive design
- Context processors for global data (categories, cart)
- Django messages framework for user feedback
- Dynamic product display with images
- AJAX-powered cart operations

## 🎨 Static Files

### CSS
- **styles.css** - Main stylesheet based on Bootstrap 5.2.3
- Includes Start Bootstrap "Shop Homepage" template
- Custom styles for e-commerce layout
- Responsive design for mobile devices

### JavaScript
- **scripts.js** - Custom JavaScript functionality
- AJAX handlers for cart operations
- Dynamic UI interactions

### Assets
- Product images stored in `media/uploads/products/`
- Admin static files in `staticfiles/admin/`

## � Checkout Flow

### Process Overview
```
Cart → Checkout → Order Confirmation
  ↓         ↓              ↓
Review   Fill Form    View Order
Items    & Submit     Details
```

### Checkout Page Features
1. **Shipping Information Form**
   - Full name, email, phone
   - Complete address (line 1, line 2, city, state, postal code, country)
   - Auto-fills for logged-in users

2. **Payment Methods**
   - Cash on Delivery (enabled)
   - Credit/Debit Card (coming soon)
   - PayPal (coming soon)

3. **Order Summary**
   - List of all cart items with images
   - Subtotal, Tax (10%), Shipping ($5.00)
   - Grand total calculation

4. **Order Notes**
   - Optional special instructions

### Order Confirmation
- Unique order number (PAL-XXXXXXXX format)
- Complete shipping address display
- Payment method and status
- List of ordered items
- Order totals breakdown
- "What Happens Next" guide
- Continue shopping option

### Order Status Flow
```
Pending → Processing → Shipped → Delivered
                              ↓
                          Cancelled
```

## �🔐 Admin Panel

### Access
- URL: `/admin/`
- Requires superuser credentials
- Create superuser: `python manage.py createsuperuser`

### Registered Models
1. **Categories** - Manage product categories with product count
2. **Products** - Add/edit/delete products with image previews
3. **Customers** - View customer information
4. **Orders (Legacy)** - Legacy order management
5. **Checkout Orders** - Full checkout order management with status tracking
6. **Order Items** - Individual items in orders (inline in Checkout Orders)
7. **Shipping Addresses** - Saved customer addresses

### Admin Features
- Full CRUD operations for all models
- Image upload and preview for products
- Search and filter functionality
- Inline editing for prices and sale status
- Order status management with color-coded badges
- Inline order items view in checkout orders
- Date hierarchy for order filtering
- Bulk actions
- Custom admin branding (PALESSI Administration)

## 🔒 Security Notes

### ⚠️ Important Security Considerations

1. **Secret Key**
   ```python
   SECRET_KEY = 'django-insecure-...'  # CHANGE THIS IN PRODUCTION!
   ```
   - Generate a new secret key for production
   - Keep it confidential and secure

2. **Debug Mode**
   ```python
   DEBUG = True  # SET TO FALSE IN PRODUCTION!
   ```
   - Never run production with DEBUG=True
   - Exposes sensitive information

3. **Allowed Hosts**
   - Add your production domain to ALLOWED_HOSTS
   - Remove localhost in production

4. **Password Security**
   - Uses Django's built-in password hashing
   - Password validators enabled
   - Minimum 8 characters required

5. **CSRF Protection**
   - Enabled by default
   - Required for all POST requests

6. **Session Security**
   - Session-based cart storage
   - Secure session cookies in production

### Production Recommendations
- Use environment variables for sensitive data
- Use HTTPS in production
- Set secure cookie flags
- Use PostgreSQL or MySQL instead of SQLite
- Configure proper static file serving (Nginx, Apache)
- Enable security middleware
- Regular security updates

## 🎯 Cart Functionality

### Cart Class (`cart/cart.py`)

The shopping cart is implemented as a session-based system:

```python
class Cart():
    def __init__(self, request)
    def add(self, product, quantity=1)
    def get_prods(self)
    def delete(self, product)
    def __len__(self)
    def get_total_quantity(self)
```

### Features
- **Session Storage** - Cart persists in user session
- **Add Products** - With quantity selection
- **Update Quantities** - Increase/decrease via AJAX
- **Remove Items** - Delete individual products
- **Cart Count** - Display total items in navigation
- **Price Calculation** - Real-time total updates
- **Sale Price Support** - Automatically uses sale price when available
- **Cart Clear** - Clear all items after checkout

### Context Processor
Cart is available globally in templates via context processor:
```python
def cart(request):
    return {'cart': Cart(request)}
```

## 📝 User Authentication

### Registration Process
1. User fills registration form (first name, last name, username, email, password)
2. Email validation check
3. Password length validation (min 8 chars)
4. Username uniqueness check
5. Email uniqueness check
6. Password confirmation match
7. User created with Django's `create_user()` (auto-hashes password)
8. Redirect to login page

### Login Process
1. Supports login with username OR email
2. Email detection via '@' symbol
3. User lookup by email if provided
4. Django authentication system
5. Session creation on success
6. Redirect to homepage

### Password Security
- Django's PBKDF2 algorithm with SHA256 hash
- Password validators enforced:
  - UserAttributeSimilarityValidator
  - MinimumLengthValidator
  - CommonPasswordValidator
  - NumericPasswordValidator

## 🚀 Future Enhancements

### Planned Features
- [ ] Payment integration (Stripe, PayPal)
- [ ] Order confirmation emails
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Advanced search with filters
- [ ] Product inventory management
- [ ] Multi-image support for products
- [ ] User profile pages with order history
- [ ] Coupon/discount codes
- [ ] Product recommendations
- [ ] Social media sharing
- [ ] Newsletter subscription
- [ ] Live chat support
- [ ] Mobile app (React Native/Flutter)

### Completed Features ✅
- [x] Complete checkout flow
- [x] Order confirmation page
- [x] Unique order number generation
- [x] Order status tracking
- [x] Enhanced admin panel
- [x] Sale price handling in cart

### Technical Improvements
- [ ] RESTful API (Django REST Framework)
- [ ] PostgreSQL migration
- [ ] Redis caching
- [ ] Celery for async tasks
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Comprehensive test suite
- [ ] Performance optimization
- [ ] SEO optimization
- [ ] Analytics integration

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

2. **Database errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Images not displaying**
   - Check MEDIA_URL and MEDIA_ROOT settings
   - Ensure media files are being served in urls.py
   - Verify file permissions in media directory

4. **Cart not persisting**
   - Check session middleware is enabled
   - Clear browser cookies
   - Verify session backend configuration

## 📄 License

This project is open-source and available for educational purposes. Please check with the repository owner for specific licensing terms.

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues, questions, or contributions, please:
- Open an issue in the repository
- Contact the development team
- Check existing documentation

## 🙏 Acknowledgments

- Django Framework
- Bootstrap 5
- Start Bootstrap templates
- Pillow (Python Imaging Library)

---

**Version:** 1.0.0  
**Last Updated:** January 2026  
**Django Version:** 6.0  
**Python Version:** 3.8+

---

### Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access application
# Main site: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

**Note:** This is a development version. For production deployment, ensure all security measures are implemented and DEBUG is set to False.
