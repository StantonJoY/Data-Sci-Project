Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ResCountry',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.country', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street_format', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="Format to use for streets belonging to this country.\n\nYou can use the python-style string pattern with all the fields of the street (for example, use '%(street_name)s, %(street_number)s' if you want to display the street name, followed by a comma and the house number)\n%(street_name)s: the name of the street\n%(street_number)s: the house number\n%(street_number2)s: the door number", kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='%(street_number)s/%(street_number2)s %(street_name)s', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
