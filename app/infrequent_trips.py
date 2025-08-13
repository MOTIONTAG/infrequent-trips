from typing import List

from app.trip import Trip


def filter_infrequent_trips(trips: List[Trip]) -> List[Trip]:
    return [trip for trip in trips if trip.is_infrequent]
