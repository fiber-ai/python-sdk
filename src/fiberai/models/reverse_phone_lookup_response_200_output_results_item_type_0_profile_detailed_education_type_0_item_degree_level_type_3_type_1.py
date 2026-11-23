from enum import StrEnum


class ReversePhoneLookupResponse200OutputResultsItemType0ProfileDetailedEducationType0ItemDegreeLevelType3Type1(
    StrEnum
):
    ARCHITECTURE = "Architecture"
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    BUSINESS = "Business"
    CERTIFICATE = "Certificate"
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
