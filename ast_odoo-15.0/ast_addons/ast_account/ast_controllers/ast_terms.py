Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=24,
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
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
            end_lineno=21,
            end_col_offset=78,
            name='TermsController',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=22,
                    end_lineno=8,
                    end_col_offset=37,
                    value=Name(lineno=8, col_offset=22, end_lineno=8, end_col_offset=26, id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=78,
                    name='terms_conditions',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=11, col_offset=25, end_lineno=11, end_col_offset=29, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=11, col_offset=33, end_lineno=11, end_col_offset=39, arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=108,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=25, id='use_invoice_terms', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=28,
                                end_lineno=12,
                                end_col_offset=108,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=28,
                                    end_lineno=12,
                                    end_col_offset=79,
                                    value=Call(
                                        lineno=12,
                                        col_offset=28,
                                        end_lineno=12,
                                        end_col_offset=69,
                                        func=Attribute(
                                            lineno=12,
                                            col_offset=28,
                                            end_lineno=12,
                                            end_col_offset=67,
                                            value=Subscript(
                                                lineno=12,
                                                col_offset=28,
                                                end_lineno=12,
                                                end_col_offset=62,
                                                value=Attribute(
                                                    lineno=12,
                                                    col_offset=28,
                                                    end_lineno=12,
                                                    end_col_offset=39,
                                                    value=Name(lineno=12, col_offset=28, end_lineno=12, end_col_offset=35, id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=12, col_offset=40, end_lineno=12, end_col_offset=61, value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=12, col_offset=80, end_lineno=12, end_col_offset=107, value='account.use_invoice_terms', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=101,
                            test=UnaryOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=79,
                                op=Not(),
                                operand=BoolOp(
                                    lineno=13,
                                    col_offset=16,
                                    end_lineno=13,
                                    end_col_offset=78,
                                    op=And(),
                                    values=[
                                        Name(lineno=13, col_offset=16, end_lineno=13, end_col_offset=33, id='use_invoice_terms', ctx=Load()),
                                        Compare(
                                            lineno=13,
                                            col_offset=38,
                                            end_lineno=13,
                                            end_col_offset=78,
                                            left=Attribute(
                                                lineno=13,
                                                col_offset=38,
                                                end_lineno=13,
                                                end_col_offset=68,
                                                value=Attribute(
                                                    lineno=13,
                                                    col_offset=38,
                                                    end_lineno=13,
                                                    end_col_offset=57,
                                                    value=Attribute(
                                                        lineno=13,
                                                        col_offset=38,
                                                        end_lineno=13,
                                                        end_col_offset=49,
                                                        value=Name(lineno=13, col_offset=38, end_lineno=13, end_col_offset=45, id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='terms_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=13, col_offset=72, end_lineno=13, end_col_offset=78, value='html', kind=None)],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=101,
                                    value=Call(
                                        lineno=14,
                                        col_offset=19,
                                        end_lineno=16,
                                        end_col_offset=101,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=19,
                                            end_lineno=14,
                                            end_col_offset=33,
                                            value=Name(lineno=14, col_offset=19, end_lineno=14, end_col_offset=26, id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(lineno=14, col_offset=34, end_lineno=14, end_col_offset=59, value='http_routing.http_error', kind=None),
                                            Dict(
                                                lineno=14,
                                                col_offset=61,
                                                end_lineno=16,
                                                end_col_offset=100,
                                                keys=[
                                                    Constant(lineno=15, col_offset=16, end_lineno=15, end_col_offset=29, value='status_code', kind=None),
                                                    Constant(lineno=16, col_offset=16, end_lineno=16, end_col_offset=32, value='status_message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        lineno=15,
                                                        col_offset=31,
                                                        end_lineno=15,
                                                        end_col_offset=40,
                                                        func=Name(lineno=15, col_offset=31, end_lineno=15, end_col_offset=32, id='_', ctx=Load()),
                                                        args=[Constant(lineno=15, col_offset=33, end_lineno=15, end_col_offset=39, value='Oops', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        lineno=16,
                                                        col_offset=34,
                                                        end_lineno=16,
                                                        end_col_offset=99,
                                                        func=Name(lineno=16, col_offset=34, end_lineno=16, end_col_offset=35, id='_', ctx=Load()),
                                                        args=[Constant(lineno=16, col_offset=36, end_lineno=16, end_col_offset=98, value="The requested page is invalid, or doesn't exist anymore.", kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=17,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=9,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=14, id='values', ctx=Store())],
                            value=Dict(
                                lineno=17,
                                col_offset=17,
                                end_lineno=20,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=31, value='use_invoice_terms', kind=None),
                                    Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=21, value='company', kind=None),
                                ],
                                values=[
                                    Name(lineno=18, col_offset=33, end_lineno=18, end_col_offset=50, id='use_invoice_terms', ctx=Load()),
                                    Attribute(
                                        lineno=19,
                                        col_offset=23,
                                        end_lineno=19,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=19,
                                            col_offset=23,
                                            end_lineno=19,
                                            end_col_offset=34,
                                            value=Name(lineno=19, col_offset=23, end_lineno=19, end_col_offset=30, id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=78,
                            value=Call(
                                lineno=21,
                                col_offset=15,
                                end_lineno=21,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=21,
                                    col_offset=15,
                                    end_lineno=21,
                                    end_col_offset=29,
                                    value=Name(lineno=21, col_offset=15, end_lineno=21, end_col_offset=22, id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=69, value='account.account_terms_conditions_page', kind=None),
                                    Name(lineno=21, col_offset=71, end_lineno=21, end_col_offset=77, id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=81,
                            func=Attribute(
                                lineno=10,
                                col_offset=5,
                                end_lineno=10,
                                end_col_offset=15,
                                value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=24, value='/terms', kind=None)],
                            keywords=[
                                keyword(
                                    lineno=10,
                                    col_offset=26,
                                    end_lineno=10,
                                    end_col_offset=37,
                                    arg='type',
                                    value=Constant(lineno=10, col_offset=31, end_lineno=10, end_col_offset=37, value='http', kind=None),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=39,
                                    end_lineno=10,
                                    end_col_offset=52,
                                    arg='auth',
                                    value=Constant(lineno=10, col_offset=44, end_lineno=10, end_col_offset=52, value='public', kind=None),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=54,
                                    end_lineno=10,
                                    end_col_offset=66,
                                    arg='website',
                                    value=Constant(lineno=10, col_offset=62, end_lineno=10, end_col_offset=66, value=True, kind=None),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=68,
                                    end_lineno=10,
                                    end_col_offset=80,
                                    arg='sitemap',
                                    value=Constant(lineno=10, col_offset=76, end_lineno=10, end_col_offset=80, value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)