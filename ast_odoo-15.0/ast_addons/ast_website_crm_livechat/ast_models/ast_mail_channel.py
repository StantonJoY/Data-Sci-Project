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
            end_lineno=19,
            end_col_offset=19,
            name='MailChannel',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=18,
                    end_lineno=7,
                    end_col_offset=30,
                    value=Name(lineno=7, col_offset=18, end_lineno=7, end_col_offset=24, id='models', ctx=Load()),
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
                    end_col_offset=29,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=29, value='mail.channel', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=19,
                    name='_convert_visitor_to_lead',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=10, col_offset=33, end_lineno=10, end_col_offset=37, arg='self', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=39, end_lineno=10, end_col_offset=46, arg='partner', annotation=None, type_comment=None),
                            arg(lineno=10, col_offset=48, end_lineno=10, end_col_offset=51, arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=37,
                            value=Constant(lineno=11, col_offset=8, end_lineno=13, end_col_offset=37, value=' When website is installed, we can link the created lead from /lead command\n         to the current website_visitor. We do not use the lead name as it does not correspond\n         to the lead contact name.', kind=None),
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=78,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=12, id='lead', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=64,
                                    value=Call(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=39,
                                        func=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=20, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=14, col_offset=21, end_lineno=14, end_col_offset=32, id='MailChannel', ctx=Load()),
                                            Name(lineno=14, col_offset=34, end_lineno=14, end_col_offset=38, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_convert_visitor_to_lead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=14, col_offset=65, end_lineno=14, end_col_offset=72, id='partner', ctx=Load()),
                                    Name(lineno=14, col_offset=74, end_lineno=14, end_col_offset=77, id='key', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=54,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=20, id='visitor_sudo', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=23,
                                end_lineno=15,
                                end_col_offset=54,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=23,
                                    end_lineno=15,
                                    end_col_offset=52,
                                    value=Attribute(
                                        lineno=15,
                                        col_offset=23,
                                        end_lineno=15,
                                        end_col_offset=47,
                                        value=Name(lineno=15, col_offset=23, end_lineno=15, end_col_offset=27, id='self', ctx=Load()),
                                        attr='livechat_visitor_id',
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=16,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=72,
                            test=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=23, id='visitor_sudo', ctx=Load()),
                            body=[
                                Expr(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=60,
                                    value=Call(
                                        lineno=17,
                                        col_offset=12,
                                        end_lineno=17,
                                        end_col_offset=60,
                                        func=Attribute(
                                            lineno=17,
                                            col_offset=12,
                                            end_lineno=17,
                                            end_col_offset=30,
                                            value=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=24, id='visitor_sudo', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=17,
                                                col_offset=31,
                                                end_lineno=17,
                                                end_col_offset=59,
                                                keys=[Constant(lineno=17, col_offset=32, end_lineno=17, end_col_offset=42, value='lead_ids', kind=None)],
                                                values=[
                                                    List(
                                                        lineno=17,
                                                        col_offset=44,
                                                        end_lineno=17,
                                                        end_col_offset=58,
                                                        elts=[
                                                            Tuple(
                                                                lineno=17,
                                                                col_offset=45,
                                                                end_lineno=17,
                                                                end_col_offset=57,
                                                                elts=[
                                                                    Constant(lineno=17, col_offset=46, end_lineno=17, end_col_offset=47, value=4, kind=None),
                                                                    Attribute(
                                                                        lineno=17,
                                                                        col_offset=49,
                                                                        end_lineno=17,
                                                                        end_col_offset=56,
                                                                        value=Name(lineno=17, col_offset=49, end_lineno=17, end_col_offset=53, id='lead', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=72,
                                    targets=[
                                        Attribute(
                                            lineno=18,
                                            col_offset=12,
                                            end_lineno=18,
                                            end_col_offset=27,
                                            value=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=16, id='lead', ctx=Load()),
                                            attr='country_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        lineno=18,
                                        col_offset=30,
                                        end_lineno=18,
                                        end_col_offset=72,
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                lineno=18,
                                                col_offset=30,
                                                end_lineno=18,
                                                end_col_offset=45,
                                                value=Name(lineno=18, col_offset=30, end_lineno=18, end_col_offset=34, id='lead', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                lineno=18,
                                                col_offset=49,
                                                end_lineno=18,
                                                end_col_offset=72,
                                                value=Name(lineno=18, col_offset=49, end_lineno=18, end_col_offset=61, id='visitor_sudo', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=19,
                            value=Name(lineno=19, col_offset=15, end_lineno=19, end_col_offset=19, id='lead', ctx=Load()),
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