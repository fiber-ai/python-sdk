from enum import Enum


class SyncCombinedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1(str, Enum):
    ACCOUNTING = "accounting"
    ADMINISTRATIVE = "administrative"
    ARTS_AND_DESIGN = "arts_and_design"
    BUSINESS_DEVELOPMENT = "business_development"
    CONSULTING = "consulting"
    DATA_SCIENCE = "data_science"
    EDUCATION = "education"
    ENGINEERING = "engineering"
    ENTREPRENEURSHIP = "entrepreneurship"
    FINANCE = "finance"
    HUMAN_RESOURCES = "human_resources"
    INFORMATION_TECHNOLOGY = "information_technology"
    LEGAL = "legal"
    MARKETING = "marketing"
    MEDIA_AND_COMMMUNICATION = "media_and_commmunication"
    OPERATIONS = "operations"
    PRODUCT_MANAGEMENT = "product_management"
    SALES = "sales"
    SUPPORT = "support"
    VALUE_0 = "_all_employees"

    def __str__(self) -> str:
        return str(self.value)
