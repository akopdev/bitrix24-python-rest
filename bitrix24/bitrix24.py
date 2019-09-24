# -*- coding: utf-8 -*-

"""
Bitrix24
~~~~~~~~~~~~

This module implements the Bitrix24 REST API.

:copyright: (c) 2019 by Akop Kesheshyan.

"""
import requests
from time import sleep
from .exceptions import BitrixError


class Bitrix24(object):
    """A user-created :class:`Bitrix24 <Bitrix24>` object.
    Used to sent to the server.

    :param domain: REST call domain, including account name, user ID and secret code.
    :param timeout: (Optional) waiting for a response after a given number of seconds.
    Usage::
      >>> from bitrix24 import Bitrix24
      >>> bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')
      >>> bx24.callMethod('crm.product.list')
    """

    def __init__(self, domain, timeout=60):
        self.domain = domain
        self.timeout = timeout

    def _prepare_params(self, params):
        """Transforms list of params to a valid bitrix array."""

        new_params = {}
        for index, value in params.items():
            if type(value) is dict:
                for i, v in value.items():
                    new_params['%s[%s]' % (index, i)] = v
            else:
                new_params[index] = value
        return new_params

    def callMethod(self, method, **params):
        """Calls a REST method with specified parameters.

       :param url: REST method name.
       :param \*\*params: Optional arguments which will be converted to a POST request string.
       :return: Returning the REST method response as an array, an object or a scalar
       """

        try:
            url = '{0}/{1}.json'.format(self.domain, method)

            p = self._prepare_params(params)

            if method.rsplit('.', 1)[0] in ['add', 'update', 'delete', 'set']:
                r = requests.post(url, data=p, timeout=self.timeout).json()
            else:
                r = requests.get(url, params=p, timeout=self.timeout).json()
        except ValueError:
            if r['error'] not in 'QUERY_LIMIT_EXCEEDED':
                raise BitrixError(r)
            # Looks like we need to wait until expires limitation time by Bitrix24 API
            sleep(2)
            return self.callMethod(method, **params)
        
        if 'error' in r:
            raise BitrixError(r)
        if 'page' not in params:
            params['page'] = 1
        if 'next' in r and r['total'] > (r['next']*params['page']):
            params['page'] += 1
            return r['result'] + self.callMethod(method, **params)
        return r['result']
