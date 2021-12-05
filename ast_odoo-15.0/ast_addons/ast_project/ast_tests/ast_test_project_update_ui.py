Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=39,
            module='odoo.tests',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=9,
            end_col_offset=69,
            name='TestProjectUpdateUi',
            bases=[Name(lineno=6, col_offset=26, end_lineno=6, end_col_offset=34, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=8,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=69,
                    name='test_01_project_tour',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=8, col_offset=29, end_lineno=8, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=69,
                            value=Call(
                                lineno=9,
                                col_offset=8,
                                end_lineno=9,
                                end_col_offset=69,
                                func=Attribute(
                                    lineno=9,
                                    col_offset=8,
                                    end_lineno=9,
                                    end_col_offset=23,
                                    value=Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=9, col_offset=24, end_lineno=9, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=9, col_offset=32, end_lineno=9, end_col_offset=53, value='project_update_tour', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=9,
                                        col_offset=55,
                                        end_lineno=9,
                                        end_col_offset=68,
                                        arg='login',
                                        value=Constant(lineno=9, col_offset=61, end_lineno=9, end_col_offset=68, value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    lineno=5,
                    col_offset=1,
                    end_lineno=5,
                    end_col_offset=38,
                    func=Name(lineno=5, col_offset=1, end_lineno=5, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=5, col_offset=8, end_lineno=5, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=5, col_offset=24, end_lineno=5, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
