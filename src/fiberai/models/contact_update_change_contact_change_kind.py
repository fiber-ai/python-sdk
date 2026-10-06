from enum import StrEnum


class ContactUpdateChangeContactChangeKind(StrEnum):
    JOB_CHANGE = "job_change"
    NEW_CONTACT_INFO = "new_contact_info"

    def __str__(self) -> str:
        return str(self.value)
