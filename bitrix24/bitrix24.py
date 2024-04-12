#   ____  _ _        _      ____  _  _     ____  _____ ____ _____
#  | __ )(_) |_ _ __(_)_  _|___ \| || |   |  _ \| ____/ ___|_   _|
#  |  _ \| | __| '__| \ \/ / __) | || |_  | |_) |  _| \___ \ | |
#  | |_) | | |_| |  | |>  < / __/|__   _| |  _ <| |___ ___) || |
#  |____/|_|\__|_|  |_/_/\_\_____|  |_|   |_| \_\_____|____/ |_|

import warnings
from time import sleep
from typing import Any, Dict
from urllib.parse import urlparse

import requests

from .exceptions import BitrixError


class Bitrix24:
    """
    Bitrix24 API class.

    Provides an easy way to communicate with Bitrix24 portal over REST without OAuth.
    """

    def __init__(self, domain: str, timeout: int = 60, safe: bool = True):
        """
        Create Bitrix24 API object.

        Parameters
        ----------
            domain (str): Bitrix24 webhook domain
            timeout (int): Timeout for API request in seconds
        """
        self.domain = self._prepare_domain(domain)
        self.timeout = timeout
        self.safe = safe

    def _prepare_domain(self, domain: str):
        """Normalize user passed domain to a valid one."""
        if not domain:
            raise BitrixError("Empty domain")

        o = urlparse(domain)
        user_id, code = o.path.split("/")[2:4]
        return "{0}://{1}/rest/{2}/{3}".format(o.scheme, o.netloc, user_id, code)

    def _prepare_params(self, params: Dict[str, Any], prev=""):
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

    def request(self, method, p):
        url = "{0}/{1}.json".format(self.domain, method)
        if method.rsplit(".", 1)[0] in ["add", "update", "delete", "set"]:
            r = requests.post(url, data=p, timeout=self.timeout, verify=self.safe).json()
        else:
            r = requests.get(url, params=p, timeout=self.timeout, verify=self.safe)
        try:
            r = r.json()
        except requests.exceptions.JSONDecodeError:
            warnings.warn("bitrix24: JSON decode error...")
            if r.status_code == 403:
                warnings.warn(
                    f"bitrix24: Forbidden: {method}. "
                    "Check your bitrix24 webhook settings. Returning None! "
                )
                return None
            elif r.ok:
                return r.content

    def callMethod(self, method: str, **params):
        """Call a REST method with specified parameters.

        Parameters
        ----------
            method (str): REST method name
            params (dict): Optional arguments which will be converted to a POST request string

        Returns
        -------
            Returning the REST method response as an array, an object or a scalar
        """
        if not method or len(method.split(".")) < 3:
            raise BitrixError("Wrong method name", 400)

        try:
            p = self._prepare_params(params)
            r = self.request(method, p)
            if not r:
                return None
        except ValueError:
            if r["error"] not in "QUERY_LIMIT_EXCEEDED":
                raise BitrixError(message=r["error_description"], code=r["error"])
            # Looks like we need to wait until expires limitation time by Bitrix24 API
            sleep(2)
            return self.callMethod(method, **params)

        if "error" in r:
            raise BitrixError(r)
        if "start" not in params:
            params["start"] = 0
        if "next" in r and r["total"] > params["start"]:
            params["start"] += 50
            data = self.callMethod(method, **params)
            if isinstance(r["result"], dict):
                result = r["result"].copy()
                result.update(data)
            else:
                result = r["result"] + data
            return result
        return r["result"]
