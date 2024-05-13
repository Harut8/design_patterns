from abc import ABC, abstractmethod

"""
The Composite Design Pattern is a structural approach that organizes objects into tree-like
structures, uniformly treating individual objects and compositions.

When to Use the Builder Pattern:
The Composite Pattern suits tasks needing a tree-like structure where elements
and collections are handled similarly.

Hierarchical Structures: Employ when creating tree-like systems where elements share common handling.
Complex Relationships: Ideal for managing intricate connections among objects,
and simplifying software structures.
Unified Element Management: Use to streamline handling various elements uniformly
within software hierarchies.
"""


class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class LeafFile(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def operation(self) -> str:
        return f'LeafFile: {self.name}'


class CompositeFile(Component):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def operation(self) -> str:
        return f'CompositeFile: {self.name} ({", ".join(c.operation() for c in self.children)})'


def test():
    file1 = LeafFile('file1.txt')
    file2 = LeafFile('file2.txt')
    file3 = LeafFile('file3.txt')
    folder1 = CompositeFile('folder1')
    folder1.add(file1)
    folder1.add(file2)
    folder2 = CompositeFile('folder2')
    folder2.add(file3)
    folder1.add(folder2)
    print(folder1.operation())
