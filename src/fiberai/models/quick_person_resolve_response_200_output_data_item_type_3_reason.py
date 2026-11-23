from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemType3Reason(StrEnum):
    CRUNCHBASE_ORGANIZATION_URL = "crunchbase_organization_url"
    CRUNCHBASE_UUID = "crunchbase_uuid"
    EMPTY = "empty"
    NOT_A_CRUNCHBASE_PERSON_URL = "not_a_crunchbase_person_url"
    NOT_A_LINKEDIN_PROFILE_URL = "not_a_linkedin_profile_url"
    NOT_A_LINKEDIN_SLUG = "not_a_linkedin_slug"
    NOT_A_LINKEDIN_USER_ID = "not_a_linkedin_user_id"

    def __str__(self) -> str:
        return str(self.value)
