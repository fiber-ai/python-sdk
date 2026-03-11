from enum import Enum


class ValidatePhoneNumberResponse200OutputIsReachable(str, Enum):
    BAD_NUMBER = "bad_number"
    NOT_REACHABLE = "not_reachable"
    REACHABLE = "reachable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
