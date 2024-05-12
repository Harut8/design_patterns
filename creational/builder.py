from abc import ABC, abstractmethod


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
