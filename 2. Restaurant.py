class MenuItem:
    def __init__(self, name: str, price: float, amount: int, type: str = None):
        self.__type = type
        self.name = name
        self.__price = price
        self.__amount = amount

    def total_price(self):
        return self.__price * self.__amount
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price:float):
        self.__price = price

    def get_type(self):
        return self.__type
    
    def set_type(self, type: str):
        self.__type = type
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount: int):
        self.__amount = amount

    def __str__(self):
        return f"{self.name} - $ {self.get_price()}"

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Beverage"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Beverage")

    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, amount: int, appetizer: str, type: str = "Main Course"):
        self.__appetizer = appetizer
        super().__init__(name, price, amount, type = "Main Course")
    
    def get_appetizer(self):
        return self.__appetizer
    
    def set_appetizer(self, appetizer: str):
        self.__appetizer = appetizer

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_appetizer()} - $ {self.get_price()}"

class Hamburguer(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str, type: str = "Hamburguer"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Hamburguer")
    
    def get_size(self):
        return self.__size
    
    def set_size(self, size: str):
        self.__size = size
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Pizza(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str, type: str = "Pizza"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Pizza")
    
    def get_size(self):
        return self.__size
    
    def set_size(self, size: str):
        self.__size = size
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"
    
class Salad(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str, type: str = "Salad"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Salad")
    
    def get_size(self):
        return self.__size
    
    def set_size(self, size: str):
        self.__size = size

    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Pasta(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Pasta"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Pasta")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class VeganFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Vegan Food"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Vegan Food")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - $ {self.get_price()}"

class SeaFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, fish_type: str, type: str = "Sea Food"):
        self.__fish_type = fish_type
        super().__init__(name, price, amount, type = "Sea Food")
    
    def get_fish_type(self):
        return self.__fish_type
    
    def set_fish_type(self, fish_type: str):
        self.__fish_type = fish_type

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_fish_type()} - $ {self.get_price()}"

class AsianFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Asian Food"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Asian Food")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Dessert"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Dessert")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Soup(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Soup"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Soup")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Order:
    def __init__(self, order_number: int, discount: float = 0, items: list[MenuItem] = None, price: float = 0):
        self.order_number = order_number
        self.__items = []
        self.discount = discount
    
    def get_items(self):
        return self.__items

    def add_item(self, item: MenuItem):
        self.__items.append(item)

    def remove_item(self, item: MenuItem):
        if item in self.get_items():
            self.__items.remove(item)
        else:
            print("Item not found in the order.")

    def total_price(self) -> float:
        price = sum(item.get_price() * item.get_amount() for item in self.get_items())
        return price
    
    def calculate_discount(self) -> tuple:
        total = self.total_price()
        discount = 0
        message = "No discount applied"

        # 20% si total supera 80000
        if total > 80000:
            discount = total * 0.20
            message = "20% off total"

        # 30% en bebidas si hay más de 4 postres
        elif self.count_by_type("Dessert") > 4:
            beverage_discount = self.total_by_type("Beverage") * 0.30
            discount = beverage_discount
            message = "30% off beverages"

        # 10% en comida de mar si supera 50000
        elif self.total_by_type("Sea Food") > 50000:
            seafood_discount = self.total_by_type("Sea Food") * 0.10
            discount = seafood_discount
            message = "10% off seafood"
    
        # 10% en bebidas si hay Main Course (tu condición previa)
        elif any(item.get_type() == "Main Course" for item in self.get_items()):
            beverage_discount = self.total_by_type("Beverage") * 0.10
            discount = beverage_discount
            message = "10% discount on beverages (Main Course)"

        # 15% en bebidas si hay Dessert (tu condición previa alternativa)
        elif any(item.get_type() == "Dessert" for item in self.get_items()):
                beverage_discount = self.total_by_type("Beverage") * 0.15
                discount = beverage_discount
                message = "15% discount on beverages (Dessert)"
    
        total -= discount
        return total, f"{message}: -${discount:.2f}" if discount else message

    
    def total_by_type(self, item_type: str) -> float:
        return sum(item.get_price() * item.get_amount() for item in self.get_items()   
        if item.get_type() == item_type)

    def count_by_type(self, item_type: str) -> int:
        return sum(item.get_amount() for item in self.get_items() 
                   if item.get_type() == item_type)
        
    def apply_discount(self):
        return self.calculate_discount()
        
    def __str__(self):
        order_details = f"Order Number: {self.order_number}\n"
        order_details += "Items:\n"
    
        # Listado de items
        for item in self.get_items():
            order_details += f" - {item} x {item.get_amount()} = ${item.total_price():.2f}\n"
    
        # Aplicar descuento según calculate_discount()
        total_with_discount, discount_message = self.calculate_discount()
    
        if "No discount" not in discount_message:
            order_details += f"{discount_message}\n"
            order_details += f"Total Price with Discount: ${total_with_discount:.2f}"
        else:
            order_details += f"Total Price: ${total_with_discount:.2f}"
        
        return order_details

class Payment:
    def __init__(self, order: Order, medio_pago):
        self.__order = order
        self.__medio_pago = medio_pago
    
    def get_order(self):
        return self.__order
    
    def set_order(self, order: Order):
        self.__order = order
    
    def get_medio_pago(self):
        return self.__medio_pago
    
    def set_medio_pago(self, medio_pago):
        self.__medio_pago = medio_pago

    def realizar_pago(self):
        total, message = self.get_order().calculate_discount()
        print(f"Total a pagar: ${total:.2f}")
        self.get_medio_pago().pagar(total)

class MedioPago:
    def __init__(self):
        pass
  
    def pagar(self, monto):
        pass

class Tarjeta(MedioPago):
    def __init__(self, numero, cvv):
        super().__init__()
        self.__numero = numero
        self.__cvv = cvv

    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def get_cvv(self):
        return self.__cvv
    
    def set_cvv(self, cvv):
        self.__cvv = cvv
    
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta {self.get_numero()[-4:]}")

class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
        else:
            print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")


