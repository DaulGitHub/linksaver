import time
from urllib.parse import urlparse
from flask import Flask, g, request, jsonify
from dataaccess.storage import Storage


app = Flask(__name__)
app.config.from_object('config.dev.DevelopmentConfig')


def get_db():
    if not hasattr(g, 'storage'):
        g.storage = Storage(app.config['DB_HOST'])
    return g.storage


@app.before_request
def before_request():
    g.storage = get_db()


def extract_domains(links: list) -> list:

    return [urlparse(link).hostname for link in links]


@app.route('/visited_links', methods=['POST'])
def save_links():

    data = request.get_json()

    links = data['links']
    timestamp = int(time.time())
    g.storage.save_links(links, timestamp)

    return jsonify({"status": "ok"})


@app.route('/visited_domains', methods=['GET'])
def get_domains():

    time_from = request.args.get('from')
    time_to = request.args.get('to')

    links = g.storage.get_links(int(time_from), int(time_to))
    domains = extract_domains(links)

    return jsonify({"domains": domains, "status": "ok"})
