import pytest
from aioresponses import aioresponses

from bitrix24 import Bitrix24


@pytest.mark.asyncio()
async def test_async_call_method(b24: Bitrix24):
    with aioresponses() as m:
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/user.get.json?ID=1&start=0",
            payload={"result": [{"ID": 1}]},
            status=200,
        )
        res = await b24.callMethod("user.get", {"ID": 1})
        assert res[0]["ID"] == 1
