import json

from flask import Flask, request, send_from_directory, abort
from .mock import mock_time_series
import mypackage.mock

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
    # TODO: get from tables flow, salinity, and turbidity
    pass


@app.route('/api/time_series/<string:community>')
def time_series(community: str):
    result = mock_time_series['body']
    return return_json(result)


@app.route('/api/time_series/', methods=['POST'])
def time_series_post():
    community_name = request.form['body']['community_name']
    datapoints = request.form['body']['datapoints']
    # TODO: parse datapoints, including into each logical day
    # TODO: submit datapoints as row associated with that community and day
    # TODO: also update running averages and current value for metric summaries
    return community_name + datapoints


def return_json(result):
    if result is None:
        abort(404)
    else:
        return json.dumps(result), 200
