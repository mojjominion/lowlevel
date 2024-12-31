import unittest
from threading import Lock, Thread
from time import sleep


class NaiveSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            sleep(1)
            cls._instance = super(NaiveSingleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def destroy(cls):
        cls._instance = None

    def __init__(self):
        pass


class ThreadSafeSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            sleep(1)
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def destroy(cls):
        cls._instance = None

    def __init__(self):
        pass


def getNaiveInstance(instances: list[int]):
    s1 = NaiveSingleton()
    instances.append(id(s1))


def getThreadSafeInstance(instances: list[int]):
    s1 = ThreadSafeSingleton()
    instances.append(id(s1))


class SingletonTest(unittest.TestCase):
    def tearDown(self) -> None:
        NaiveSingleton.destroy()

    def test_singleton(self):
        instances = []
        getNaiveInstance(instances)
        getNaiveInstance(instances)
        self.assertEqual(len(set(instances)), 1)

    def test_naive_singleton_concurrent_failure(self):
        instances = []
        pool = [Thread(target=getNaiveInstance, args=(instances,)) for _ in range(10)]
        for t in pool:
            t.start()
        for p in pool:
            p.join()
        self.assertEqual(len(set(instances)) > 1, True)

    def test_thread_safe_singleton_concurrent(self):
        instances = []
        pool = [
            Thread(target=getThreadSafeInstance, args=(instances,)) for _ in range(10)
        ]
        for t in pool:
            t.start()
        for p in pool:
            p.join()
        self.assertEqual(len(set(instances)) == 1, True)
