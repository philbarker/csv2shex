"""Read DCAP/CSV (expand prefixes?). Write and read config file."""

import csv
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import List
import ruamel.yaml as yaml
from .config import CSV_MODEL
from .csvrow import CSVRow
from .exceptions import CsvError

CSV_MODEL_DICT = yaml.safe_load(CSV_MODEL)


def csvreader(csvfile):
    """Read CSV file and return list of dicts, one dict per CSV row."""
    csv_dictreader_obj = csv.DictReader(
        Path(csvfile).open(newline="", encoding="utf-8-sig")
    )
    csvrow_dicts_list = list(csv_dictreader_obj)
    if "propertyID" not in list(csvrow_dicts_list[0].keys()):
        raise CsvError("Valid DCAP CSV must have a 'propertyID' column.")
    corrected_csvrow_dicts_list = _get_corrected_csvrows_list(csvrow_dicts_list)
    return corrected_csvrow_dicts_list


def _get_corrected_csvrows_list(csvrow_dicts_list=None, csv_model_dict=CSV_MODEL_DICT):
    """Turn list of dicts into list of CSVRow objects."""
    corrected_csvrow_dicts_list = []
    shapeids_list = []
    first_shape_encountered = True
    keys = csv_model_dict["shape_elements"] + csv_model_dict["cvpair_elements"]
    keys.remove("shapeID")
    for row in csvrow_dicts_list:
        if not row.get("propertyID") and row.get("shapeID"):
            shapeids_list.append(row["shapeID"])
            continue

        stat = CSVRow()

        if row.get("shapeID"):
            stat.shapeID = row["shapeID"]
        else:
            if shapeids_list:
                stat.shapeID = shapeids_list[-1]
            elif not shapeids_list:
                stat.shapeID = ":default"
        if stat.shapeID not in shapeids_list:
            shapeids_list.append(stat.shapeID)
        if first_shape_encountered:
            first_shape_encountered = False

        for key in keys:
            if key in row:
                setattr(stat, key, row[key])

        stat.normalize()
        stat.validate()
        corrected_csvrow_dicts_list.append(asdict(stat))
    return corrected_csvrow_dicts_list


def get_csvshape_dicts_list(csvrow_dicts_list, csv_model=CSV_MODEL) -> List[dict]:
    """Get list of csvshape dicts from list of csvrow dicts."""

    aggregator_ddict = defaultdict(dict)
    is_first_csvrow_encountered = True
    pvdict = dict()
    csv_model_dict = yaml.safe_load(csv_model)

    for csvrow_dict in csvrow_dicts_list:
        if csvrow_dict["shapeID"] not in aggregator_ddict.keys():
            shap_dict = dict()
            shap_dict["shapeID"] = csvrow_dict["shapeID"]
            shap_dict["shapeLabel"] = csvrow_dict["shapeLabel"]
            shap_dict["shapeClosed"] = csvrow_dict["shapeClosed"]
            shap_dict["start"] = bool(is_first_csvrow_encountered)
            shap_dict["pvdicts_list"] = list()
            aggregator_ddict[shap_dict["shapeID"]] = shap_dict
            is_first_csvrow_encountered = False

        for key in csv_model_dict["cvpair_elements"]:
            pvdict[key] = csvrow_dict[key]

        aggregator_ddict[shap_dict["shapeID"]]["pvdicts_list"].append(pvdict.copy())
        pvdict.clear()

    csvshape_dicts_list = []
    for key in aggregator_ddict.keys():
        csvshape_dict = aggregator_ddict[key]
        csvshape_dicts_list.append(csvshape_dict)

    return csvshape_dicts_list
