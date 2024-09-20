from abc import ABC, abstractmethod


# Step1: Define strategy interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


# Step2: Implement Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."


class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte."


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino."


# step3: Implement the factory (CoffeeMachine)
class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown coffee type!"


# Step4: Use the Factory to Create Products
if __name__ == "__main__":
    machine = CoffeeMachine()

    coffee = machine.make_coffee("Espresso")
    print(coffee)

    coffee = machine.make_coffee("Latte")
    print(coffee)

    coffee = machine.make_coffee("Cappuccino")
    print(coffee) 