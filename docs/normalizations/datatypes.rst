RDF datatypes
^^^^^^^^^^^^^

In RDF, the datatype of a literal can optionally be specified with a datatype URI. If a constraint type of `Datatype` is provided, csv2shex normalizes statement elements as follows:

- Csv2shex checks that the value provided for 'constraint_value' is a URI or prefixed URI (as it must be, according to the rules of RDF). If it is not, the constraint value is set to None.
- Where no value type is provided, csv2shex assigns the value Literal.
- If a constraint type of Datatype is specified for anything other than a value of type Literal (which does not make sense in terms of RDF), csv2shex will leave it to the user to spot and correct this error.


.. csv-table:: 
   :file: ../normalizations/datatypes.csv
   :header-rows: 1

This is interpreted as::

    DCAP
        Shape
            shapeID: @default
            start: True
            Statement
                propertyID: :color
                value_type: Literal
                constraint_value: xsd:string
                constraint_type: Datatype
            Statement
                propertyID: :color
                value_type: Literal
                constraint_value: None
                constraint_type: Datatype
