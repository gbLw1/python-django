from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

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
                {"products": products},
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

            if error := validate_product_data("POST", name=name, price=price):
                return render(request, "create.html", {"error": error})

            price = get_float_price(price)

            product = Product(
                name=name,
                description=description,
                price=price,
            )
            product.save()

            messages.success(request, "Product created successfully!")

            return redirect("/list")
        case _:
            return HttpResponse("Method not allowed!", status=405)


def update_product(request, product_id):
    match request.method:
        case "GET":
            product = get_object_or_404(Product, id=product_id)
            return render(request, "update.html", {"product": product})
        case "POST":
            product = get_object_or_404(Product, id=product_id)

            name, description, price = (
                request.POST.get("product_name"),
                request.POST.get("product_description"),
                request.POST.get("product_price"),
            )

            if error := validate_product_data("PUT", name=name, price=price):
                messages.error(request, error)
                return render(request, "update.html", {"product": product})

            price = get_float_price(price)

            product.name = name
            product.description = description
            product.price = price

            try:
                product.save()
                messages.success(request, "Product updated successfully!")
            except IntegrityError:
                messages.error(
                    request,
                    "An error occurred while updating the product. Please try again.",
                )

            return redirect("/list")
        case _:
            return HttpResponse("Method not allowed!", status=405)


def delete_product(request, product_id):
    match request.method:
        case "GET":
            try:
                product = Product.objects.get(id=product_id)
                product.delete()
                messages.success(request, "Product deleted successfully!")
            except Product.DoesNotExist:
                messages.error(request, "Delete failed! Product not found.")
            return redirect("/list")
        case _:
            return HttpResponse("Method not allowed!", status=405)
