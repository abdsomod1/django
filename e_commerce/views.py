from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from  .models import Product, ProductCategory
from .form import ProductForm

# Create your views here.
def home(request: HttpRequest):
    return  HttpResponse('hello world')
def create_product(request: HttpRequest):
    _context = {}
    form = ProductForm()
    _context['form']=form

    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
        _context['form']=form

    return render(request , 'new-product.html', _context)


def create_product_2(request: HttpRequest):

    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Category = request.POST.get('category')
        product = Product.objects.create(name=name, price=price, category=Category)
        product.save()

        return JsonResponse(
            data=product.to_dict()
        )
        
    return render(request, 'new-product2.html')

def product_detail(request: HttpRequest, pk: int):
    p = Product.objects.get(pk=pk)
    if p is not None:
        return JsonResponse(
            data=p.to_dict()
        )
    return JsonResponse(data={'message':'not found'})





def update_product_detail(request:HttpRequest, pk:int):
    

    
    return render(request, 'new-product2.html')


# def update_product_detail(request: HttpRequest, pk:int):
#     p = Product.objects.get(pk=pk)
#     product = Product
#     _context = {}
#     form = ProductForm()
#     _context['form']=form

#     if request.method == 'POST':
#         form = ProductForm(data=request.POST, instance=s)
#         if form.is_valid():
#             form.save()
#         _context['form']=form
#     s = lambda: None
#     s.name = product.name
#     s.price = product.price
#     s.category = product.category
#     return render(request , 'update-product.html', _context)



def update_product_detail(request: HttpRequest, pk: int):
    # 1. Fetch the product using get_object_or_404 to cleanly handle missing IDs
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        # 2. Pass request.POST and the product instance to update it
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse('saved')  # Change to your actual success URL name
    else:
        # 3. Pre-populate the form with the existing product's data
        form = ProductForm(instance=product)

    # 4. Pass the form and the product to the template context
    context = {
        'form': form,
        'product': product
    }
    
    return render(request, 'update-product.html', context)
