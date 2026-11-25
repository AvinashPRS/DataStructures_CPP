"""
Runtime polymorphism (port of polymorphism.cpp).

C++ splits polymorphism into two categories:

1. Compile-Time Polymorphism (Static Binding)
   function overloading, operator overloading, templates.

2. Runtime Polymorphism (Dynamic Binding)
   requires: a base class with a virtual function, derived classes that
   override it, and a base pointer/reference to a derived object.

In Python every method is "virtual" (dynamically dispatched). Abstract base
classes (abc.ABC + @abstractmethod) play the role of pure virtual functions.
"""
from abc import ABC, abstractmethod


def fmt(x):
    """print doubles like C++ default cout (45 instead of 45.0)."""
    return f"{x:g}"


# 1. Base Class (Abstract Class)
class PaymentMethod(ABC):
    def __init__(self, amt):
        self.amount = amt

    # Pure virtual function acting as an interface contract
    @abstractmethod
    def processPayment(self):
        ...


# 2. Derived Class: Credit Card
class CreditCardPayment(PaymentMethod):
    def __init__(self, amt, cardNum):
        super().__init__(amt)
        self.cardNumber = cardNum

    def processPayment(self):
        print(f"Processing Credit Card payment of ${fmt(self.amount)} "
              f"using card ending in {self.cardNumber[-4:]}.")


# 3. Derived Class: PayPal
class PayPalPayment(PaymentMethod):
    def __init__(self, amt, userEmail):
        super().__init__(amt)
        self.email = userEmail

    def processPayment(self):
        print(f"Processing PayPal payment of ${fmt(self.amount)} for user {self.email}.")


# 4. Derived Class: Bitcoin
class BitcoinPayment(PaymentMethod):
    def __init__(self, amt, wallet):
        super().__init__(amt)
        self.walletAddress = wallet

    def processPayment(self):
        print(f"Processing Bitcoin payment of ${fmt(self.amount)} to wallet: {self.walletAddress}")


# 5. Client Application / Demonstration - main code harness:
def main():
    # A checkout line managing multiple pending transactions
    # of different concrete types under the uniform PaymentMethod interface.
    checkoutLine = [
        CreditCardPayment(150.75, "1234567890123456"),
        PayPalPayment(45.00, "customer@email.com"),
        BitcoinPayment(1200.00, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"),
    ]

    print("=== Processing Checkout Queue ===")

    # Polymorphism in action: the loop handles all objects uniformly
    for payment in checkoutLine:
        payment.processPayment()


if __name__ == "__main__":
    main()
