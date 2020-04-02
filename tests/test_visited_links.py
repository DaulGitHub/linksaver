import time
from app import app
from tests.conftest import yandex_domen, connect_db, links1 as request_links1, links3 as request_links2


def replace_timestamp(link):

    protocol_end_position = 6
    return link[:link.index(':', protocol_end_position)]


method = '/visited_links'


def test_visited_links_save_one_link(connect_db):
    yandex_link = f"http://{yandex_domen}/123"
    time_from = int(time.time())
    response = app.test_client().post(method, json={"links": [yandex_link]})
    time_to = int(time.time())

    storage = connect_db
    links = storage.get_links(time_from, time_to)
    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert len(links) == 1
    link = replace_timestamp(links[0])
    assert link == yandex_link


def test_visited_links_save_two_sets(connect_db):
    time_from = int(time.time())
    response1 = app.test_client().post(method, json={"links": request_links1})
    response2 = app.test_client().post(method, json={"links": request_links2})
    time_to = int(time.time())

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json['status'] == 'ok'
    assert response2.json['status'] == 'ok'

    storage = connect_db
    links = storage.get_links(time_from, time_to)
    response_links = []
    for link in links:
        response_links.append(replace_timestamp(link))

    request_links = []
    request_links.extend(request_links1)
    request_links.extend(request_links2)
    assert set(response_links) == set(request_links)