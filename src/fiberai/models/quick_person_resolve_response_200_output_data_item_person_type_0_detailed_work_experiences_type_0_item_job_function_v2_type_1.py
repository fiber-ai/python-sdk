from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemPersonType0DetailedWorkExperiencesType0ItemJobFunctionV2Type1(StrEnum):
    ACCOUNTING = "Accounting"
    ADMINISTRATIVE = "Administrative"
    ARTS_AND_DESIGN = "Arts and Design"
    BUSINESS_DEVELOPMENT = "Business Development"
    COMMUNITY_AND_SOCIAL_SERVICES = "Community and Social Services"
    CONSULTING = "Consulting"
    CUSTOMER_SUCCESS_AND_SUPPORT = "Customer Success and Support"
    EDUCATION = "Education"
    ENGINEERING = "Engineering"
    ENTREPRENEURSHIP = "Entrepreneurship"
    FINANCE = "Finance"
    HEALTHCARE_SERVICES = "Healthcare Services"
    HUMAN_RESOURCES = "Human Resources"
    INFORMATION_TECHNOLOGY = "Information Technology"
    LEGAL = "Legal"
    MARKETING = "Marketing"
    MEDIA_AND_COMMUNICATION = "Media and Communication"
    MILITARY_AND_PROTECTIVE_SERVICES = "Military and Protective Services"
    OPERATIONS = "Operations"
    OTHER = "Other"
    PRODUCT_MANAGEMENT = "Product Management"
    PROGRAM_AND_PROJECT_MANAGEMENT = "Program and Project Management"
    PURCHASING = "Purchasing"
    QUALITY_ASSURANCE = "Quality Assurance"
    REAL_ESTATE = "Real Estate"
    RESEARCH = "Research"
    SALES = "Sales"

    def __str__(self) -> str:
        return str(self.value)
