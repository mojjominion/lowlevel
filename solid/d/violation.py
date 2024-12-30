class Keyboard:
    def input(self):
        return "Keyboard input"


class Monitor:
    def display(self, content):
        print(f"Displaying: {content}")


class Computer:
    def __init__(self):
        self.keyboard = Keyboard()  # Directly depends on the concrete Keyboard class
        self.monitor = Monitor()    # Directly depends on the concrete Monitor class

    def compute(self):
        user_input = self.keyboard.input()
        self.monitor.display(f"Processing: {user_input}")


# Violates dependency inversion cause Computer is dependent on concrete implementation of Keyboard and Monitor
