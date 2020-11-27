"""Read CSV file and return list of rows as Python dictionaries."""

import pytest
from csv2shex.csvreader import _get_csvshapes
from csv2shex.csvshape import CSVShape, CSVTripleConstraint


def test_get_csvshape_list_minimal_csv():
    """Minimal CSV with three columns, one triple constraint each."""
    rows = [
        {
            "shapeID": ":book",
            "propertyID": "dc:creator",
            "valueConstraint": "",
            "valueShape": ":author",
        },
        {
            "shapeID": ":author",
            "propertyID": "foaf:name",
            "valueConstraint": "",
            "valueShape": "",
        },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":book",
            start=True,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="dc:creator", valueConstraint="", valueShape=":author"
                ),
            ],
        ),
        CSVShape(
            shapeID=":author",
            start=False,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="foaf:name", valueConstraint="", valueShape=""
                )
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes


def test_get_csvshape_list_longer_minimal_csv():
    """Slightly longer minimal CSV with three columns."""
    rows = [
        {
            "shapeID": ":book",
            "propertyID": "dc:creator",
            "valueConstraint": "",
            "valueShape": ":author",
        },
        {
            "shapeID": "",
            "propertyID": "dc:type",
            "valueConstraint": "so:Book",
            "valueShape": "",
        },
        {
            "shapeID": ":author",
            "propertyID": "foaf:name",
            "valueConstraint": "",
            "valueShape": "",
        },
    ]
    expected_shapes = [
        CSVShape(
            shapeID=":book",
            start=True,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="dc:creator", valueConstraint="", valueShape=":author"
                ),
                CSVTripleConstraint(
                    propertyID="dc:type", valueConstraint="so:Book", valueShape=""
                ),
            ],
        ),
        CSVShape(
            shapeID=":author",
            start=False,
            tc_list=[
                CSVTripleConstraint(
                    propertyID="foaf:name", valueConstraint="", valueShape=""
                )
            ],
        ),
    ]
    assert _get_csvshapes(rows) == expected_shapes