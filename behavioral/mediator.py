"""
Say you have a dialog for creating and editing customer profiles.
It consists of various form controls such as text fields, checkboxes, buttons, etc.
Some of the form elements may interact with others.
For instance, selecting the “I have a dog” checkbox may reveal a hidden
text field for entering the dog’s name. Another example is the submit
button that has to validate values of all fields before saving the data.
By having this logic implemented directly inside the code
of the form elements you make these elements’ classes much
harder to reuse in other forms of the app. For example, you won’t be
able to use that checkbox class inside another form,
because it’s coupled to the dog’s text field. You can use either all
the classes involved in rendering the profile form, or none at all.
"""

from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object) -> None:
        pass

    @abstractmethod
    def register(self, component: "Component") -> None:
        pass


class Component(ABC):
    @abstractmethod
    def __init__(self, mediator: Mediator, event: str) -> None:
        self._mediator = mediator
        self._event = event

    @property
    def event(self) -> str:
        return self._event

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @abstractmethod
    def send(self):
        self.mediator.notify(self)

    @abstractmethod
    def receive(self):
        pass


class ComponentApplication(Component):
    def __init__(self, mediator: Mediator, event: str) -> None:
        super().__init__(mediator, event)

    def send(self):
        self.mediator.notify(self)

    def receive(self):
        print(f"Received event: {self.event}")


class ComponentForm(Component):
    def __init__(self, mediator: Mediator, event: str) -> None:
        super().__init__(mediator, event)

    def send(self):
        self.mediator.notify(self)

    def receive(self):
        print(f"Received event: {self.event}")


class ConcreteMediator(Mediator):
    def __init__(self) -> None:
        self._components = []

    def register(self, component: Component) -> None:
        self._components.append(component)

    def notify(self, sender: object) -> None:
        for component in self._components:
            if component is not sender:
                component.receive()


def test():
    mediator = ConcreteMediator()
    app = ComponentApplication(mediator, 'app')
    form = ComponentForm(mediator, 'form')

    mediator.register(app)
    mediator.register(form)

    app.send()
    form.send()


test()
