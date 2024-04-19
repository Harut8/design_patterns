"""
Imagine that you’re working on a new text-editor app.
Your current task is to create a toolbar with a bunch of buttons
for various operations of the editor. You created a very neat
Button class that can be used for buttons on the toolbar, as well as for generic buttons in various dialogs.
While all of these buttons look similar, they’re all supposed to do different things.
Where would you put the code for the various click handlers of these buttons?
The simplest solution is to create tons of subclasses for each place where the button is used.
These subclasses would contain the code that would have to be executed on a button click.
Before long, you realize that this approach is deeply flawed.
First, you have an enormous number of subclasses, and that would be okay
if you weren’t risking breaking the code in these subclasses each time you modify
the base Button class. Put simply, your GUI code has become awkwardly
dependent on the volatile code of the business logic.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Interface Command declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class GarageOpenCommand(Command):
    """
    Implements interface Command and provides open garage door functionality
    """

    def __init__(self, garage_receiver):
        self._garage_receiver = garage_receiver

    def execute(self) -> None:
        print("Command to open garage door.")
        self._garage_receiver.open_door()


class GarageCloseCommand(Command):
    """
    Implements interface Command and provides close garage door functionality
    """

    def __init__(self, garage_receiver):
        self._garage_receiver = garage_receiver

    def execute(self) -> None:
        print("Command to close garage door")
        self._garage_receiver.close_door()


class GarageReceiver:
    """
    Garage door endpoints to open and close the door
    """

    def open_door(self):
        print("Opening garage door.")

    def close_door(self):
        print("Closing garage door")


class ApplicationInvoker:
    """
    Application code to provide APIs for opening and closing of the door
    """

    def __init__(self):
        receiver = GarageReceiver()
        self._open_door = GarageOpenCommand(garage_receiver=receiver)
        self._close_door = GarageCloseCommand(garage_receiver=receiver)

    def invoke_open_door(self):
        print("App initiated garage door open.")
        self._open_door.execute()

    def invoke_close_door(self):
        print("App initiated garage door close.")
        self._close_door.execute()


def test():
    # create object for class ApplicationInvoker
    app = ApplicationInvoker()

    # let's call open door first
    app.invoke_open_door()
    print()

    # let's close the door
    app.invoke_close_door()
