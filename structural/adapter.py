from abc import ABC, abstractmethod

"""
What is the Adapter Pattern?
The Adapter pattern is a structural design pattern that facilitates the interaction
between two interfaces that are incompatible or cannot work together directly.
It acts as a bridge, allowing objects with different interfaces to collaborate.

The primary goal of the Adapter pattern is to ensure that client code can work
with classes it was not initially designed to support. It achieves this without altering
the source code of either the client or the adaptee (the class with the incompatible interface).
"""


class OldSystem:
    def legacy_operation(self):
        return "Legacy operation"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self):
        return f"Adapter: {self.old_system.legacy_operation()}"
