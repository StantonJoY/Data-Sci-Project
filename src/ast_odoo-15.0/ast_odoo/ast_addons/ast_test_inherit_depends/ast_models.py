Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=23,
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=8,
            end_col_offset=57,
            name='PublishedFoo',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=19,
                    end_lineno=6,
                    end_col_offset=31,
                    value=Name(lineno=6, col_offset=19, end_lineno=6, end_col_offset=25, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=30,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=30, value='test_new_api.foo', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=57,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=8,
                        col_offset=15,
                        end_lineno=8,
                        end_col_offset=57,
                        elts=[
                            Constant(lineno=8, col_offset=16, end_lineno=8, end_col_offset=34, value='test_new_api.foo', kind=None),
                            Constant(lineno=8, col_offset=36, end_lineno=8, end_col_offset=56, value='test_inherit.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
