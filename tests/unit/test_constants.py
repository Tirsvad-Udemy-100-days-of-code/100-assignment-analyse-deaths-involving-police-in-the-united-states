from fatal_force import constants


def test_data_file_names_are_csv_files() -> None:
    names = [
        constants.POLICE_KILLINGS_FILE,
        constants.SHARE_RACE_BY_CITY_FILE,
        constants.MEDIAN_HOUSEHOLD_INCOME_FILE,
        constants.POVERTY_FILE,
        constants.HIGH_SCHOOL_COMPLETION_FILE,
    ]
    assert all(name.endswith(".csv") for name in names)
    assert len(set(names)) == len(names)


def test_directory_constants_have_expected_values() -> None:
    assert constants.DATA_DIR_NAME == "data"
    assert constants.SCREENSHOT_DIR == "docs/screenshots"


def test_encoding_and_prefix_have_expected_values() -> None:
    assert constants.DATA_ENCODING == "cp1252"
    assert constants.SCREENSHOT_PREFIX == "step-"
