import pytest
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_rate_limit_exceeded(b24):
    with aioresponses() as m:
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/crm.deal.list.json?start=0",
            payload={"error": "QUERY_LIMIT_EXCEEDED"},
            status=200,
        )
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/crm.deal.list.json?start=0",
            payload={"result": [{"ID": 1}], "total": 100},
            status=200
        )
        res = await b24.callMethod("crm.deal.list")
        assert res == [{"ID": 1}]
