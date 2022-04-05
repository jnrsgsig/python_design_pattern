# -*- coding: utf-8 -*-
import sys


class _Const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError(f"Can't rebind const({key})")
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            raise self.ConstError(f"Can't unbind const({item})")
        raise NameError(item)


ref = sys.modules[__name__]
sys.modules[__name__] = _Const()
