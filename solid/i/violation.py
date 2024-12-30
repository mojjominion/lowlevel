from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def eat(self) -> str:
        pass


class HumanWorker(Worker):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"


class RobotWorker(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        # Robots don't eat, but they are forced to implement this method
        raise NotImplementedError("Robots don't eat")
