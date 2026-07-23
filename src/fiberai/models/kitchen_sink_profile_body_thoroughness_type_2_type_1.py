from enum import Enum


class KitchenSinkProfileBodyThoroughnessType2Type1(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
