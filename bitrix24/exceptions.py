# -*- coding: utf-8 -*-

"""
Bitrix24.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Bitrix24 REST exceptions.

:copyright: (c) 2019 by Akop Kesheshyan.

"""


class BitrixError(ValueError):
    def __init__(self, response):
        super().__init__(response['error_description'])
        self.code = response['error']
