"""
Single Instance: Ensures that only one instance of the class is created,
preventing multiple instances from causing conflicts or consuming unnecessary resources.
Global Access: Provides a global point of access to the instance, making it
easy to share data or functionality across different parts of the application.
Resource Management: Helps manage resources that should be shared,
such as database connections, without creating multiple connections and overwhelming the system.
Lazy Initialization: Allows for efficient resource usage by creating the
instance only when it is actually needed.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument
        do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClassViaMeta(metaclass=SingletonMeta):
    pass


def singleton(cls):
    instances = {}  # Dictionary to store instances of different classes

    def get_instance(*args, **kwargs):
        # If class instance doesn't exist in the dictionary
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # Return the existing instance

    # Return the closure function for class instantiation
    return get_instance


@singleton  # Applying the singleton decorator
class SingletonClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print(f"Singleton instance with data: {self.data}")
