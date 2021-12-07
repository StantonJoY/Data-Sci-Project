Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=9,
            end_col_offset=27,
            name='Partner',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=14,
                    end_lineno=7,
                    end_col_offset=26,
                    value=Name(lineno=7, col_offset=14, end_lineno=7, end_col_offset=20, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=28,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=28, value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=27,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=20, id='_mailing_enabled', ctx=Store())],
                    value=Constant(lineno=9, col_offset=23, end_lineno=9, end_col_offset=27, value=True, kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
