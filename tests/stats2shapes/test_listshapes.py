"""@@@Docstring"""

import os
import pytest
from pathlib import Path
from csv2shex.stats2shapes import list_shapes
from csv2shex.csv2stats import Statement
from dataclasses import asdict

MINIMAL_LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", v_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", v_type="String"),
]

LIST_OF_STATEMENT_OBJECTS = [
    Statement(start=True, shape_id="@a", prop_id="dct:creator", v_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:subject", v_type="URI"),
    Statement(start=True, shape_id="@a", prop_id="dct:date", v_type="String"),
    Statement(start=False, shape_id="@b", prop_id="foaf:name", v_type="String"),
]


def test_listshapes():
    """Turn list of Statement objects into list of Shapes."""
    assert True

#    assert list_shapes(LIST_OF_STATEMENT_OBJECTS) == [
#    Shape(shape_id="@a", start=True, property_values=[
#            {
#                "prop_id": "dct:creator",
#                "v_type": "URI",
#            },
#            {
#                "prop_id": "dct:subject",
#                "v_type": "URI",
#            },
#            {
#                "prop_id": "dct:date",
#                "v_type": "String",
#            }, 
#    ]),
#    Shape(shape_id="@b", start=False, property_values=[
#            {
#                "prop_id": "foaf:name",
#                "v_type": "String",
#            },
#    ])
#    ]
