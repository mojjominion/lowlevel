
from abc import ABC, abstractmethod


class IConvert(ABC):

    @abstractmethod
    def convert(self):
        pass

class EXL_Converter(IConvert):

    def __init__(self) -> None:
        pass

    def convert(self):
        #  convert to excel
        pass

class CSV_Converter(IConvert):

    def __init__(self) -> None:
        pass

    def convert(self):
        #  convert to excel
        pass

class JSON_Converter(IConvert):

    def __init__(self) -> None:
        pass

    def convert(self):
        #  convert to excel
        pass


class Printer:

    def __init__(self) -> None:
        pass

    def print(self, converter: IConvert):
        content = converter.convert()
        # print
        pass

