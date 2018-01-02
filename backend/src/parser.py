from typing import List, Dict

import pandas

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
    return join.sort_index(axis=1)  # sort column names alphabetically


def _parse_into_daily_conditions(aggregated: pandas.DataFrame) -> List[DailyConditions]:
    r = aggregated.to_dict(orient='index')
    print(r)
    r2 = dict((key.date(), value) for (key, value) in r)
    print(r2)
    raise NotImplementedError('Figure out how to convert to List of Dicts, with keys "day", "x_count", and "x_sum"')
    # return [{'day': d, 'flow_count': d['flow_count']} for d in r]
