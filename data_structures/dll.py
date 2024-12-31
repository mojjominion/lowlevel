import unittest
from typing import Any, TypeVar

T = TypeVar("T")

class DLL(dict):

    def __init__(self) -> None:
        # [prev, key, next]
        self.__root = root = []
        self.__root[:] = [root, None, root]
        self.__map = {}

    def add(self, value: Any):
        if value not in self.__map:
            root = self.__root 
            last = root[0]
            last[2] = root[0] = self.__map[value]  = [last, value, root]

    def remove(self, value: Any):
        if value in self.__map:
            link = self.__map[value] 
            last, next = link[0], link[2]
            last[2] = next
            next[0] = last
            del self.__map[value]
        else:
            raise KeyError

    def next(self):
        root = self.__root
        cur = self.__root[2]
        while cur is not root:  
            yield cur[1]
            cur = cur[2]






class DllTest(unittest.TestCase):

    def test_structural(self):
        dll = DLL()
        input = list(range(10))
        output = []

        for i in input:
            dll.add(i)

        for value in dll.next():
            output.append(value)

        self.assertEqual(input, output)

    def test_deletion(self):
        dll = DLL()
        input = list(range(10))
        output = []

        for i in input:
            dll.add(i)

        for i in [3,4,8]:
            dll.remove(i)
            input.remove(i)

        for value in dll.next():
            output.append(value)

        self.assertEqual(input, output)

    def test_deletion_till_empty(self):
        dll = DLL()
        input = list(range(10))
        output = []

        for i in input:
            dll.add(i)

        for i in input:
            dll.remove(i)
            input.remove(i)

        for value in dll.next():
            output.append(value)

        self.assertEqual(input, output)
