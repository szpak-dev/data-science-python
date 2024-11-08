from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    id: str
    gtin: str
    name: str
    price: float


class Cart:
    def __init__(self):
        self._total_price = 0
        self._products: List[Product] = []

    def get_products(self) -> List[Product]:
        return self._products

    def add_product(self, product: Product):
        self._products.append(product)
        self._total_price += product.price

    def remove_product(self, id: str):
        products = [product for product in self._products if product.id != id]
        total_price = 0
        for product in products:
            total_price += product.price

        self._products = products
        self._total_price = total_price


product_butter = Product('12', '2352545345356', 'Masło Extra 83%', 6.50)
product_water = Product('15', '43503968945', 'Woda Gazowana', 2.50)


cart = Cart()
cart.add_product(product_butter)
cart.add_product(product_water)

print('Products in cart:')
for product in cart.get_products():
    print(product)


cart.remove_product('12')
cart.remove_product('15')

print('\n\nAfter removal:')
if not cart.get_products():
    print('Cart is empty')
else:
    for product in cart.get_products():
        print(product)
