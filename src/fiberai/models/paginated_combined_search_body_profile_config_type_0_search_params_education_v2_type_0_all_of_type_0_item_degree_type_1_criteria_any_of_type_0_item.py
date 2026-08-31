from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AllOfType0ItemDegreeType1CriteriaAnyOfType0Item(
    StrEnum
):
    ARCHITECTURE = "Architecture"
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    BUSINESS = "Business"
    DENTISTRY = "Dentistry"
    DIVINITY = "Divinity"
    DOCTORATE = "Doctorate"
    EDUCATION = "Education"
    HIGH_SCHOOL = "High School"
    LAW = "Law"
    MASTER = "Master"
    MEDICINE = "Medicine"
    NURSING = "Nursing"
    PHARMACY = "Pharmacy"
    PUBLIC_HEALTH = "Public Health"
    PUBLIC_POLICY = "Public Policy"
    SOCIAL_WORK = "Social Work"

    def __str__(self) -> str:
        return str(self.value)
