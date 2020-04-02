from app import extract_domains
from tests.conftest import links1, yandex_domen, funbox_domen, stackoverflow_domen


def test_extract_domains():

    result = extract_domains(links1)

    assert [yandex_domen, yandex_domen, funbox_domen, stackoverflow_domen] == result
