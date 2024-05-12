from abc import abstractmethod, ABC

"""
What is the Abstract Factory Pattern?
The Abstract Factory pattern is a creational design pattern that
provides an interface for creating families of related or dependent
objects without specifying their concrete classes. It is all about encapsulating
the object creation process and ensuring that the created objects are compatible.

Solving a Common Problem
Before we dive into the intricacies of the Abstract Factory pattern,
let’s set the stage. Imagine you are designing an intricate software system,
and you need to create multiple related objects, such as a GUI library
for cross-platform applications, a database abstraction layer, or in our case
a multi-channel notification service (e.g., email, SMS, push notifications).
As the system evolves, you may need to switch between different families of
objects without altering existing code. This is where the Abstract Factory pattern shines.
"""


class SqlDb(ABC):
    """ ABSTRACT PRODUCT """

    @abstractmethod
    def connect(self):
        ...


class AsyncSqlDb(ABC):
    """ ABSTRACT PRODUCT """

    @abstractmethod
    async def connect(self):
        ...


class Postgres(SqlDb):
    """ CONCRETE PRODUCT """

    def connect(self):
        return 'POSTGRES'


class MySql(SqlDb):
    """ CONCRETE PRODUCT """

    def connect(self):
        return 'MYSQL'


class AsyncPostgres(AsyncSqlDb):
    """ CONCRETE PRODUCT """

    async def connect(self):
        return 'async Postgres'


class AsyncMySql(AsyncSqlDb):
    """ CONCRETE PRODUCT """

    async def connect(self):
        return 'async Mysql'


class Factory(ABC):
    """ ABSTRACT FACTORY"""

    @abstractmethod
    def create_postgres(self):
        ...

    @abstractmethod
    def create_mysql(self):
        ...


class FactoryDb(Factory):
    """ CONCRETE FACTORY """

    def create_postgres(self):
        return Postgres()

    def create_mysql(self):
        return MySql()


class FactoryAsyncDb(Factory):
    """ CONCRETE FACTORY """

    def create_postgres(self):
        return AsyncPostgres()

    def create_mysql(self):
        return AsyncMySql()
