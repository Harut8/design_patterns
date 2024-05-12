from abc import ABC, abstractmethod

"""
What is the Builder Design Pattern?
The Builder Design Pattern is a creational design pattern that focuses on
constructing complex objects step by step.

It separates the construction of an object from its representation,
allowing the same construction process to create different representations.

When to Use the Builder Pattern:
The Builder Pattern is most useful in the following situations:

Complex Object Construction: When an object needs numerous optional components or configurations,
and a cluttered constructor isn’t practical.
Multiple Representations: When you want to create various object representations using
the same construction process.
"""


class SqlQuery:
    """ Product"""

    def __init__(self, query) -> None:
        self.query = query


class SqlBuilder(ABC):
    """ Abstract Builder """

    @abstractmethod
    def select(self):
        ...

    @abstractmethod
    def from_(self):
        ...

    @abstractmethod
    def where(self):
        ...


class PostgresBuilder(SqlBuilder):
    """ Concrete Builder """

    def select(self):
        print(SqlQuery("select postgres"))
        return self

    def from_(self):
        print(SqlQuery("from"))
        return self

    def where(self):
        print(SqlQuery("where"))
        return self


class MySqlBuilder(SqlBuilder):
    """ Concrete Builder """

    def select(self):
        print(SqlQuery("select mysql"))
        return self

    def from_(self):
        print(SqlQuery("from"))
        return self

    def where(self):
        print(SqlQuery("where"))
        return self


class SqlDirector:
    """ Director """

    def __init__(self, builder) -> None:
        self.builder = builder

    def construct(self):
        return self.builder.select().from_().where()


def test():
    postgres_builder = PostgresBuilder()
    postgres_director = SqlDirector(postgres_builder)
    postgres_director.construct()

    mysql_builder = MySqlBuilder()
    mysql_director = SqlDirector(mysql_builder)
    mysql_director.construct()
