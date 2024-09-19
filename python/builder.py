"""
Ejemplo: Construcción de una Orden de Comida
Supongamos que tenemos diferentes tipos de órdenes de comida, y cada una puede incluir una bebida, un platillo principal y un postre. El Builder nos permite construir diferentes combinaciones de órdenes, paso a paso.
"""

from abc import ABC, abstractmethod


# Producto final: Orden de Comida
class Meal:
    def __init__(self):
        self.items = []
        self.cost = 0

    def add_item(self, item):
        self.items.append(item)
        self.cost += item.price
    def show_order(self):
        print("Orden de comida:")
        for item in self.items:
            print(f"Item: {item.name}, Packing: {item.packing.pack()}, Price: {item.price}")
        print(f"Total Cost: {self.cost}")

