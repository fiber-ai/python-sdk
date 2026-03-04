from enum import Enum

class GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemTagsType0Item(str, Enum):
    ATTENDED_TOP_GLOBAL_UNIVERSITY = "attended-top-global-university"
    ATTENDED_TOP_US_UNIVERSITY = "attended-top-us-university"
    BOARD_MEMBER = "board-member"
    C_SUITE = "c-suite"
    DECISION_MAKER = "decision-maker"
    DEEP_TECHNICAL_BACKGROUND = "deep-technical-background"
    EXPERIENCED_EXECUTIVE = "experienced-executive"
    FORTUNE_500_EXECUTIVE = "fortune-500-executive"
    INFLUENCER = "influencer"
    MAJOR_TECH_COMPANY_EXPERIENCE = "major-tech-company-experience"
    PHD = "phd"
    RECENTLY_CHANGED_COMPANIES = "recently-changed-companies"
    RECENTLY_PROMOTED = "recently-promoted"
    SECOND_TIME_FOUNDER = "second-time-founder"
    STEALTH_FOUNDER = "stealth-founder"
    STUDENT = "student"

    def __str__(self) -> str:
        return str(self.value)
