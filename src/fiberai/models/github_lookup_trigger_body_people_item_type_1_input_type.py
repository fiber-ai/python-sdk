from enum import Enum


class GithubLookupTriggerBodyPeopleItemType1InputType(str, Enum):
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
