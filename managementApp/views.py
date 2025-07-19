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
    return render(request, template_name='dashboard.html', context={"name": name})


def allProducts(request):
    products = Product.objects.all()
    
    return render(request, template_name='products.html', context={'products': products})

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
        
     
    return render(request, template_name="add_product.html")
     

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