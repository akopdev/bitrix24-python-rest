import pytest
from aioresponses import aioresponses
from bitrix24 import Bitrix24


@pytest.mark.asyncio
async def test_concurrent_requests(b24):
    with aioresponses() as m:
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/crm.deal.list.json?start=0",
            payload={"result": [{"ID": 1}], "next": 50, "total": 82},
            status=200,
            repeat=True,
        )
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/crm.deal.list.json?start=50",
            payload={"result": [{"ID": 2}], "total": 82},
            status=200,
            repeat=True,
        )
        res = await b24.callMethod("crm.deal.list")
        assert res == [{"ID": 1}, {"ID": 2}]


@pytest.mark.asyncio
async def test_concurrent_requests_nesting_level(b24):
    with aioresponses() as m:
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/tasks.task.list.json?start=0",
            payload={"result": {"tasks": [{"ID": 1}]}, "next": 50, "total": 100},
            status=200,
            repeat=True,
        )
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/tasks.task.list.json?start=50",
            payload={"result": {"tasks": [{"ID": 2}]}, "total": 100},
            status=200,
            repeat=True,
        )
        res = await b24.callMethod("tasks.task.list")
        assert res == {"tasks": [{"ID": 1}, {"ID": 2}]}


@pytest.mark.asyncio
async def test_request_with_disabled_pagination():
    b24 = Bitrix24("https://example.bitrix24.com/rest/1/123456789", fetch_all_pages=False)
    with aioresponses() as m:
        m.get(
            "https://example.bitrix24.com/rest/1/123456789/crm.deal.list.json?start=0",
            payload={"result": [{"ID": 1}], "next": 50, "total": 100},
            status=200,
            repeat=True,
        )
        res = await b24.callMethod("crm.deal.list")
        assert res == [{"ID": 1}]
