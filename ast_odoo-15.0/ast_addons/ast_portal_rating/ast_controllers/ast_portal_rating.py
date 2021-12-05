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
            end_lineno=17,
            end_col_offset=90,
            name='PortalRating',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=19,
                    end_lineno=8,
                    end_col_offset=34,
                    value=Name(lineno=8, col_offset=19, end_lineno=8, end_col_offset=23, id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=11,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=90,
                    name='publish_rating_comment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=11, col_offset=31, end_lineno=11, end_col_offset=35, arg='self', annotation=None, type_comment=None),
                            arg(lineno=11, col_offset=37, end_lineno=11, end_col_offset=46, arg='rating_id', annotation=None, type_comment=None),
                            arg(lineno=11, col_offset=48, end_lineno=11, end_col_offset=65, arg='publisher_comment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=83,
                            targets=[Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=14, id='rating', ctx=Store())],
                            value=Call(
                                lineno=12,
                                col_offset=17,
                                end_lineno=12,
                                end_col_offset=83,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=17,
                                    end_lineno=12,
                                    end_col_offset=52,
                                    value=Subscript(
                                        lineno=12,
                                        col_offset=17,
                                        end_lineno=12,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=12,
                                            col_offset=17,
                                            end_lineno=12,
                                            end_col_offset=28,
                                            value=Name(lineno=12, col_offset=17, end_lineno=12, end_col_offset=24, id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=12, col_offset=29, end_lineno=12, end_col_offset=44, value='rating.rating', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=12,
                                        col_offset=53,
                                        end_lineno=12,
                                        end_col_offset=82,
                                        elts=[
                                            Tuple(
                                                lineno=12,
                                                col_offset=54,
                                                end_lineno=12,
                                                end_col_offset=81,
                                                elts=[
                                                    Constant(lineno=12, col_offset=55, end_lineno=12, end_col_offset=59, value='id', kind=None),
                                                    Constant(lineno=12, col_offset=61, end_lineno=12, end_col_offset=64, value='=', kind=None),
                                                    Call(
                                                        lineno=12,
                                                        col_offset=66,
                                                        end_lineno=12,
                                                        end_col_offset=80,
                                                        func=Name(lineno=12, col_offset=66, end_lineno=12, end_col_offset=69, id='int', ctx=Load()),
                                                        args=[Name(lineno=12, col_offset=70, end_lineno=12, end_col_offset=79, id='rating_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=13,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=49,
                            test=UnaryOp(
                                lineno=13,
                                col_offset=11,
                                end_lineno=13,
                                end_col_offset=21,
                                op=Not(),
                                operand=Name(lineno=13, col_offset=15, end_lineno=13, end_col_offset=21, id='rating', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    lineno=14,
                                    col_offset=12,
                                    end_lineno=14,
                                    end_col_offset=49,
                                    value=Dict(
                                        lineno=14,
                                        col_offset=19,
                                        end_lineno=14,
                                        end_col_offset=49,
                                        keys=[Constant(lineno=14, col_offset=20, end_lineno=14, end_col_offset=27, value='error', kind=None)],
                                        values=[
                                            Call(
                                                lineno=14,
                                                col_offset=29,
                                                end_lineno=14,
                                                end_col_offset=48,
                                                func=Name(lineno=14, col_offset=29, end_lineno=14, end_col_offset=30, id='_', ctx=Load()),
                                                args=[Constant(lineno=14, col_offset=31, end_lineno=14, end_col_offset=47, value='Invalid rating', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=62,
                            value=Call(
                                lineno=15,
                                col_offset=8,
                                end_lineno=15,
                                end_col_offset=62,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=8,
                                    end_lineno=15,
                                    end_col_offset=20,
                                    value=Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=14, id='rating', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=15,
                                        col_offset=21,
                                        end_lineno=15,
                                        end_col_offset=61,
                                        keys=[Constant(lineno=15, col_offset=22, end_lineno=15, end_col_offset=41, value='publisher_comment', kind=None)],
                                        values=[Name(lineno=15, col_offset=43, end_lineno=15, end_col_offset=60, id='publisher_comment', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=90,
                            value=Subscript(
                                lineno=17,
                                col_offset=15,
                                end_lineno=17,
                                end_col_offset=90,
                                value=Call(
                                    lineno=17,
                                    col_offset=15,
                                    end_lineno=17,
                                    end_col_offset=87,
                                    func=Attribute(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=26,
                                        value=Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=21, id='rating', ctx=Load()),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            lineno=17,
                                            col_offset=27,
                                            end_lineno=17,
                                            end_col_offset=86,
                                            elts=[
                                                Constant(lineno=17, col_offset=28, end_lineno=17, end_col_offset=47, value='publisher_comment', kind=None),
                                                Constant(lineno=17, col_offset=49, end_lineno=17, end_col_offset=63, value='publisher_id', kind=None),
                                                Constant(lineno=17, col_offset=65, end_lineno=17, end_col_offset=85, value='publisher_datetime', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(lineno=17, col_offset=88, end_lineno=17, end_col_offset=89, value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=10,
                            col_offset=5,
                            end_lineno=10,
                            end_col_offset=102,
                            func=Attribute(
                                lineno=10,
                                col_offset=5,
                                end_lineno=10,
                                end_col_offset=15,
                                value=Name(lineno=10, col_offset=5, end_lineno=10, end_col_offset=9, id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    lineno=10,
                                    col_offset=16,
                                    end_lineno=10,
                                    end_col_offset=43,
                                    elts=[Constant(lineno=10, col_offset=17, end_lineno=10, end_col_offset=42, value='/website/rating/comment', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    lineno=10,
                                    col_offset=45,
                                    end_lineno=10,
                                    end_col_offset=56,
                                    arg='type',
                                    value=Constant(lineno=10, col_offset=50, end_lineno=10, end_col_offset=56, value='json', kind=None),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=58,
                                    end_lineno=10,
                                    end_col_offset=69,
                                    arg='auth',
                                    value=Constant(lineno=10, col_offset=63, end_lineno=10, end_col_offset=69, value='user', kind=None),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=71,
                                    end_lineno=10,
                                    end_col_offset=87,
                                    arg='methods',
                                    value=List(
                                        lineno=10,
                                        col_offset=79,
                                        end_lineno=10,
                                        end_col_offset=87,
                                        elts=[Constant(lineno=10, col_offset=80, end_lineno=10, end_col_offset=86, value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    lineno=10,
                                    col_offset=89,
                                    end_lineno=10,
                                    end_col_offset=101,
                                    arg='website',
                                    value=Constant(lineno=10, col_offset=97, end_lineno=10, end_col_offset=101, value=True, kind=None),
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