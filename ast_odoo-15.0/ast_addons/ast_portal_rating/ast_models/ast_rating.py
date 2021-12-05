Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=46,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=23,
            end_col_offset=48,
            name='Rating',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=13,
                    end_lineno=6,
                    end_col_offset=25,
                    value=Name(lineno=6, col_offset=13, end_lineno=6, end_col_offset=19, id='models', ctx=Load()),
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
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=30, value='rating.rating', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=56,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=21, id='publisher_comment', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=24,
                        end_lineno=10,
                        end_col_offset=56,
                        func=Attribute(
                            lineno=10,
                            col_offset=24,
                            end_lineno=10,
                            end_col_offset=35,
                            value=Name(lineno=10, col_offset=24, end_lineno=10, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=36, end_lineno=10, end_col_offset=55, value='Publisher comment', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=70,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='publisher_id', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=19,
                        end_lineno=12,
                        end_col_offset=70,
                        func=Attribute(
                            lineno=11,
                            col_offset=19,
                            end_lineno=11,
                            end_col_offset=34,
                            value=Name(lineno=11, col_offset=19, end_lineno=11, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=11, col_offset=35, end_lineno=11, end_col_offset=48, value='res.partner', kind=None),
                            Constant(lineno=11, col_offset=50, end_lineno=11, end_col_offset=64, value='Commented by', kind=None),
                        ],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=35,
                                end_lineno=12,
                                end_col_offset=54,
                                arg='ondelete',
                                value=Constant(lineno=12, col_offset=44, end_lineno=12, end_col_offset=54, value='set null', kind=None),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=56,
                                end_lineno=12,
                                end_col_offset=69,
                                arg='readonly',
                                value=Constant(lineno=12, col_offset=65, end_lineno=12, end_col_offset=69, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=71,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=22, id='publisher_datetime', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=25,
                        end_lineno=13,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=13,
                            col_offset=25,
                            end_lineno=13,
                            end_col_offset=40,
                            value=Name(lineno=13, col_offset=25, end_lineno=13, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=41, end_lineno=13, end_col_offset=55, value='Commented on', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=57,
                                end_lineno=13,
                                end_col_offset=70,
                                arg='readonly',
                                value=Constant(lineno=13, col_offset=66, end_lineno=13, end_col_offset=70, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=48,
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=15, col_offset=14, end_lineno=15, end_col_offset=18, arg='self', annotation=None, type_comment=None),
                            arg(lineno=15, col_offset=20, end_lineno=15, end_col_offset=26, arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            lineno=16,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=68,
                            test=Call(
                                lineno=16,
                                col_offset=11,
                                end_lineno=16,
                                end_col_offset=42,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=11,
                                    end_lineno=16,
                                    end_col_offset=21,
                                    value=Name(lineno=16, col_offset=11, end_lineno=16, end_col_offset=17, id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(lineno=16, col_offset=22, end_lineno=16, end_col_offset=41, value='publisher_comment', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=114,
                                    test=UnaryOp(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=77,
                                        op=Not(),
                                        operand=Call(
                                            lineno=17,
                                            col_offset=19,
                                            end_lineno=17,
                                            end_col_offset=77,
                                            func=Attribute(
                                                lineno=17,
                                                col_offset=19,
                                                end_lineno=17,
                                                end_col_offset=42,
                                                value=Attribute(
                                                    lineno=17,
                                                    col_offset=19,
                                                    end_lineno=17,
                                                    end_col_offset=32,
                                                    value=Attribute(
                                                        lineno=17,
                                                        col_offset=19,
                                                        end_lineno=17,
                                                        end_col_offset=27,
                                                        value=Name(lineno=17, col_offset=19, end_lineno=17, end_col_offset=23, id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(lineno=17, col_offset=43, end_lineno=17, end_col_offset=76, value='website.group_website_publisher', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            lineno=18,
                                            col_offset=16,
                                            end_lineno=18,
                                            end_col_offset=114,
                                            exc=Call(
                                                lineno=18,
                                                col_offset=22,
                                                end_lineno=18,
                                                end_col_offset=114,
                                                func=Attribute(
                                                    lineno=18,
                                                    col_offset=22,
                                                    end_lineno=18,
                                                    end_col_offset=44,
                                                    value=Name(lineno=18, col_offset=22, end_lineno=18, end_col_offset=32, id='exceptions', ctx=Load()),
                                                    attr='AccessError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        lineno=18,
                                                        col_offset=45,
                                                        end_lineno=18,
                                                        end_col_offset=113,
                                                        func=Name(lineno=18, col_offset=45, end_lineno=18, end_col_offset=46, id='_', ctx=Load()),
                                                        args=[Constant(lineno=18, col_offset=47, end_lineno=18, end_col_offset=112, value='Only the publisher of the website can change the rating comment', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=20,
                                    end_col_offset=68,
                                    test=UnaryOp(
                                        lineno=19,
                                        col_offset=15,
                                        end_lineno=19,
                                        end_col_offset=51,
                                        op=Not(),
                                        operand=Call(
                                            lineno=19,
                                            col_offset=19,
                                            end_lineno=19,
                                            end_col_offset=51,
                                            func=Attribute(
                                                lineno=19,
                                                col_offset=19,
                                                end_lineno=19,
                                                end_col_offset=29,
                                                value=Name(lineno=19, col_offset=19, end_lineno=19, end_col_offset=25, id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(lineno=19, col_offset=30, end_lineno=19, end_col_offset=50, value='publisher_datetime', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=20,
                                            col_offset=16,
                                            end_lineno=20,
                                            end_col_offset=68,
                                            targets=[
                                                Subscript(
                                                    lineno=20,
                                                    col_offset=16,
                                                    end_lineno=20,
                                                    end_col_offset=44,
                                                    value=Name(lineno=20, col_offset=16, end_lineno=20, end_col_offset=22, id='values', ctx=Load()),
                                                    slice=Constant(lineno=20, col_offset=23, end_lineno=20, end_col_offset=43, value='publisher_datetime', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=20,
                                                col_offset=47,
                                                end_lineno=20,
                                                end_col_offset=68,
                                                func=Attribute(
                                                    lineno=20,
                                                    col_offset=47,
                                                    end_lineno=20,
                                                    end_col_offset=66,
                                                    value=Attribute(
                                                        lineno=20,
                                                        col_offset=47,
                                                        end_lineno=20,
                                                        end_col_offset=62,
                                                        value=Name(lineno=20, col_offset=47, end_lineno=20, end_col_offset=53, id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    lineno=21,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=68,
                                    test=UnaryOp(
                                        lineno=21,
                                        col_offset=15,
                                        end_lineno=21,
                                        end_col_offset=45,
                                        op=Not(),
                                        operand=Call(
                                            lineno=21,
                                            col_offset=19,
                                            end_lineno=21,
                                            end_col_offset=45,
                                            func=Attribute(
                                                lineno=21,
                                                col_offset=19,
                                                end_lineno=21,
                                                end_col_offset=29,
                                                value=Name(lineno=21, col_offset=19, end_lineno=21, end_col_offset=25, id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(lineno=21, col_offset=30, end_lineno=21, end_col_offset=44, value='publisher_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=22,
                                            col_offset=16,
                                            end_lineno=22,
                                            end_col_offset=68,
                                            targets=[
                                                Subscript(
                                                    lineno=22,
                                                    col_offset=16,
                                                    end_lineno=22,
                                                    end_col_offset=38,
                                                    value=Name(lineno=22, col_offset=16, end_lineno=22, end_col_offset=22, id='values', ctx=Load()),
                                                    slice=Constant(lineno=22, col_offset=23, end_lineno=22, end_col_offset=37, value='publisher_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                lineno=22,
                                                col_offset=41,
                                                end_lineno=22,
                                                end_col_offset=68,
                                                value=Attribute(
                                                    lineno=22,
                                                    col_offset=41,
                                                    end_lineno=22,
                                                    end_col_offset=65,
                                                    value=Attribute(
                                                        lineno=22,
                                                        col_offset=41,
                                                        end_lineno=22,
                                                        end_col_offset=54,
                                                        value=Attribute(
                                                            lineno=22,
                                                            col_offset=41,
                                                            end_lineno=22,
                                                            end_col_offset=49,
                                                            value=Name(lineno=22, col_offset=41, end_lineno=22, end_col_offset=45, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=48,
                            value=Call(
                                lineno=23,
                                col_offset=15,
                                end_lineno=23,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=23,
                                    col_offset=15,
                                    end_lineno=23,
                                    end_col_offset=40,
                                    value=Call(
                                        lineno=23,
                                        col_offset=15,
                                        end_lineno=23,
                                        end_col_offset=34,
                                        func=Name(lineno=23, col_offset=15, end_lineno=23, end_col_offset=20, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=23, col_offset=21, end_lineno=23, end_col_offset=27, id='Rating', ctx=Load()),
                                            Name(lineno=23, col_offset=29, end_lineno=23, end_col_offset=33, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=23, col_offset=41, end_lineno=23, end_col_offset=47, id='values', ctx=Load())],
                                keywords=[],
                            ),
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