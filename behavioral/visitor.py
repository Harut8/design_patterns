from __future__ import annotations
from abc import ABC, abstractmethod
from functools import singledispatchmethod

"""
PROBLEM 


Problem
Imagine that your team develops an app which works with
geographic information structured as one colossal graph.
Each node of the graph may represent a complex entity such as a city,
but also more granular things like industries, sightseeing areas, etc.
The nodes are connected with others if there’s a road between the real
objects that they represent. Under the hood, each node type is represented by
its own class, while each specific node is an object.

"""



"""
FIRST IMPLEMENTATION
"""


class Car:

    # second implementation
    def accept(self, visitor: IVisitor):
        visitor.visit_car(self)


class Plane:

    # second implementation
    def accept(self, visitor: IVisitor):
        visitor.visit_plane(self)


class Train:

    # second implementation
    def accept(self, visitor: IVisitor):
        visitor.visit_train(self)


class Visitor:

    @singledispatchmethod
    def visit(self, obj: Train | Plane | Car):
        ...

    @visit.register
    def _(self, obj: Train):
        print("Train")

    @visit.register
    def _(self, obj: Plane):
        print("Plane")

    @visit.register
    def _(self, obj: Car):
        print("Car")


# TEST
def test_first_implementation():
    car = Car()
    plane = Plane()
    train = Train()

    visitor = Visitor()
    visitor.visit(car)
    visitor.visit(plane)
    visitor.visit(train)


class IVisitor(ABC):
    @abstractmethod
    def visit_car(self, obj: Car):
        ...

    @abstractmethod
    def visit_plane(self, obj: Plane):
        ...

    @abstractmethod
    def visit_train(self, obj: Train):
        ...


class SampleVisitor(IVisitor):

    def visit_car(self, obj: Car):
        print("Car")

    def visit_plane(self, obj: Plane):
        print("Plane")

    def visit_train(self, obj: Train):
        print("Train")


class DiscountVisitor(IVisitor):

    def visit_car(self, obj: Car):
        print("Discount Car")

    def visit_plane(self, obj: Plane):
        print("Discount Plane")

    def visit_train(self, obj: Train):
        print("Discount Train")


def test_second_implementation():
    car = Car()
    plane = Plane()
    train = Train()

    sample_visitor = SampleVisitor()
    car.accept(sample_visitor)
    plane.accept(sample_visitor)
    train.accept(sample_visitor)

    discount_visitor = DiscountVisitor()
    car.accept(discount_visitor)
    plane.accept(discount_visitor)
    train.accept(discount_visitor)
