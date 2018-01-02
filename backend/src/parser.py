from typing import List, Dict

import pandas
import numpy

Datapoint = Dict[str, float]
DailyConditions = Dict[str, float]


def parse_datapoint_set(datapoints: List[Datapoint]) -> List[DailyConditions]:
    data_frame = _convert_to_pandas(datapoints)
    grouped = _group_by_day(data_frame)
    aggregated = _get_count_and_sum_per_day(grouped)
    return _parse_into_daily_conditions(aggregated)


def _convert_to_pandas(datapoints: List[Datapoint]) -> pandas.DataFrame:
    raw_dates = [d['timestamp'] for d in datapoints]
    dates = pandas.to_datetime(raw_dates, unit='s')
    return pandas.DataFrame(datapoints, index=dates, columns=['flow', 'salinity', 'turbidity'])


def _group_by_day(data_frame: pandas.DataFrame):
    return data_frame.groupby(pandas.Grouper(freq='D'))


def _get_count_and_sum_per_day(groups) -> pandas.DataFrame:
    count = groups.count()
    count.columns = ['flow_count', 'salinity_count', 'turbidity_count']
    sum_ = groups.sum()
    sum_.columns = ['flow_sum', 'salinity_sum', 'turbidity_sum']
    join = count.join(sum_, how='outer')
    sorted_ = join.sort_index(axis=1)
    rounded = sorted_.round({'flow_sum': 2, 'salinity_sum': 2, 'turbidity_sum': 4})
    rounded['flow_count'] = rounded['flow_count'].apply(numpy.int)  # TODO: doesn't actually make int
    rounded['salinity_count'] = rounded['salinity_count'].apply(numpy.int)
    rounded['turbidity_count'] = rounded['turbidity_count'].apply(numpy.int)
    return rounded


def _parse_into_daily_conditions(aggregated: pandas.DataFrame) -> List[DailyConditions]:
    results = aggregated.to_dict(orient='index')
    day_indexes = list(results)
    daily_conditions: List[DailyConditions] = []
    for day in day_indexes:
        day_values = results[day]
        daily_condition = {'day': day.date(),
                           'flow_count': day_values['flow_count'],
                           'flow_sum': day_values['flow_sum'],
                           'turbidity_count': day_values['turbidity_count'],
                           'turbidity_sum': day_values['turbidity_sum'],
                           'salinity_count': day_values['salinity_count'],
                           'salinity_sum': day_values['salinity_sum'],
                           }
        daily_conditions.append(daily_condition)
    return daily_conditions

