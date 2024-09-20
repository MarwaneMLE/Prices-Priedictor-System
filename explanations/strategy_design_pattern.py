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