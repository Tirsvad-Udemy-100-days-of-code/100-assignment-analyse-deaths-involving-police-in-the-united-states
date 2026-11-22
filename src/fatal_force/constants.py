"""@brief All constants of the Fatal Force project, defined once."""

DATA_DIR_NAME = "data"
SCREENSHOT_DIR = "docs/screenshots"
SCREENSHOT_PREFIX = "step-"
SCREENSHOT_SUFFIX = ".png"

DATA_ENCODING = "cp1252"

FATALITIES_FILE = "Deaths_by_Police_US.csv"
SHARE_RACE_BY_CITY_FILE = "Share_of_Race_By_City.csv"
MEDIAN_HOUSEHOLD_INCOME_FILE = "Median_Household_Income_2015.csv"
POVERTY_FILE = "Pct_People_Below_Poverty_Level.csv"
HIGH_SCHOOL_COMPLETION_FILE = "Pct_Over_25_Completed_High_School.csv"

README_DATA_HINT = "See the Setup section of README.md for where to obtain the files."

# Raw census column names (the state column is spelled two ways in the sources).
RAW_STATE_COLUMNS = ("Geographic Area", "Geographic area")
STATE_COLUMN = "state"
CITY_RAW_COLUMN = "City"
CITY_COLUMN = "city"

INCOME_COLUMN = "Median Income"
HIGH_SCHOOL_COLUMN = "percent_completed_hs"
POVERTY_COLUMN = "poverty_rate"
SHARE_COLUMNS = (
    "share_white",
    "share_black",
    "share_native_american",
    "share_asian",
    "share_hispanic",
)

# Census values that mean "not available".
CENSUS_PLACEHOLDERS = ("(X)", "-", "")
# Census values carry thousands separators and open-ended bounds such as "250,000+".
CENSUS_THOUSANDS_SEPARATOR = ","
CENSUS_BOUND_PATTERN = r"[+-]$"

# Fatalities columns and cleaning rules.
ID_COLUMN = "id"
DATE_COLUMN = "date"
DATE_FORMAT = "%d/%m/%y"
AGE_COLUMN = "age"
BOOLEAN_COLUMNS = ("signs_of_mental_illness", "body_camera")
TRUE_LABEL = "TRUE"
UNKNOWN_LABEL = "unknown"
RACE_COLUMN = "race"
UNKNOWN_FILL_COLUMNS = ("armed", RACE_COLUMN, "gender", "flee")

# Race analysis: output columns and the readable label of each race code.
RACE_CODE_COLUMN = "race_code"
DEATHS_COLUMN = "deaths"
RACE_LABELS = {
    "W": "White",
    "B": "Black",
    "H": "Hispanic",
    "A": "Asian",
    "N": "Native American",
    "O": "Other",
    UNKNOWN_LABEL: "Unknown",
}
# Legend text of each census share column, in the order of SHARE_COLUMNS.
SHARE_LABELS = ("White", "Black", "Native American", "Asian", "Hispanic")

LINE_TERMINATOR_CR = "\r"
LINE_TERMINATOR_CRLF = "\r\n"
LINE_TERMINATOR_LF = "\n"

# Chart text shared by the figures.
SOURCE_NOTE = "Source: US census data supplied with the course"
FATALITIES_SOURCE_NOTE = (
    "Source: The Washington Post database of fatal police shootings, "
    "supplied with the course"
)
