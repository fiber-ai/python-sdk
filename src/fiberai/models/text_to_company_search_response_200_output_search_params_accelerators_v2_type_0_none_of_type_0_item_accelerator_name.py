from enum import Enum


class TextToCompanySearchResponse200OutputSearchParamsAcceleratorsV2Type0NoneOfType0ItemAcceleratorName(str, Enum):
    A16Z_SPEEDRUN = "a16z_speedrun"
    ACCEL_ATOMS = "accel_atoms"
    AI2_INCUBATOR = "ai2_incubator"
    ALCHEMIST_ACCELERATOR = "alchemist_accelerator"
    ALLIANCE = "alliance"
    ANTLER = "antler"
    BERKELEY_SKYDECK = "berkeley_skydeck"
    FOUNDERS_INC = "founders_inc"
    GOOGLE_STARTUPS = "google_startups"
    LAUNCH_ACCELERATOR = "launch_accelerator"
    NEO = "neo"
    PEAR_X = "pear_x"
    PLUG_AND_PLAY = "plug_and_play"
    SOSV = "sosv"
    SOUTH_PARK_COMMONS = "south_park_commons"
    STARTX = "startx"
    TECHSTARS = "techstars"
    THE_MINT = "the_mint"
    YCOMBINATOR = "ycombinator"

    def __str__(self) -> str:
        return str(self.value)
