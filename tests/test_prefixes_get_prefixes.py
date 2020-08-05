"""Return prefixes dictionary from reading prefixes file."""

import os
from pathlib import Path
import pytest
from csv2shex.config import PREFIXFILE_NAME
from csv2shex.prefixes import get_prefixes


PREFIXFILE_CONTENT = (
    "prefixes:\n"
    "    dc: http://purl.org/dc/elements/1.1/\n"
    "    dcterms: http://purl.org/dc/terms/\n"
)

PREFIXES_PYOBJ = {
    "prefixes": {
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
    }
}


def test_get_prefixes(tmp_path):
    """Return dictionary of configuration settings from YAML file."""
    os.chdir(tmp_path)
    Path(PREFIXFILE_NAME).write_text(PREFIXFILE_CONTENT)
    assert get_prefixes() == PREFIXES_PYOBJ


def test_get_prefixes_from_prefixfile_with_lines_commented_out(tmp_path):
    """Return configuration dictionary even if some lines are commented out."""
    os.chdir(tmp_path)
    prefixfile_content = (
        "prefixes:\n"
        "#   dc: http://purl.org/dc/elements/1.1/\n"
        "    dcterms: http://purl.org/dc/terms/\n"
    )
    Path(PREFIXFILE_NAME).write_text(prefixfile_content)
    expected = {"prefixes": {"dcterms": "http://purl.org/dc/terms/"}}
    assert get_prefixes() == expected


def test_exit_if_prefixfile_has_bad_yaml(tmp_path):
    """Raise exception if config file has bad YAML."""
    os.chdir(tmp_path)
    prefixfile_content = "DELIBE\nRATELY BAD: -: ^^YAML CONTENT^^\n"
    Path(PREFIXFILE_NAME).write_text(prefixfile_content)
    with pytest.raises(SystemExit):
        get_prefixes()
