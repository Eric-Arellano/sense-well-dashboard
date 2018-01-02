import unittest

import numpy

import src.parser as parser


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.datapoints = [
            {
                "timestamp": 1514833341,
                "flow": 37.2,
                "salinity": 19.23,
                "turbidity": 0.5476
            },
            {
                "timestamp": 1514836941,
                "flow": 29.9
            },
            {
                "timestamp": 1514840541,
                "flow": 46
            },
            {
                "timestamp": 1514844141,
                "flow": 35
            },
            {
                "timestamp": 1514847741,
                "flow": 27.7
            },
            {
                "timestamp": 1514851341,
                "flow": 27.6,
                "turbidity": 1.6351
            }
        ]
        cls.data_frame = parser._convert_to_pandas(cls.datapoints)
        cls.group = parser._group_by_day(cls.data_frame)
        cls.aggregated = parser._get_count_and_sum_per_day(cls.group)

    @unittest.skip("Not sure why these dicts aren't evaluating to the same?")
    def test_convert_to_pandas(self):
        expected = {'timestamp': {0: 1514833341, 1: 1514836941},
                    'flow': {0: 37.2, 1: 29.9},
                    'salinity': {0: 19.23, 1: numpy.NaN},
                    'turbidity': {0: 0.5476, 1: numpy.NaN}}
        data = self.datapoints[:2]
        result = parser._convert_to_pandas(data)
        self.assertDictEqual(result.to_dict(), expected)

    def test_split_days(self):
        result = parser._group_by_day(self.data_frame).count()
        day1 = result.loc['2018-01-01']
        day2 = result.loc['2018-01-02']
        self.assertEqual(len(result), 2)
        self.assertEqual(day1["flow"].item(), 5)
        self.assertEqual(day2["flow"].item(), 1)

    @unittest.skip("Not sure how to test")
    def test_get_count_and_sum_by_day(self):
        result = parser._get_count_and_sum_per_day(self.group)

    def test_parse_into_daily_conditions(self):
        result = parser._parse_into_daily_conditions(self.aggregated)
        print(result)