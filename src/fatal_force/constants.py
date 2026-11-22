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
ARMED_COLUMN = "armed"
GENDER_COLUMN = "gender"
FLEE_COLUMN = "flee"
MANNER_COLUMN = "manner_of_death"
THREAT_LEVEL_COLUMN = "threat_level"
MENTAL_ILLNESS_COLUMN = BOOLEAN_COLUMNS[0]
UNKNOWN_FILL_COLUMNS = (ARMED_COLUMN, RACE_COLUMN, GENDER_COLUMN, FLEE_COLUMN)

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

# Victim analysis: generic count columns and the label of an unarmed victim.
VALUE_COLUMN = "value"
COUNT_COLUMN = "count"
UNARMED_LABEL = "unarmed"

# Geography analysis: census place-type suffixes dropped when matching city names.
CITY_SUFFIXES = (
    "city and borough",
    "urban county",
    "municipality",
    "township",
    "borough",
    "village",
    "town",
    "city",
    "cdp",
    "(balance)",
)
# Race groups compared with the census, and the census column of each.
RACE_GROUPS = ("W", "B", "H", "A", "N")
RACE_SHARE_COLUMNS = {
    "W": "share_white",
    "B": "share_black",
    "H": "share_hispanic",
    "A": "share_asian",
    "N": "share_native_american",
}
VICTIM_SHARE_COLUMN = "victim_share"
POPULATION_SHARE_COLUMN = "population_share"
RATIO_COLUMN = "ratio"
CITY_LABEL_COLUMN = "city_label"
DEFAULT_TOP_CITIES = 10

# Timeline analysis: output columns.
MONTH_COLUMN = "month"
YEAR_COLUMN = "year"
ROLLING_MEAN_SUFFIX = "_rolling_mean"

# Map figure size in pixels.
MAP_WIDTH = 1100
MAP_HEIGHT = 650

LINE_TERMINATOR_CR = "\r"
LINE_TERMINATOR_CRLF = "\r\n"
LINE_TERMINATOR_LF = "\n"

# Chart text shared by the figures.
SOURCE_NOTE = "Source: US census data supplied with the course"
FATALITIES_SOURCE_NOTE = (
    "Source: The Washington Post database of fatal police shootings, "
    "supplied with the course"
)
