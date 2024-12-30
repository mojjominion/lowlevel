from abc import ABC, abstractmethod

class IWork(ABC):
    @abstractmethod
    def work(self) -> str:
        pass


class IEat(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass


class HumanWorker(IWork, IEat):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"


class RobotWorker(IWork):
    def work(self):
        return "Robot is working"

