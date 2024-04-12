import pytest

from bitrix24 import Bitrix24, BitrixError


def test_init_with_empty_domain():
    with pytest.raises(BitrixError):
        Bitrix24("")


def test_call_with_empty_method(b24):
    with pytest.raises(BitrixError):
        b24.callMethod("")


def test_call_non_exists_method(b24):
    with pytest.raises(BitrixError):
        b24.callMethod("hello.world")


def test_call_wrong_method(b24):
    with pytest.raises(BitrixError):
        b24.callMethod("helloworld")
