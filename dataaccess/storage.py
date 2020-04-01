import redis


def map_vals(vals: list, score: int):

    return {val: score for val in vals}


class Storage:

    _links_key = "urls"

    def __init__(self, host: str):

        self._db = redis.Redis(host)

    def save_links(self, links: list, timestamp: int):

        mapped_vals = map_vals(links, timestamp)
        self._db.zadd(self._links_key, mapped_vals)

    def get_links(self, timestamp_from: int, timestamp_to: int) -> list:

        links = self._db.zrangebyscore(self._links_key, timestamp_from, timestamp_to)
        links = [link.decode('utf-8') for link in links]

        return links
