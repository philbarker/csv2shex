"""Writes starter configuration file (YAML format)."""

import os
import pytest
from pathlib import Path
from csv2shex.config import (
    write_starter_configfile,
    CONFIG_DEFAULTS,
    CONFIGFILE_NAME,
)


def test_write_starter_configfile_and_read_back(tmp_path):
    """Write CONFIG_DEFAULTS to text file CONFIGFILE_NAME and read back as text."""
    os.chdir(tmp_path)
    write_starter_configfile()
    assert open(CONFIGFILE_NAME).read() == CONFIG_DEFAULTS


def test_write_starter_configfile_but_not_if_already_exists(tmp_path):
    """Exits with error if CONFIGFILE_NAME already exists."""
    os.chdir(tmp_path)
    Path(CONFIGFILE_NAME).write_text("Config stuff")
    with pytest.raises(SystemExit):
        write_starter_configfile()


def test_write_starter_configfile_specifying_basedir(tmp_path):
    """Write CONFIG_DEFAULTS to text file CONFIGFILE_NAME specifying basedir."""
    os.chdir(tmp_path)
    abc = Path.cwd() / "some_basedir"
    abc.mkdir()
    os.chdir(abc)
    write_starter_configfile(basedir=abc)
    expected_configfile_pathname = Path(abc) / CONFIGFILE_NAME
    assert open(expected_configfile_pathname).read() == CONFIG_DEFAULTS