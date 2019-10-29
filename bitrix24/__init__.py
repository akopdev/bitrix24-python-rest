# -*- coding: utf-8 -*-

#   ____  _ _        _      ____  _  _     ____  _____ ____ _____
#  | __ )(_) |_ _ __(_)_  _|___ \| || |   |  _ \| ____/ ___|_   _|
#  |  _ \| | __| '__| \ \/ / __) | || |_  | |_) |  _| \___ \ | |
#  | |_) | | |_| |  | |>  < / __/|__   _| |  _ <| |___ ___) || |
#  |____/|_|\__|_|  |_/_/\_\_____|  |_|   |_| \_\_____|____/ |_|


"""
Bitrix24 REST library
~~~~~~~~~~~~~~~~~~~~~

Bitrix24 REST provides easy way to communicate with bitrix24 portal over REST without OAuth 2.0. 
usage:

   >>> from bitrix24 import Bitrix24
   >>> bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')
   >>> r = bx24.callMethod('crm.product.list')

Copyright (c) 2019 by Akop Kesheshyan.
"""

__version__ = '1.1.1'
__author__ = 'Akop Kesheshyan <akop.kesheshyan@icloud.com>'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Akop Kesheshyan'

from .bitrix24 import Bitrix24
from .exceptions import BitrixError