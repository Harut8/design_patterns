"""
What is the Prototype Design Pattern?
The Prototype design pattern is one of the creational design patterns.
Its primary goal is to create new objects by copying an existing object,
known as the prototype. This pattern is particularly useful when object
creation is complex or resource-intensive. By cloning an existing object,
we can achieve efficient object creation while customizing the copied object’s properties as needed.

How Does the Prototype Pattern Work?
At its core, the Prototype pattern relies on the concept of cloning.
Instead of creating new objects from scratch, we create copies of existing objects,
known as prototypes. These prototypes serve as templates, allowing
us to replicate their structure and attributes. When a new object is needed,
we clone the prototype, saving both time and resources.
"""


class Prototype:
    """ The Prototype interface. """

    def clone(self):
        return copy.deepcopy(self)


class DbConnection(Prototype):
    def __init__(self, name: str, host: str, port: int):
        self.name = name
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        # expensive operation
        self.connection = f'{self.name}://{self.host}:{self.port}'
        return self.connection

    def create_connection_pool(self, pool_size: int):
        return [self.clone() for _ in range(pool_size)]
