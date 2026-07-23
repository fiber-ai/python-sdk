from enum import Enum


class KitchenSinkBulkProfileBodyThoroughnessType3Type1(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
