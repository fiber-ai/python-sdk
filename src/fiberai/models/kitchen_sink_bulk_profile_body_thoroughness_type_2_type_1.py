from enum import Enum


class KitchenSinkBulkProfileBodyThoroughnessType2Type1(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
