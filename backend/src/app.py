import json

from flask import Flask, request, send_from_directory, abort
from .mock import mock_time_series

app = Flask(__name__,
            static_folder="../../frontend/build/static",
            template_folder="../../frontend/build")
app.url_map.strict_slashes = False


@app.route('/')
def render_react():
    return send_from_directory('../../frontend/build', 'index.html')


@app.route('/api/test')
def api_test():
    return 'Server is running! Good luck debugging :O'


@app.route('/api/metric_summaries/<string:community>')
def metric_summaries(community: str):
    pass


@app.route('/api/time_series/<string:community>')
def time_series(community: str):
    result = mock_time_series['body']
    return return_json(result)


@app.route('/api/time_series/', methods=['POST'])
def time_series_post():
    result = request.form['name'] + request.form['date'] + request.form['time_series']
    return result


def return_json(result):
    if result is None:
        abort(404)
    else:
        return json.dumps(result), 200
