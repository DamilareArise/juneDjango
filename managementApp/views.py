from django.shortcuts import render, redirect

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


def dashboard(request):
    name ="Arise Damilare"
    return render(request, template_name='dashboard.html', context={"name": name})


def allProducts(request):
    return render(request, template_name='products.html', context={'products': db})

def viewProduct(request, id):
    for product in db:
        if product['id'] == id:
            return render(request, template_name='single_product.html', context={'product': product})
        
    return redirect('products')