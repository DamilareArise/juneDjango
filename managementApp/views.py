from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, StockLog
from .forms import StockLogForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

db = [
    {   
        'id': 1,
        'name': 'Yamaha',
        'quantity': 20,
        'price': 20000
    },
    {   
        'id': 2,
        'name': 'LG',
        'quantity': 10,
        'price': 10000
    }
]

@login_required
def dashboard(request):
    user = get_object_or_404(User, id = request.user.id)
    name = user.first_name +" "+ user.last_name
    products = Product.objects.all()
    stocks = StockLog.objects.all()
    total_products = products.count()
    total_in_stock = stocks.filter(type='in').count()
    total_out_stock = stocks.filter(type='out').count()
    total_stock = stocks.count()
    
    total_price = sum([ product.price * product.quantity for product in products])
    # total products 
    # total in stock
    # total out stock
    # total stock
    
    
    return render(
        request, 
        template_name='dashboard.html', 
        context={
            "name": name, 
            'total_products': total_products,
            'total_in_stock': total_in_stock,
            'total_out_stock': total_out_stock,
            'total_stock': total_stock,
            'total_price': total_price
            })


def allProducts(request):
    products = Product.objects.all()
    
    return render(request, template_name='products.html', context={'products': products})

@login_required
def viewProduct(request, id):
    # for product in db:
    #     if product['id'] == id:
    #         return render(request, template_name='single_product.html', context={'product': product})
    
    # product = Product.objects.get(id = id)
    product = get_object_or_404(Product, id=id)
    return render(request, template_name='single_product.html', context={'product': product})
        
    # return redirect('products')

@login_required
def addProduct(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('product_image')
        
        # print(product_name, quantity, price, image)
        Product.objects.create(
            name = product_name,
            quantity = quantity,
            price = price,
            image = image,
            created_by = request.user
        )
        
        messages.success(request, 'Product added successfully')
        
     
    return render(request, template_name="add_product.html")
     

@login_required
def deleteProduct(request, id):
    product = get_object_or_404(Product, id = id)
    product.delete()
    
    messages.success(request, 'Product deleted successfully')
    return redirect('products')


def editProduct(request, id):
    product = get_object_or_404(Product, id = id)
    
    if request.method == 'POST':
        product.name = request.POST.get('product_name')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        
        if request.FILES.get('product_image'):
            product.image = request.FILES.get('product_image')
            
        product.save()
        messages.success(request, 'Product edited successfully')
        return redirect('view-product', product.id)
    else:
        return render(request, 'edit_product.html', {'product': product})
    

@login_required
def stockLogView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = StockLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.product = product
            log.created_by = request.user
            
            # Increase the product quantity for stock type IN or vice versa
            if log.type == "in":
                product.quantity += int(log.quantity)  
            else:
                if product.quantity < log.quantity:
                    messages.error(request, "Insufficient product quantity")
                    return render(request, template_name="stock_log.html", context={"form": form, "product": product})
                else:
                    product.quantity -= int(log.quantity)
            
            product.save()
            log.save()
            
            messages.success(request, 'Stock updated successfully')
            return redirect('products')
            
        else:
            return render(request, template_name="stock_log.html", context={"form": form, "product": product})
         
    
    else:
        form = StockLogForm()
        return render(request, template_name="stock_log.html", context={"form": form, "product": product})
    
@login_required
def allLogs(request):
    logs = StockLog.objects.all()
    return render(request, 'all_logs.html', {'logs': logs})
    