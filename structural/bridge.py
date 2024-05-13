"""
What is the Bridge Design Pattern?
The Bridge Design Pattern is a structural design pattern that decouples
an abstraction from its implementation, allowing them to vary independently.
It achieves this by providing a bridge between the abstraction and its implementation,
enabling changes to one without affecting the other.

When to Use the Bridge Pattern:
When considering the use of the Bridge Design Pattern:

Divide and organize a monolithic class with multiple variants: If a class handles various
functionalities, such as working with different database servers, and you want to avoid
a monolithic structure.
Extend a class in orthogonal dimensions: When you need to extend a class in multiple
independent dimensions, the Bridge Pattern suggests creating separate class hierarchies
for each dimension.
Switch implementations at runtime: If you need the flexibility to replace implementation
objects within the abstraction dynamically, the Bridge Pattern allows for easy implementation swapping.
"""


# Step 1: Define Abstraction (Abstract class)
class FileStorage(ABC):
    """Abstract class representing the file storage abstraction."""

    @abstractmethod
    def save_file(self, file_name):
        """Abstract method to save a file."""
        pass


# Step 2: Define Implementation (Abstract class)
class StorageImplementation(ABC):
    """Abstract class representing the storage implementation."""

    @abstractmethod
    def save(self, file_name):
        """Abstract method to save a file."""
        pass


# Step 3: Create Concrete Implementations
class LocalStorage(StorageImplementation):
    """Concrete implementation for local file storage."""

    def save(self, file_name):
        """Save a file locally."""
        return f"File '{file_name}' saved locally"


class CloudStorage(StorageImplementation):
    """Concrete implementation for cloud file storage."""

    def save(self, file_name):
        """Save a file to the cloud."""
        return f"File '{file_name}' saved to the cloud"


class NetworkStorage(StorageImplementation):
    """Concrete implementation for network file storage."""

    def save(self, file_name):
        """Save a file to a network location."""
        return f"File '{file_name}' saved to a network location"


# Step 4: Create Refined Abstraction
class AdvancedFileStorage(FileStorage):
    """Refined abstraction for advanced file storage."""

    def __init__(self, storage_impl):
        """Initialize with a specific storage implementation."""
        self._storage_impl = storage_impl

    def save_file(self, file_name):
        """Save a file using the specified storage implementation."""
        return self._storage_impl.save(file_name)


def test():
    local_storage = LocalStorage()
    cloud_storage = CloudStorage()
    network_storage = NetworkStorage()

    # Create refined abstractions and link them with concrete implementations
    advanced_local_storage = AdvancedFileStorage(local_storage)
    advanced_cloud_storage = AdvancedFileStorage(cloud_storage)
    advanced_network_storage = AdvancedFileStorage(network_storage)

    # Use refined abstractions to save files
    print(advanced_local_storage.save_file("example.txt"))
    print(advanced_cloud_storage.save_file("example.txt"))
    print(advanced_network_storage.save_file("example.txt"))
