# -*- coding: utf-8 -*-
import inspect
import functools


def check_type(fn):
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        params = inspect.signature(fn).parameters
        for k, v in kwargs.items():
            param = params[k]
            if param.annotation != inspect._empty and not isinstance(
                    v, param.annotation):
                raise TypeError('parameter {} required {}, but {}'.format(
                    k, param.annotation, type(v)))
        for i, arg in enumerate(args):
            param = list(params.values())[i]
            if param.annotation != inspect._empty and not isinstance(
                    arg, param.annotation):
                raise TypeError('parameter {} required {}, but {}'.format(
                    param.name, param.annotation, type(arg)))
        return fn(*args, **kwargs)

    return wrap


@check_type
def add(x: int, y: int):
    return x + y


a = add(1, y=2)
print(a)

a = add(1, y='2')
print(a)