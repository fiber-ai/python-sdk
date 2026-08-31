from enum import StrEnum


class KitchenSinkBulkProfileBodyThoroughnessType2Type1(StrEnum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
