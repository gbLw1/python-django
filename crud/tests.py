from django.test import TestCase
from .models import Product
from .utils import validate_product_data


class ValidateProductDataTests(TestCase):
    def test_create_product_with_empty_name_should_fail(self):
        result = validate_product_data(None, "10.00")
        self.assertEqual(result, "Name is required!")

    def test_create_product_with_empty_price_should_fail(self):
        result = validate_product_data("Product 1", None)
        self.assertEqual(result, "Price is required!")

    def test_create_product_with_invalid_price_should_fail(self):
        result = validate_product_data("Product 1", "invalid")
        self.assertEqual(result, "Invalid price format!")

    def test_create_product_with_negative_price_should_fail(self):
        result = validate_product_data("Product 1", "-10.00")
        self.assertEqual(result, "Price must be a positive number!")

    def test_create_product_with_zero_price_should_fail(self):
        result = validate_product_data("Product 1", "0.00")
        self.assertEqual(result, "Price must be a positive number!")

    def test_create_existing_product_should_fail(self):
        Product.objects.create(name="Product 1", price=10.00)

        result = validate_product_data("Product 1", "10.00")
        self.assertEqual(result, "Product already exists!")

    def test_create_valid_product_should_pass(self):
        result = validate_product_data("Product 2", "15.00")
        self.assertIsNone(result)
