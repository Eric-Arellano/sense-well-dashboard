import json

from flask import Flask, request, send_from_directory, abort

from src.mock import mock_time_series
from src import parser

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


@app.route('/api/time_series', methods=['POST'])
def time_series_post():
    req_data = request.get_json()
    community_name = req_data['body']['community_name']
    datapoints = req_data['body']['datapoints']
    # day_aggregates = parser.parse_datapoint_set(datapoints)
    # TODO: submit datapoints as row associated with that community and day
    # TODO: also update running averages and current value for metric summaries
    # return community_name + datapoints
    return community_name


def return_json(result):
    if result is None:
        abort(404)
    else:
        return json.dumps(result), 200
