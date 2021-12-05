Module(
    body=[
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=4,
            col_offset=0,
            end_lineno=5,
            end_col_offset=34,
            name='A',
            bases=[
                Attribute(
                    lineno=4,
                    col_offset=8,
                    end_lineno=4,
                    end_col_offset=20,
                    value=Name(lineno=4, col_offset=8, end_lineno=4, end_col_offset=14, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=5,
                    col_offset=4,
                    end_lineno=5,
                    end_col_offset=34,
                    targets=[
                        Name(lineno=5, col_offset=4, end_lineno=5, end_col_offset=9, id='_name', ctx=Store()),
                        Name(lineno=5, col_offset=12, end_lineno=5, end_col_offset=24, id='_description', ctx=Store()),
                    ],
                    value=Constant(lineno=5, col_offset=27, end_lineno=5, end_col_offset=34, value='tab.a', kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=9,
            end_col_offset=34,
            name='B',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=8,
                    end_lineno=8,
                    end_col_offset=20,
                    value=Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=14, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=34,
                    targets=[
                        Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store()),
                        Name(lineno=9, col_offset=12, end_lineno=9, end_col_offset=24, id='_description', ctx=Store()),
                    ],
                    value=Constant(lineno=9, col_offset=27, end_lineno=9, end_col_offset=34, value='tab.b', kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
