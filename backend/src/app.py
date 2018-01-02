import json
from textwrap import dedent
from typing import List

from flask import Flask, request, send_from_directory, abort

from src import parser
from src.mock import mock_time_series

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
    day_aggregates = parser.parse_datapoint_set(datapoints)
    # TODO: submit datapoints as row associated with that community and day
    # TODO: also update running averages and current value for metric summaries
    return _generate_report(community_name, day_aggregates)


def _generate_report(community_name: str, day_aggregates: List[parser.DailyConditions]) -> str:
    report = dedent(f'''
    {community_name}
    ----------------------------
    ''')
    for day in day_aggregates:
        report += dedent(f'''
        flow average for {day['day']}: {day['flow_sum'] / day['flow_count']}
        salinity average for {day['day']}: {day['salinity_sum'] / day['salinity_count']}
        turbidity average for {day['day']}: {day['turbidity_sum'] / day['turbidity_count']}\n''')
    return dedent(report)


def return_json(result):
    if result is None:
        abort(404)
    else:
        return json.dumps(result), 200
