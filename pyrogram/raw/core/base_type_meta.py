from typing import get_args


class BaseTypeMeta(type):
    def __instancecheck__(cls, instance):
        return isinstance(instance, get_args(cls.__union_types__))

    def __subclasscheck__(cls, subclass):
        return issubclass(subclass, get_args(cls.__union_types__))