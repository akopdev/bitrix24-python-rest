import pytest

from bitrix24 import Bitrix24


@pytest.fixture
def b24():
    return Bitrix24("https://example.bitrix24.com/rest/1/123456789")
