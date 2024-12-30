from abc import ABC, abstractmethod

class IKeyboard:
    @abstractmethod
    def input(self)->str:
        pass

class IMonitor(ABC):
    @abstractmethod
    def display(self, content):
        pass


class Keyboard(IKeyboard):
    def input(self):
        return "Keyboard input"

class Monitor:
    def display(self, content):
        print(f"Displaying: {content}")


class Computer:
    def __init__(self, keyboard: IKeyboard, monitor: IMonitor):
        self.keyboard = keyboard
        self.monitor = monitor

    def compute(self):
        user_input = self.keyboard.input()
        self.monitor.display(f"Processing: {user_input}")

