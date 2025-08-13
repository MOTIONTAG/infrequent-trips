import unittest

from app.infrequent_trips import filter_infrequent_trips
from app.trip import Trip


class TestInfrequentTrips(unittest.TestCase):
    def test_filter_infrequent_trips(self):
        trips = [
            Trip(id=1, kilometers=20),
            Trip(id=2, kilometers=10),
            Trip(id=3, kilometers=30)
        ]

        filtered_trips = filter_infrequent_trips(trips)

        self.assertListEqual(
            [trip.id for trip in filtered_trips],
            [1, 3]
        )
