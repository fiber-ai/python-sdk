from enum import StrEnum


class ValidatePhoneNumberResponse200OutputIsReachable(StrEnum):
    BAD_NUMBER = "bad_number"
    NOT_REACHABLE = "not_reachable"
    REACHABLE = "reachable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
