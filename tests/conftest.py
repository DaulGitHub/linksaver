import pytest
from dataaccess.storage import Storage
from app import app


yandex_domen = 'ya.ru'
funbox_domen = 'funbox.ru'
stackoverflow_domen = "stackoverflow.com"
pytest_domen = 'docs.pytest.org'
palletsprojects_domen = 'flask.palletsprojects.com'

timestamp1 = 1585740049
timestamp2 = 1585740171
timestamp3 = 1585740286

links1 = [f"https://{yandex_domen}",
          f"https://{yandex_domen}?q=123",
          f"{funbox_domen}",
          f"https://{stackoverflow_domen}/questions/11828270/how-to-exit-the-vim-editor"]
links2 = [f"https://{yandex_domen}"]
links3 = [f"https://{yandex_domen}",
          f"https://{palletsprojects_domen}/en/1.1",
          f"https://{pytest_domen}/en/latest",
          f"https://{funbox_domen}/q/python.pdf"]


@pytest.fixture(scope='module')
def fill_db_links_set():
    storage = Storage(app.config['DB_HOST'])
    storage.save_links(links1, timestamp1)
    storage.save_links(links2, timestamp2)
    storage.save_links(links3, timestamp3)
    print("fill")
    yield
    storage.clear_all()
    print("clear")
