#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Record time when call function
Author: Hunter-0x07
Finish_Date: 2020-11-27 20:31
"""

from time import localtime, strftime
import os
import logging


def record_decorator(func):
    """
    Save execution's records to system log
    """
    filename = "/var/log/python-{}/{}.log".format(
        strftime('%Y-%m-%d', localtime()),
        strftime('%H-%M-%S', localtime())
    )

    if not os.path.exists(os.path.dirname(filename)):
        # Determine whether there is a path
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as e:
            raise e

    # Logging config
    logging.basicConfig(filename=filename,
                        filemode='w',
                        level=logging.DEBUG)

    # Logging time to log
    logging.info('Call function time: {}'.format(
        strftime('%Y-%m-%d %X', localtime())
    ))

    def inner(n):
        return func(n)

    return inner


@record_decorator
def fib(n):
    """
    For fibonacci number
    :param n: int
    :return: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    """Entrance of Programming"""
    print(fib(4))


if __name__ == "__main__":
    main()
