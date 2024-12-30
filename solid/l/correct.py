from abc import abstractmethod

class Bird:

    @abstractmethod
    def sound(self):
        pass

class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass

class NonFlyingBird(Bird):

    def __init__(self) -> None:
        pass

class Ostrich(NonFlyingBird):

    def __init__(self) -> None:
        pass

    def sound(self):
        pass

class Parrot(FlyingBird):

    def __init__(self) -> None:
        pass

    def fly(self):
        pass

class Crow(FlyingBird):

    def __init__(self) -> None:
        pass

    def fly(self):
        pass

