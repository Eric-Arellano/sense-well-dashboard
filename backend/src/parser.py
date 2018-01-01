from typing import List, Dict

Datapoint = Dict[str, float]
DailyConditions = Dict[str, float]


def parse_datapoint_set(datapoints: List[Datapoint]) -> List[DailyConditions]:
    datapoints_by_day = split_into_dates(datapoints)
    daily_conditions: List[DailyConditions] = []
    for day in datapoints_by_day:
        daily_condition = parse_day_into_daily_conditions(day)
        daily_conditions.append(daily_condition)
    return daily_conditions


def split_into_dates(datapoints: List[Datapoint]) -> List[List[Datapoint]]:
    raise NotImplementedError


def parse_day_into_daily_conditions(datapoints: List[Datapoint]) -> DailyConditions:
    raise NotImplementedError
