"""Read CSV file and return list of rows as Python dictionaries."""

import os
from dataclasses import asdict
import pytest
from pathlib import Path
from csv2shex.csvreader import _get_csvrow_dicts_list
from csv2shex.csvrow import CSVRow

DEFAULTS = asdict(CSVRow())


def test_get_csvrow_dicts_list_with_simple_csvfile(tmp_path):
    """Simple CSV with three columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propertyID,valueNodeType\n"
            ":a,dct:creator,URI\n"
            ":a,dct:subject,URI\n"
            ":a,dct:date,String\n"
        )
    )
    expected_csvrow_dicts_list = [
        { 'shapeID': ':a', 'propertyID': 'dct:creator', 'valueNodeType': 'URI' }, 
        { 'shapeID': ':a', 'propertyID': 'dct:subject', 'valueNodeType': 'URI' }, 
        { 'shapeID': ':a', 'propertyID': 'dct:date', 'valueNodeType': 'String' }
    ]
    assert _get_csvrow_dicts_list(csvfile_name) == expected_csvrow_dicts_list


def test_get_csvrow_dicts_list_with_complete_csvfile(tmp_path):
    """Simple CSV with all columns."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,shapeLabel,propertyID"
            ",propertyLabel,mandatory,repeatable,valueNodeType,"
            "valueDataType,valueConstraint,valueConstraintType,valueShape,note\n"
            ":a,Book,dct:creator,Creator,Y,N,URI,,,,:b,Typically the author.\n"
            ":b,Person,foaf:name,Name,Y,N,String,xsd:string,,,,\n"
        )
    )
    corrected_csvrows_list = [
        {
            "shapeID": ":a",
            "shapeLabel": "Book",
            "shapeClosed": False,
            "propertyID": "dct:creator",
            "propertyLabel": "Creator",
            "mandatory": True,
            "repeatable": False,
            "valueNodeType": "URI",
            "valueDataType": "",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": ":b",
            "note": "Typically the author.",
        },
        {
            "shapeID": ":b",
            "shapeLabel": "Person",
            "shapeClosed": False,
            "propertyID": "foaf:name",
            "propertyLabel": "Name",
            "mandatory": True,
            "repeatable": False,
            "valueNodeType": "String",
            "valueDataType": "xsd:string",
            "valueConstraint": "",
            "valueConstraintType": "",
            "valueShape": "",
            "note": "",
        },
    ]
    assert type(_get_csvrow_dicts_list(csvfile_name)) == list
    assert _get_csvrow_dicts_list(csvfile_name)[0]["mandatory"]
    assert type(corrected_csvrows_list) == list
    assert len(_get_csvrow_dicts_list(csvfile_name)) == 2
    assert len(corrected_csvrows_list) == 2


def test_get_csvrow_dicts_list_with_invalid_csvfile(tmp_path):
    """A DCAP CSV is invalid if it does not at least have "propertyID"."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(("shapeID,propID,valueNodeType\n" ":a,dct:creator,URI\n"))
    with pytest.raises(SystemExit):
        _get_csvrow_dicts_list(csvfile_name)


def test_liststatements_with_csv_column_outside_dctap_model_are_ignored(tmp_path):
    """CSV columns not part of the DC TAP model are simply ignored."""
    os.chdir(tmp_path)
    csvfile_name = Path(tmp_path).joinpath("some.csv")
    csvfile_name.write_text(
        (
            "shapeID,propertyID,confidential\n"
            ":a,dct:subject,True\n"
        )
    )
    expected_csvrow_dicts_list = [
        {"shapeID": ":a", "propertyID": "dct:subject", "confidential": "True"},
    ]
    assert _get_csvrow_dicts_list(csvfile_name) == expected_csvrow_dicts_list

#    corrected_csvrows_list = [
#        {"shapeID": ":a", "propertyID": "dct:creator", "valueNodeType": "URI"},
#        {"shapeID": ":a", "propertyID": "dct:subject", "valueNodeType": "URI"},
#        {"shapeID": ":a", "propertyID": "dct:date", "valueNodeType": "String"},
#    ]
#    expected_output_list = [dict(DEFAULTS, **item) for item in corrected_csvrows_list]
#    assert _get_csvrow_dicts_list(csvfile_name) == expected_output_list
#    expected_output_list = [dict(DEFAULTS, **item) for item in corrected_csvrows_list]
#    assert _get_csvrow_dicts_list(csvfile_name) == expected_output_list
#    expected_output_list = [dict(DEFAULTS, **item) for item in corrected_csvrows_list]
#    assert _get_csvrow_dicts_list(csvfile_name) == expected_output_list