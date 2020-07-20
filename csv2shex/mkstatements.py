"""Class for Python objects derived from CSV files."""


import csv
from dataclasses import dataclass
from pathlib import Path
from .constants import SHAPE_KEYS, STATEMENT_KEYS

# pylint: disable=no-self-use,too-many-branches,too-many-instance-attributes
# => self-use: for now...
# => too-many-branches: a matter of taste?
# => too-many-instance-attributes: disagree!


@dataclass
class Statement:
    """Holds state and self-validation methods for a statement."""

    start: bool = False
    shape_id: str = None
    shape_label: str = None
    prop_id: str = None
    prop_label: str = None
    mand: str = None
    repeat: str = None
    value_type: str = None
    value_datatype: str = None
    constraint_value: str = None
    constraint_type: str = None
    shape_ref: str = None
    annot: str = None

    def is_valid(self):
        """Returns True if Statement instance is valid."""
        # self._valid_uristem()
        # self._property_id_is_mandatory()
        # self._value_type_is_valid_type()
        return True

    def _is_uristem_used_correctly(self):
        """Returns True if constraint type URI Stem used correctly."""
        if self.constraint_type == "URIStem":
            if self.constraint_value:
                print(
                    f"Constraint type {self.constraint_type} "
                    "used with constraint value - ok."
                )
            else:
                print(
                    f"Warning: Constraint type {self.constraint_type} "
                    "requires corresponding constraint value."
                )


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    rows_odict = csv.DictReader(Path(csvfile).open(newline="", encoding="utf-8-sig"))
    rows = [dict(r) for r in rows_odict]
    return rows


def list_statements(csvrow_list=None):
    """Return list of Statement objects from list of dicts ("CSV rows")."""
    statements_list = []
    shape_ids = []
    first_shape_encountered = True
    keys = SHAPE_KEYS + STATEMENT_KEYS
    keys.remove("shape_id")
    for row in csvrow_list:
        if not row.get("prop_id") and row.get("shape_id"):
            shape_ids.append(row["shape_id"])
            continue

        stat = Statement()

        if row.get("shape_id"):
            stat.shape_id = row["shape_id"]
        else:
            if shape_ids:
                stat.shape_id = shape_ids[-1]
            elif not shape_ids:
                stat.shape_id = "@default"
        if stat.shape_id not in shape_ids:
            shape_ids.append(stat.shape_id)
        if first_shape_encountered:
            first_shape = stat.shape_id
            first_shape_encountered = False
        if stat.shape_id == first_shape:
            stat.start = True

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        statements_list.append(stat)
    return statements_list
