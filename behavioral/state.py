"""
Imagine an e-commerce application where the behavior of a shopping
cart varies depending on whether it’s empty, has items,
or is in the process of checkout. Handling the behavior transitions
and business logic for each state within a single class becomes
unwieldy and leads to code that is difficult to understand and maintain.

The State pattern allows us to encapsulate these states in
separate objects and switch between them seamlessly.
"""

from abc import ABC, abstractmethod


class CheckoutState(ABC):

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def review_cart(self):
        pass

    @abstractmethod
    def enter_shipping_info(self, info):
        pass

    @abstractmethod
    def process_payment(self):
        pass


class EmptyCartState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")
        return ItemAddedState()

    def review_cart(self):
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


class ItemAddedState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")

    def review_cart(self):
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(CheckoutState):
    def __init__(self, info):
        self.info = info

    def add_item(self, item):
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info):
        print("Shipping information already entered.")

    def process_payment(self):
        print("Processing payment with the entered shipping info.")


class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info)

    def process_payment(self):
        self.current_state.process_payment()


def test():
    cart = CheckoutContext()
    print(cart.current_state)
    cart.add_item("Product 1")
    print(cart.current_state)
    cart.review_cart()
    print(cart.current_state)
    cart.enter_shipping_info("123 Main St, City")
    print(cart.current_state)
    cart.process_payment()
    print(cart.current_state)


print(test())
