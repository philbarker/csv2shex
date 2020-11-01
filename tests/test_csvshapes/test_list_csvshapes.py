"""Turn list of CSVRows into list of CSVShapes."""

import pytest
from csv2shex.csvshapes import pprint_schema, list_csvshapeobjs, CSVShape
from csv2shex.csvrows import CSVRow


def test_list_csvshapeobjs_two_shapes():
    """Turn list of CSVRow objects into list with two CSVShapes."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
        CSVRow(shapeID=":b", propertyID="foaf:name"),
    ]

    expected_csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            shapeClosed=False,
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
                {
                    "propertyID": "dct:date",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                },
            ],
        ),
        CSVShape(
            start=False,
            shapeID=":b",
            shapeLabel=None,
            statement_csvrows_list=[
                {
                    "propertyID": "foaf:name",
                    "mandatory": False,
                    "note": None,
                    "propertyLabel": None,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueDataType": None,
                    "valueNodeType": None,
                    "valueShape": None,
                }
            ],
        ),
    ]
    assert len(list_csvshapeobjs(csvrows_list)) == len(expected_csvshapes_list)
    assert list_csvshapeobjs(csvrows_list)[0].statement_csvrows_list == expected_csvshapes_list[0].statement_csvrows_list
    assert list_csvshapeobjs(csvrows_list) == expected_csvshapes_list


def test_list_csvshapeobjs_one_shape():
    """Turn list of CSVRow objects into list with one CSVShape."""
    csvrows_list = [
        CSVRow(shapeID=":a", propertyID="dct:creator"),
        CSVRow(shapeID=":a", propertyID="dct:date"),
    ]

    expected_csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel=None,
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        )
    ]
    assert list_csvshapeobjs(csvrows_list) == expected_csvshapes_list


def test_list_csvshapeobjs_one_shape_and_shapeLabel():
    """One CSVShape with shape label."""
    csvrows_list = [
        CSVRow(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:creator",
            valueNodeType="URI",
        ),
        CSVRow(
            shapeID=":a",
            shapeLabel="Author",
            propertyID="dct:date",
            valueNodeType="String",
        ),
    ]

    csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel="Author",
            statement_csvrows_list=[
                {
                    "propertyID": "dct:creator",
                    "valueNodeType": "URI",
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "dct:date",
                    "valueNodeType": "String",
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        )
    ]
    assert list_csvshapeobjs(csvrows_list) == csvshapes_list 


def test_list_csvshapeobjs_two_shapes_assign_start_to_first():
    """First shape created is marked as the 'start' shape."""
    csvrows_list = [
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop1"),
        CSVRow(shapeID=":a", shapeLabel="A CSVShape", propertyID=":prop2"),
        CSVRow(shapeID=":b", shapeLabel="B CSVShape", propertyID=":prop3"),
    ]
    csvshapes_list = [
        CSVShape(
            start=True,
            shapeID=":a",
            shapeLabel="A CSVShape",
            statement_csvrows_list=[
                {
                    "propertyID": ":prop1",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": ":prop2",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
            ],
        ),
        CSVShape(
            start=False,
            shapeID=":b",
            shapeLabel="B CSVShape",
            statement_csvrows_list=[
                {
                    "propertyID": ":prop3",
                    "valueNodeType": None,
                    "valueDataType": None,
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                }
            ],
        ),
    ]
    #from pprint import pprint
    #pprint(list_csvshapeobjs(csvrows_list))
    #print("")
    #pprint(csvshapes_list)
    #assert False
    assert list_csvshapeobjs(csvrows_list) == csvshapes_list
"""Turn list of CSVRows into list of CSVShapes (for ShEx example)."""

import pytest
from csv2shex.csvshapes import list_csvshapeobjs, CSVShape
from csv2shex.csvrows import CSVRow
from pprint import pprint


def test_listshapes_one_shape_for_shex_example():
    """Turn list of CSVRow objects into list with one CSVShape."""
    csvrows_list = [
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/title",
            mandatory=True,
            repeatable=False,
            valueNodeType="literal",
            valueDataType=None,
            valueConstraint=None,
            valueConstraintType=None,
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/description",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType="http://www.w3.org/2001/XMLSchema#string",
            valueConstraint=None,
            valueConstraintType=None,
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/subject",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType=None,
            valueConstraint="http://lod.nal.usda.gov/nalt/",
            valueConstraintType="IriStem",
            valueShape=None,
        ),
        CSVRow(
            shapeID="http://example.org/myshape",
            propertyID="http://purl.org/dc/terms/creator",
            mandatory=False,
            repeatable=False,
            valueNodeType=None,
            valueDataType=None,
            valueConstraint=None,
            valueConstraintType=None,
            valueShape="http://example.org/mycreator",
        ),
    ]

    one_shape_with_csvrows_list = [
        CSVShape(
            start=True,
            shapeID="http://example.org/myshape",
            shapeLabel=None,
            statement_csvrows_list=[
                {
                    "propertyID": "http://purl.org/dc/terms/title",
                    "propertyLabel": None,
                    "mandatory": True,
                    "repeatable": False,
                    "valueNodeType": "literal",
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/description",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": "http://www.w3.org/2001/XMLSchema#string",
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/subject",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": "http://lod.nal.usda.gov/nalt/",
                    "valueConstraintType": "IriStem",
                    "valueShape": None,
                    "note": None,
                },
                {
                    "propertyID": "http://purl.org/dc/terms/creator",
                    "propertyLabel": None,
                    "mandatory": False,
                    "repeatable": False,
                    "valueNodeType": None,
                    "valueDataType": None,
                    "valueConstraint": None,
                    "valueConstraintType": None,
                    "valueShape": "http://example.org/mycreator",
                    "note": None,
                },
            ],
        )
    ]
    assert list_csvshapeobjs(csvrows_list) == one_shape_with_csvrows_list
