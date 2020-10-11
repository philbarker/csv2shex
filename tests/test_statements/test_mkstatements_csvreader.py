"""Read CSV file and return list of rows as Python dictionaries."""

import os
from pathlib import Path
from csv2shex.mkstatements import csvreader


def test_csvreader_with_simple_csvfile(tmp_path):
    """Simple CSV with three columns."""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text(
        (
            "shape_id,prop_id,value_node_type\n"
            ":a,dct:creator,URI\n"
            ":a,dct:subject,URI\n"
            ":a,dct:date,String\n"
        )
    )
    expected_output = [
        {"shape_id": ":a", "prop_id": "dct:creator", "value_node_type": "URI"},
        {"shape_id": ":a", "prop_id": "dct:subject", "value_node_type": "URI"},
        {"shape_id": ":a", "prop_id": "dct:date", "value_node_type": "String"},
    ]
    assert csvreader(csvfile) == expected_output


def test_csvreader_with_complete_csvfile(tmp_path):
    """Simple CSV with all columns."""
    os.chdir(tmp_path)
    csvfile = Path(tmp_path).joinpath("some.csv")
    csvfile.write_text(
        (
            "shape_id,shape_label,prop_id,prop_label,mand,repeat,value_node_type,"
            "value_datatype,value_constraint,constraint_type,shape_ref,annot\n"
            "@a,Book,dct:creator,Creator,Y,N,URI,,,,@b,Typically the author.\n"
            "@a,Book,dct:date,Date,Y,N,String,xsd:string,(\d+/\d+/\d+),Regex,,\n"
            "@b,Person,foaf:name,Name,Y,N,String,xsd:string,,,,\n"
        )
    )
    expected_output = [
        {
            "shape_id": "@a",
            "shape_label": "Book",
            "prop_id": "dct:creator",
            "prop_label": "Creator",
            "mand": "Y",
            "repeat": "N",
            "value_node_type": "URI",
            "value_datatype": "",
            "value_constraint": "",
            "constraint_type": "",
            "shape_ref": "@b",
            "annot": "Typically the author.",
        },
        {
            "shape_id": "@a",
            "shape_label": "Book",
            "prop_id": "dct:date",
            "prop_label": "Date",
            "mand": "Y",
            "repeat": "N",
            "value_node_type": "String",
            "value_datatype": "xsd:string",
            "value_constraint": "(\d+/\d+/\d+)",
            "constraint_type": "Regex",
            "shape_ref": "",
            "annot": "",
        },
        {
            "shape_id": "@b",
            "shape_label": "Person",
            "prop_id": "foaf:name",
            "prop_label": "Name",
            "mand": "Y",
            "repeat": "N",
            "value_node_type": "String",
            "value_datatype": "xsd:string",
            "value_constraint": "",
            "constraint_type": "",
            "shape_ref": "",
            "annot": "",
        },
    ]
    assert type(csvreader(csvfile)) == list
    assert type(expected_output) == list
    assert len(csvreader(csvfile)) == 3
    assert len(expected_output) == 3
    assert type(csvreader(csvfile)[0]) == dict
    assert csvreader(csvfile) == expected_output
