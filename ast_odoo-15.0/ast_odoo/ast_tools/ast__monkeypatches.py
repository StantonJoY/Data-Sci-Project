Module(
    body=[
        Try(
            lineno=1,
            col_offset=0,
            end_lineno=18,
            end_col_offset=32,
            body=[
                ImportFrom(
                    lineno=2,
                    col_offset=4,
                    end_lineno=2,
                    end_col_offset=25,
                    module='xlrd',
                    names=[alias(name='xlsx', asname=None)],
                    level=0,
                ),
            ],
            handlers=[
                ExceptHandler(
                    lineno=3,
                    col_offset=0,
                    end_lineno=4,
                    end_col_offset=8,
                    type=Name(lineno=3, col_offset=7, end_lineno=3, end_col_offset=18, id='ImportError', ctx=Load()),
                    name=None,
                    body=[Pass(lineno=4, col_offset=4, end_lineno=4, end_col_offset=8)],
                ),
            ],
            orelse=[
                ImportFrom(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=26,
                    module='lxml',
                    names=[alias(name='etree', asname=None)],
                    level=0,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=19,
                    targets=[
                        Attribute(
                            lineno=16,
                            col_offset=4,
                            end_lineno=16,
                            end_col_offset=11,
                            value=Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=8, id='xlsx', ctx=Load()),
                            attr='ET',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(lineno=16, col_offset=14, end_lineno=16, end_col_offset=19, id='etree', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=32,
                    targets=[
                        Attribute(
                            lineno=17,
                            col_offset=4,
                            end_lineno=17,
                            end_col_offset=25,
                            value=Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=8, id='xlsx', ctx=Load()),
                            attr='ET_has_iterparse',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(lineno=17, col_offset=28, end_lineno=17, end_col_offset=32, value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=32,
                    targets=[
                        Attribute(
                            lineno=18,
                            col_offset=4,
                            end_lineno=18,
                            end_col_offset=25,
                            value=Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=8, id='xlsx', ctx=Load()),
                            attr='Element_has_iter',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(lineno=18, col_offset=28, end_lineno=18, end_col_offset=32, value=True, kind=None),
                    type_comment=None,
                ),
            ],
            finalbody=[],
        ),
    ],
    type_ignores=[],
)