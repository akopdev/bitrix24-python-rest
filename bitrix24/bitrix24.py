#   ____  _ _        _      ____  _  _     ____  _____ ____ _____
#  | __ )(_) |_ _ __(_)_  _|___ \| || |   |  _ \| ____/ ___|_   _|
#  |  _ \| | __| '__| \ \/ / __) | || |_  | |_) |  _| \___ \ | |
#  | |_) | | |_| |  | |>  < / __/|__   _| |  _ <| |___ ___) || |
#  |____/|_|\__|_|  |_/_/\_\_____|  |_|   |_| \_\_____|____/ |_|

import asyncio
import itertools
from typing import Any, Dict, Optional
from urllib.parse import urlparse

from aiohttp import ClientSession

from .exceptions import BitrixError


class Bitrix24:
    """
    Bitrix24 API class.

    Provides an easy way to communicate with Bitrix24 portal over REST without OAuth.
    """

    def __init__(self, domain: str, timeout: int = 60):
        """
        Create Bitrix24 API object.

        Parameters
        ----------
            domain (str): Bitrix24 webhook domain
            timeout (int): Timeout for API request in seconds
        """
        self.domain = self._prepare_domain(domain)
        self.timeout = timeout

    def _prepare_domain(self, domain: str) -> str:
        """Normalize user passed domain to a valid one."""
        if not domain:
            raise BitrixError("Empty domain")

        o = urlparse(domain)
        user_id, code = o.path.split("/")[2:4]
        return "{0}://{1}/rest/{2}/{3}".format(o.scheme, o.netloc, user_id, code)

    def _prepare_params(self, params: Dict[str, Any], prev="") -> str:
        """
        Transform list of parameters to a valid bitrix array.

        Parameters
        ----------
            params (dict): Dictionary of parameters
            prev (str): Previous key

        Returns
        -------
            str: Prepared parameters
        """
        ret = ""
        if isinstance(params, dict):
            for key, value in params.items():
                if isinstance(value, dict):
                    if prev:
                        key = "{0}[{1}]".format(prev, key)
                    ret += self._prepare_params(value, key)
                elif (isinstance(value, list) or isinstance(value, tuple)) and len(value) > 0:
                    for offset, val in enumerate(value):
                        if isinstance(val, dict):
                            ret += self._prepare_params(
                                val, "{0}[{1}][{2}]".format(prev, key, offset)
                            )
                        else:
                            if prev:
                                ret += "{0}[{1}][{2}]={3}&".format(prev, key, offset, val)
                            else:
                                ret += "{0}[{1}]={2}&".format(key, offset, val)
                else:
                    if prev:
                        ret += "{0}[{1}]={2}&".format(prev, key, value)
                    else:
                        ret += "{0}={1}&".format(key, value)
        return ret

    async def request(self, method: str, params: str = None) -> Dict[str, Any]:
        async with ClientSession() as session:
            async with session.get(
                f"{self.domain}/{method}.json", params=params, timeout=self.timeout
            ) as resp:
                if resp.status not in [200, 201]:
                    raise BitrixError(f"HTTP error: {resp.status}")
                response = await resp.json()
                if "error" in response:
                    raise BitrixError(response["error_description"], response["error"])
                return response

    async def call(self, method: str, params: Dict[str, Any] = {}, start: Optional[int] = None):
        """Async call a REST method with specified parameters.

        This method is a replacement for the callMethod method, which is synchronous.

        Parameters
        ----------
            method (str): REST method name
            params (dict): Optional arguments which will be converted to a POST request string
        """
        if start is not None:
            params["start"] = start

        payload = self._prepare_params(params)
        res = await self.request(method, payload)

        if "next" in res and start is None:
            tasks = [self.call(method, params, start=start) for start in range(res["total"] // 50)]
            items = await asyncio.gather(*tasks)
            result = list(itertools.chain(*items))
            return res["result"] + result
        return res["result"]

    def callMethod(self, method: str, params: Dict[str, Any] = {}, **kwargs):
        """Call a REST method with specified parameters.

        Parameters
        ----------
            method (str): REST method name
            params (dict): Optional arguments which will be converted to a POST request string

        Returns
        -------
            Returning the REST method response as an array, an object or a scalar
        """
        if not method or len(method.split(".")) < 2:
            raise BitrixError("Wrong method name", 400)

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(self.call(method, params or kwargs))
            loop.close()
        else:
            result = asyncio.ensure_future(self.call(method, params or kwargs))
        return result
