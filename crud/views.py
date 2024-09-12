from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Product
from .utils import validate_product_data, get_float_price, get_formatted_price

# Create your views here.


def list_products(request):
    match request.method:
        case "GET":
            products = Product.objects.all()

            for product in products:
                product.price = get_formatted_price(product.price)

            return render(
                request,
                "list.html",
                {"products": products, "status": request.GET.get("status")},
            )
        case _:
            return HttpResponse("Method not allowed!", status=405)


def create_product(request):
    match request.method:
        case "GET":
            return render(request, "create.html")
        case "POST":
            name, description, price = (
                request.POST.get("product_name"),
                request.POST.get("product_description"),
                request.POST.get("product_price"),
            )

            if error := validate_product_data(name=name, price=price):
                return render(request, "create.html", {"error": error})

            price = get_float_price(price)

            product = Product(
                name=name,
                description=description,
                price=price,
            )
            product.save()

            return redirect("/list?status=1")
        case _:
            return HttpResponse("Method not allowed!", status=405)
