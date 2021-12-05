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
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=16,
            end_col_offset=27,
            name='Http',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=11,
                    end_lineno=8,
                    end_col_offset=31,
                    value=Name(lineno=8, col_offset=11, end_lineno=8, end_col_offset=17, id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=24,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=9, col_offset=15, end_lineno=9, end_col_offset=24, value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=27,
                    name='session_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=21, end_lineno=11, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=59,
                            value=Constant(lineno=12, col_offset=8, end_lineno=12, end_col_offset=59, value=' Add information about iap enrich to perform ', kind=None),
                        ),
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=55,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=20, id='session_info', ctx=Store())],
                            value=Call(
                                lineno=13,
                                col_offset=23,
                                end_lineno=13,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=23,
                                    end_lineno=13,
                                    end_col_offset=53,
                                    value=Call(
                                        lineno=13,
                                        col_offset=23,
                                        end_lineno=13,
                                        end_col_offset=40,
                                        func=Name(lineno=13, col_offset=23, end_lineno=13, end_col_offset=28, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=13, col_offset=29, end_lineno=13, end_col_offset=33, id='Http', ctx=Load()),
                                            Name(lineno=13, col_offset=35, end_lineno=13, end_col_offset=39, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=14,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=101,
                            test=Call(
                                lineno=14,
                                col_offset=11,
                                end_lineno=14,
                                end_col_offset=39,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=11,
                                    end_lineno=14,
                                    end_col_offset=27,
                                    value=Name(lineno=14, col_offset=11, end_lineno=14, end_col_offset=23, id='session_info', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=14, col_offset=28, end_lineno=14, end_col_offset=38, value='is_admin', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    lineno=15,
                                    col_offset=12,
                                    end_lineno=15,
                                    end_col_offset=101,
                                    targets=[
                                        Subscript(
                                            lineno=15,
                                            col_offset=12,
                                            end_lineno=15,
                                            end_col_offset=46,
                                            value=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=24, id='session_info', ctx=Load()),
                                            slice=Constant(lineno=15, col_offset=25, end_lineno=15, end_col_offset=45, value='iap_company_enrich', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        lineno=15,
                                        col_offset=49,
                                        end_lineno=15,
                                        end_col_offset=101,
                                        op=Not(),
                                        operand=Attribute(
                                            lineno=15,
                                            col_offset=53,
                                            end_lineno=15,
                                            end_col_offset=101,
                                            value=Attribute(
                                                lineno=15,
                                                col_offset=53,
                                                end_lineno=15,
                                                end_col_offset=80,
                                                value=Attribute(
                                                    lineno=15,
                                                    col_offset=53,
                                                    end_lineno=15,
                                                    end_col_offset=69,
                                                    value=Attribute(
                                                        lineno=15,
                                                        col_offset=53,
                                                        end_lineno=15,
                                                        end_col_offset=64,
                                                        value=Name(lineno=15, col_offset=53, end_lineno=15, end_col_offset=60, id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='iap_enrich_auto_done',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=16,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=27,
                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=27, id='session_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)