"""Config constants. Write and read configuration file."""

import os
from pathlib import Path
import ruamel.yaml as yaml
from .exceptions import ConfigError

CSV_ELEMENTS = """\
shape_elements:
- shapeID
- shapeLabel
- shapeClosed
- start

statement_elements:
- propertyID
- propertyLabel
- mandatory
- repeatable
- valueNodeType
- valueDataType
- valueConstraint
- valueConstraintType
- valueShape
- note

uri_elements:
- shapeID
- propertyID
- valueShape
"""

DEFAULT_CONFIGFILE_NAME = ".csv2rc"

CONFIG_DEFAULTS = """\
prefixes:
    : http://example.org/
    dc: http://purl.org/dc/elements/1.1/
    dcat: http://www.w3.org/ns/dcat
    dct: http://purl.org/dc/terms/
    dcterms: http://purl.org/dc/terms/
    foaf: http://xmlns.com/foaf/0.1/
    rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
    rdfs: http://www.w3.org/2000/01/rdf-schema#
    skos: http://www.w3.org/2004/02/skos/core#
    skosxl: http://www.w3.org/2008/05/skos-xl#
    sx: http://www.w3.org/ns/shex
    xsd: http://www.w3.org/2001/XMLSchema#
    wd: https://www.wikidata.org/wiki/
    wdt: http://www.wikidata.org/prop/direct/

valueNodeType:
- URI
- BNode
- Literal
- Nonliteral

valueConstraintType:
- Datatype
- UriStem
- UriPicklist
- LitPicklist
- LangTag
- LangTagPicklist
- Regex
"""

elements = yaml.safe_load(CSV_ELEMENTS)
SHAPE_ELEMENTS = elements["shape_elements"]
STATEMENT_ELEMENTS = elements["statement_elements"]
URI_ELEMENTS = elements["uri_elements"]


def write_starter_configfile(
    basedir=None,
    default_configfile_name=DEFAULT_CONFIGFILE_NAME,
    config_defaults=CONFIG_DEFAULTS,
):
    """Write initial config file, by default to CWD, or exit if already exists."""
    if not basedir:
        basedir = Path.cwd()
    configfile_pathname = Path(basedir) / default_configfile_name
    if os.path.exists(configfile_pathname):
        raise ConfigError(
            f"Found existing {str(configfile_pathname)} - delete to re-generate."
        )
    with open(configfile_pathname, "w", encoding="utf-8") as outfile:
        outfile.write(config_defaults)
        print(f"Wrote config defaults (for editing) to: {str(configfile_pathname)}")


def get_config_settings(
    rootdir_path=None,
    default_configfile_name=DEFAULT_CONFIGFILE_NAME,
    config_defaults=CONFIG_DEFAULTS,
    verbose=False,
):
    """Returns config dict from config file, if found, or from built-in defaults."""
    if not rootdir_path:
        rootdir_path = Path.cwd()
    configfile_pathname = Path(rootdir_path) / default_configfile_name

    try:
        configfile_contents = Path(configfile_pathname).read_text()
        if verbose:
            print(f"Reading config file {repr(configfile_pathname)}.")
        return yaml.safe_load(configfile_contents)
    except FileNotFoundError:
        if verbose:
            print(
                f"Config file {repr(configfile_pathname)} not found - using defaults."
            )
        return yaml.safe_load(config_defaults)
    except (yaml.YAMLError, yaml.scanner.ScannerError):
        print(
            f"Ignoring badly formed config file {repr(default_configfile_name)}"
            " - using defaults."
        )
        return yaml.safe_load(config_defaults)
