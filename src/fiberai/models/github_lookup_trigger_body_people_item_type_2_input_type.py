from enum import StrEnum


class GithubLookupTriggerBodyPeopleItemType2InputType(StrEnum):
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
