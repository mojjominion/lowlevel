from abc import ABC, abstractmethod
from enum import Enum


class ConvertType(Enum):
    csv = 0
    excel = 1
    json = 2

class IConvert(ABC):

    @abstractmethod
    def convert_csv(self):
        pass
    @abstractmethod
    def convert_json(self):
        pass
    @abstractmethod
    def convert_excel(self):
        pass

    @abstractmethod
    def convert(self, ctype: ConvertType):
        pass


class Converter(IConvert):

    def __init__(self) -> None:
        pass

    def convert_excel(self):
            #  convert to excel
            pass
    def convert_csv(self):
            #  convert to csv
            pass
    def convert_json(self):
            #  convert to json
            pass

    def convert(self, ctype: ConvertType):
        if ctype == ConvertType.json:
            self.convert_json()
        if ctype == ConvertType.csv:
            self.convert_csv()
        if ctype == ConvertType.excel:
            self.convert_excel()


class Printer:

    def __init__(self) -> None:
        pass

    def print(self, converter: IConvert, ctype: ConvertType):
        content = converter.convert(ctype)
        # print
        pass

# Satisfies single-responsibility principle but violates OCP ; Because converter is responsible only for conversion

# REASON
# voilates open/close becaue if we have to add more conversion types we will have too modify
# 1. IConverter, and Converter class both

