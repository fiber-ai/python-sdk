from enum import Enum


class KitchenSinkProfileBodyThoroughnessType3Type1(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
