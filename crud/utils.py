from typing import Optional
from .models import Product


def validate_product_data(name: Optional[str], price: Optional[str]) -> Optional[str]:
    if not name:
        return "Name is required!"

    if not price:
        return "Price is required!"

    converted_price = get_float_price(price)
    if converted_price is None:
        return "Invalid price format!"
    if converted_price <= 0:
        return "Price must be a positive number!"

    if Product.objects.filter(name=name).exists():
        return "Product already exists!"

    return None


def get_float_price(price: str) -> float | None:
    try:
        return float(price)
    except ValueError:
        return None


def get_formatted_price(price: float) -> str:
    # input: 123456.78
    # output: R$ 123.456,78
    return f"R$ {price:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
