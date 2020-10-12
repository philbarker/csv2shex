"""Turn list of Statements into list of Shapes."""

from csv2shex.mkshapes import list_shapes, Shape
from csv2shex.mkstatements import Statement

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"),
    Statement(start=True, shapeID="@a", prop_id="dct:subject", value_node_type="URI"),
    Statement(start=True, shapeID="@a", prop_id="dct:date", value_node_type="String"),
    Statement(
        start=False, shapeID="@b", prop_id="foaf:name", value_node_type="String"
    ),
]


def test_listshapes_one_shape():
    """Turn list of Statement objects into list with one Shape."""
    as_input = [
        Statement(
            start=True, shapeID="@a", prop_id="dct:creator", value_node_type="URI"
        ),
        Statement(
            start=True, shapeID="@a", prop_id="dct:date", value_node_type="String"
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID="@a",
            shape_label=None,
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_node_type": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_node_type": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
            ],
        )
    ]


def test_listshapes_one_shape_and_shape_label():
    """One Shape with shape label."""
    as_input = [
        Statement(
            start=True,
            shapeID="@a",
            shape_label="Author",
            prop_id="dct:creator",
            value_node_type="URI",
        ),
        Statement(
            start=True,
            shapeID="@a",
            shape_label="Author",
            prop_id="dct:date",
            value_node_type="String",
        ),
    ]
    assert list_shapes(as_input) == [
        Shape(
            start=True,
            shapeID="@a",
            shape_label="Author",
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_node_type": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_node_type": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
            ],
        )
    ]


def test_listshapes_two_shapes():
    """Turn list of Statement objects into list with two Shapes."""
    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
        Shape(
            start=True,
            shapeID="@a",
            shape_statements=[
                {
                    "prop_id": "dct:creator",
                    "value_node_type": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "prop_id": "dct:subject",
                    "value_node_type": "URI",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
                {
                    "prop_id": "dct:date",
                    "value_node_type": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                },
            ],
        ),
        Shape(
            start=False,
            shapeID="@b",
            shape_statements=[
                {
                    "prop_id": "foaf:name",
                    "value_node_type": "String",
                    "value_datatype": None,
                    "prop_label": None,
                    "mand": False,
                    "repeat": False,
                    "value_constraint": None,
                    "value_constraint_type": None,
                    "value_shape": None,
                    "note": None,
                }
            ],
        ),
    ]
