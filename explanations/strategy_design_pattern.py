from abc import ABC, abstractmethod


# Step1: Define strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Step2: Implement Concrete Strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Credit Card"
    

 
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using PayPal"


class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paying {amount} using Bitcoin."


# Step2: Implement the Context
class ShoppingCart:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def checkout(self, amount):
        return self.payment_method.pay(amount)


# Step4: Use the strategy in the Context
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(1000))

    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(2000))

    cart = ShoppingCart(CreditCardPayment())
    print(cart.checkout(3000))