from dataclasses import dataclass

MIN_KILOMETERS = 15

@dataclass
class Trip:
    id: int
    kilometers: float

    @property
    def is_infrequent(self) -> bool:
        return self.kilometers > MIN_KILOMETERS
