from django.shortcuts import render,redirect
from . models import  product,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html',{})

def login_user(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if input is an email
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect('login')
        else:
            username = username_or_email
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    
    return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Debug: Print what we're receiving
        print(f"First Name: '{first_name}', Last Name: '{last_name}', Username: '{username}', Email: '{email}'")
        
        # Validation checks
        if not first_name or not last_name or not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('register')
        
        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            return redirect('register')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        # Check password length
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('register')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
        
        # Create user with hashed password
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,  # create_user() automatically hashes the password
            first_name=first_name,
            last_name=last_name
        )
        
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    
    return render(request, 'signup.html',{})

def product_detail(request, pk):
    prod = product.objects.get(id=pk)
    # Get related products from the same category, excluding the current product
    related_products = product.objects.filter(category=prod.category).exclude(id=pk)[:4]
    return render(request, 'product.html', {'product': prod, 'related_products': related_products})
def category(request, category_name):
    # Replace hyphens with spaces for category lookup
    category_name = category_name.replace('-', ' ')
    
    try:
        # Get the category object
        cat = Category.objects.get(name=category_name)
        # Get all products in this category
        products = product.objects.filter(category=cat)
        return render(request, 'category.html', {'products': products, 'category': cat})
    except Category.DoesNotExist:
        messages.error(request, "Category not found.")
        return redirect('index')


def all_products(request):
    products = product.objects.all()
    return render(request, 'all_products.html', {'products': products})

