import unittest
import mypackage.parser


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
                "flow": 27.6
            }
        ]

    def test_split_days(self):
        pass