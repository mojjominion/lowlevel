from abc import ABC, abstractmethod

class Bird:

    def __init__(self) -> None:
        pass

    def fly(self):
        pass

class Ostrich:

    def __init__(self) -> None:
        pass

    def fly(self):
        raise NotImplemented

class Parrot:

    def __init__(self) -> None:
        pass

    def fly(self):
        pass

class Crow:

    def __init__(self) -> None:
        pass

    def fly(self):
        pass


# voilates Liskov's substitution becaue Ostrich can not be used as Bird in pre-existing code

