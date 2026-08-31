from enum import StrEnum


class CreateTrackerCompanyListBodyCompanySearchParamsType0JobPostingsV2Type0AllOfType0ItemJobPostingStatusType2Type1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
