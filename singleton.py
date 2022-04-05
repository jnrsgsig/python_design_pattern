# -*- coding: utf-8 -*-

"""
This module provides various implementations of Singleton design pattern
"""


class SingletonMetaclassWithDict(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonMetaclass(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DecoratorSingletonWithDict:
    def __init__(self, cls):
        self._class = cls
        self._instances = {}

    def __call__(self, *args, **kwargs):
        if self._class not in self._instances:
            self._instances[self._class] = self._class(*args, **kwargs)
        return self._instances[self._class]


class DecoratorSingleton:
    def __init__(self, cls):
        self._class = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if not isinstance(self._instance, self._class):
            self._instance = self._class(*args, **kwargs)
        return self._instance


def decorator_singleton(cls):
    _instances = {}

    # create, store, and return singleton instance
    def inner(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return inner


# TODO(Bing Zhang): wrap all tests in unittest, nose, or pytest
def _test_print_two_singletons(singleton1, singleton2):
    x = singleton1('x', y='y')
    x0_dict = x.__dict__.copy()
    x.z = 'z'
    print('singleton contents can change:', x.__dict__ != x0_dict)
    y = Singleton1('xx', y='yy')
    print('only one instance:', x is y)
    z = singleton2(1, y=2)
    print('Both derived singletons work:', x is y is not z)


class BaseClass1:
    def __init__(self, x, y=5):
        self.x = x
        self.y = y
        self.z = None


class BaseClass2:
    def __init__(self, x, y=5):
        self.x = float(x)
        self.y = float(y)
        self.z = None


def _test_metaclass_with_dict():
    class Singleton1(BaseClass1, metaclass=SingletonMetaclassWithDict):
        pass

    class Singleton2(BaseClass2, metaclass=SingletonMetaclassWithDict):
        pass

    _test_print_two_singletons(Singleton1, Singleton2)


def _test_metaclass():
    class Singleton1(BaseClass1, metaclass=SingletonMetaclass):
        pass

    class Singleton2(BaseClass2, metaclass=SingletonMetaclass):
        pass

    _test_print_two_singletons(Singleton1, Singleton2)


def _test_class_decorator_with_dict():
    @DecoratorSingletonWithDict
    class Singleton1(BaseClass1):
        pass

    @DecoratorSingletonWithDict
    class Singleton2(BaseClass2):
        pass

    _test_print_two_singletons(Singleton1, Singleton2)


def _test_class_decorator():
    @DecoratorSingleton
    class Singleton1(BaseClass1):
        pass

    @DecoratorSingleton
    class Singleton2(BaseClass2):
        pass

    _test_print_two_singletons(Singleton1, Singleton2)


def _test_function_decorator():
    @decorator_singleton
    class Singleton1(BaseClass1):
        pass

    @decorator_singleton
    class Singleton2(BaseClass2):
        pass

    _test_print_two_singletons(Singleton1, Singleton2)


def main():
    tests = [
        _test_metaclass_with_dict,
        _test_metaclass,
        _test_class_decorator_with_dict,
        _test_class_decorator,
        _test_function_decorator,
    ]
    for test in tests:
        print(test.__name__)
        test()


if __name__ == '__main__':
    main()
