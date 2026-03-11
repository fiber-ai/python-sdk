from enum import Enum


class ValidatePhoneNumberResponse200OutputValidationStatus(str, Enum):
    INVALID = "invalid"
    UNKNOWN = "unknown"
    VALID_NOT_REACHABLE = "valid_not_reachable"
    VALID_REACHABLE = "valid_reachable"

    def __str__(self) -> str:
        return str(self.value)
