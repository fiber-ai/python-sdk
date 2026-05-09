from enum import Enum


class TiktokPopularCreatorsBodyCountryType1(str, Enum):
    ARE = "ARE"
    AUS = "AUS"
    BRA = "BRA"
    CAN = "CAN"
    DEU = "DEU"
    EGY = "EGY"
    ESP = "ESP"
    FRA = "FRA"
    GBR = "GBR"
    IDN = "IDN"
    ISR = "ISR"
    ITA = "ITA"
    JPN = "JPN"
    KOR = "KOR"
    MYS = "MYS"
    PHL = "PHL"
    RUS = "RUS"
    SAU = "SAU"
    SGP = "SGP"
    THA = "THA"
    TUR = "TUR"
    TWN = "TWN"
    USA = "USA"
    VNM = "VNM"

    def __str__(self) -> str:
        return str(self.value)
