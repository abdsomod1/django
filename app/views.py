from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from.form import BookForm

all_products = [
    {"id": 1, "name": "laptop", "price": 150.00},
    {"id": 2, "name": "Smartphone", "price": 950.99},
    {"id": 3, "name": "Tablet", "price": 599.99},
    {"id": 4, "name": "Headphones", "price": 200.0},
    {"id": 5, "name": "Smart Watch", "price": 399.9},
]


# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world</h1>")


# mvt architecture


def product(request):
    return render(request, "product.html", {"products": all_products})

def product_details(request, id):
    print(id)
    for p in all_products:
        print(p, id)
        if p['id'] == id:
            return JsonResponse(
                {
                    'success': True,
                    'message': 'success',
                    'data': p
                }
            )

    return JsonResponse(
        {
            "success": False,
            "message": "Error. Product not found",
        }
    )


@csrf_exempt
def books(request):
    if request.method == "GET":
        return JsonResponse(
            data={
                "success": True,
                "message": "success",
                "data": [
                    {
                        "author": "Chinua Achebe",
                        "available": True,
                        "id": 1,
                        "price": 3500,
                        "title": "Things Fall Apart",
                    },
                    {
                        "author": "Chimamanda Ngozi Adichie",
                        "available": False,
                        "id": 2,
                        "price": 4200,
                        "title": "Purple Hibiscus",
                    },
                ],
            }
        )
    else:
        title = request.POST.get('title')
        return JsonResponse(data={"message": "success", "title": title, 'status': True})

def create_book(request: HttpRequest):
    _context = {}
    form = BookForm(data=request.POST)
    print(request.POST)
    print(form.data)
    if request.method == 'POST':
            if form.is_valid():
                print ("Sucessfully processed form")
                return JsonResponse(
                    data=form.cleaned_data
                )
            _context['form'] = form
            return render (request, 'new_book.html', _context)
    form = BookForm()
    
    _context['form'] = form
    return render (request, 'new_book.html', _context)
