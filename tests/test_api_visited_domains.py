from app import app
from tests.conftest import fill_db_links_set, funbox_domen, palletsprojects_domen, pytest_domen, \
                            stackoverflow_domen, yandex_domen, timestamp1, timestamp2, timestamp3


def test_visited_domains_from_to_same_values(fill_db_links_set):
    url = f"/visited_domains?from={timestamp2}&to={timestamp2}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 1
    assert response.json['domains'][0] == 'ya.ru'


def test_visited_domains_for_all_time(fill_db_links_set):
    url = f"/visited_domains?from={timestamp1}&to={timestamp3}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 5

    assert set(response.json['domains']) == {funbox_domen, palletsprojects_domen, pytest_domen, stackoverflow_domen,
                                             yandex_domen}


def test_visited_domains_by_first_interval(fill_db_links_set):
    url = f"/visited_domains?from={timestamp1}&to={timestamp2}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 3

    assert set(response.json['domains']) == {funbox_domen, stackoverflow_domen, yandex_domen}


def test_visited_domains_by_second_interval(fill_db_links_set):
    url = f"/visited_domains?from={timestamp2}&to={timestamp3}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 4

    assert set(response.json['domains']) == {palletsprojects_domen, pytest_domen, yandex_domen, funbox_domen}


def test_visited_domains_after_interval_interval(fill_db_links_set):
    url = f"/visited_domains?from={timestamp3+1}&to={timestamp3+200}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 0


def test_visited_domains_before_interval_interval(fill_db_links_set):
    url = f"/visited_domains?from={timestamp1-200}&to={timestamp1-1}"
    response = app.test_client().get(url)

    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(response.json['domains']) == 0
