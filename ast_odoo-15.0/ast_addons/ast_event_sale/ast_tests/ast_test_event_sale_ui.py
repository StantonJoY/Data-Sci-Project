Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=30,
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=32,
            module='odoo.fields',
            names=[alias(name='Datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=39,
            module='odoo.tests',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=10,
            col_offset=0,
            end_lineno=29,
            end_col_offset=73,
            name='TestUi',
            bases=[Name(lineno=10, col_offset=13, end_lineno=10, end_col_offset=21, id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=29,
                    end_col_offset=73,
                    name='test_event_configurator',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=32, end_lineno=12, end_col_offset=36, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=10,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=13, id='event', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=16,
                                end_lineno=18,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=16,
                                    end_lineno=14,
                                    end_col_offset=46,
                                    value=Subscript(
                                        lineno=14,
                                        col_offset=16,
                                        end_lineno=14,
                                        end_col_offset=39,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=16,
                                            end_lineno=14,
                                            end_col_offset=24,
                                            value=Name(lineno=14, col_offset=16, end_lineno=14, end_col_offset=20, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=14, col_offset=25, end_lineno=14, end_col_offset=38, value='event.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=14,
                                        col_offset=47,
                                        end_lineno=18,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=15, col_offset=12, end_lineno=15, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=16, col_offset=12, end_lineno=16, end_col_offset=24, value='date_begin', kind=None),
                                            Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=22, value='date_end', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=15, col_offset=20, end_lineno=15, end_col_offset=45, value='Design Fair Los Angeles', kind=None),
                                            BinOp(
                                                lineno=16,
                                                col_offset=26,
                                                end_lineno=16,
                                                end_col_offset=60,
                                                left=Call(
                                                    lineno=16,
                                                    col_offset=26,
                                                    end_lineno=16,
                                                    end_col_offset=40,
                                                    func=Attribute(
                                                        lineno=16,
                                                        col_offset=26,
                                                        end_lineno=16,
                                                        end_col_offset=38,
                                                        value=Name(lineno=16, col_offset=26, end_lineno=16, end_col_offset=34, id='Datetime', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    lineno=16,
                                                    col_offset=43,
                                                    end_lineno=16,
                                                    end_col_offset=60,
                                                    func=Name(lineno=16, col_offset=43, end_lineno=16, end_col_offset=52, id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            lineno=16,
                                                            col_offset=53,
                                                            end_lineno=16,
                                                            end_col_offset=59,
                                                            arg='days',
                                                            value=Constant(lineno=16, col_offset=58, end_lineno=16, end_col_offset=59, value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            BinOp(
                                                lineno=17,
                                                col_offset=24,
                                                end_lineno=17,
                                                end_col_offset=58,
                                                left=Call(
                                                    lineno=17,
                                                    col_offset=24,
                                                    end_lineno=17,
                                                    end_col_offset=38,
                                                    func=Attribute(
                                                        lineno=17,
                                                        col_offset=24,
                                                        end_lineno=17,
                                                        end_col_offset=36,
                                                        value=Name(lineno=17, col_offset=24, end_lineno=17, end_col_offset=32, id='Datetime', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    lineno=17,
                                                    col_offset=41,
                                                    end_lineno=17,
                                                    end_col_offset=58,
                                                    func=Name(lineno=17, col_offset=41, end_lineno=17, end_col_offset=50, id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            lineno=17,
                                                            col_offset=51,
                                                            end_lineno=17,
                                                            end_col_offset=57,
                                                            arg='days',
                                                            value=Constant(lineno=17, col_offset=56, end_lineno=17, end_col_offset=57, value=5, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=11,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=28,
                                end_col_offset=11,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=45,
                                    value=Subscript(
                                        lineno=20,
                                        col_offset=8,
                                        end_lineno=20,
                                        end_col_offset=38,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=8,
                                            end_lineno=20,
                                            end_col_offset=16,
                                            value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=20, col_offset=17, end_lineno=20, end_col_offset=37, value='event.event.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=20,
                                        col_offset=46,
                                        end_lineno=28,
                                        end_col_offset=10,
                                        elts=[
                                            Dict(
                                                lineno=20,
                                                col_offset=47,
                                                end_lineno=24,
                                                end_col_offset=9,
                                                keys=[
                                                    Constant(lineno=21, col_offset=12, end_lineno=21, end_col_offset=18, value='name', kind=None),
                                                    Constant(lineno=22, col_offset=12, end_lineno=22, end_col_offset=22, value='event_id', kind=None),
                                                    Constant(lineno=23, col_offset=12, end_lineno=23, end_col_offset=24, value='product_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(lineno=21, col_offset=20, end_lineno=21, end_col_offset=30, value='Standard', kind=None),
                                                    Attribute(
                                                        lineno=22,
                                                        col_offset=24,
                                                        end_lineno=22,
                                                        end_col_offset=32,
                                                        value=Name(lineno=22, col_offset=24, end_lineno=22, end_col_offset=29, id='event', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=23,
                                                        col_offset=26,
                                                        end_lineno=23,
                                                        end_col_offset=77,
                                                        value=Call(
                                                            lineno=23,
                                                            col_offset=26,
                                                            end_lineno=23,
                                                            end_col_offset=74,
                                                            func=Attribute(
                                                                lineno=23,
                                                                col_offset=26,
                                                                end_lineno=23,
                                                                end_col_offset=38,
                                                                value=Attribute(
                                                                    lineno=23,
                                                                    col_offset=26,
                                                                    end_lineno=23,
                                                                    end_col_offset=34,
                                                                    value=Name(lineno=23, col_offset=26, end_lineno=23, end_col_offset=30, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=23, col_offset=39, end_lineno=23, end_col_offset=73, value='event_sale.product_product_event', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                lineno=24,
                                                col_offset=11,
                                                end_lineno=28,
                                                end_col_offset=9,
                                                keys=[
                                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=18, value='name', kind=None),
                                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=22, value='event_id', kind=None),
                                                    Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=24, value='product_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(lineno=25, col_offset=20, end_lineno=25, end_col_offset=25, value='VIP', kind=None),
                                                    Attribute(
                                                        lineno=26,
                                                        col_offset=24,
                                                        end_lineno=26,
                                                        end_col_offset=32,
                                                        value=Name(lineno=26, col_offset=24, end_lineno=26, end_col_offset=29, id='event', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=27,
                                                        col_offset=26,
                                                        end_lineno=27,
                                                        end_col_offset=77,
                                                        value=Call(
                                                            lineno=27,
                                                            col_offset=26,
                                                            end_lineno=27,
                                                            end_col_offset=74,
                                                            func=Attribute(
                                                                lineno=27,
                                                                col_offset=26,
                                                                end_lineno=27,
                                                                end_col_offset=38,
                                                                value=Attribute(
                                                                    lineno=27,
                                                                    col_offset=26,
                                                                    end_lineno=27,
                                                                    end_col_offset=34,
                                                                    value=Name(lineno=27, col_offset=26, end_lineno=27, end_col_offset=30, id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ref',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(lineno=27, col_offset=39, end_lineno=27, end_col_offset=73, value='event_sale.product_product_event', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=73,
                            value=Call(
                                lineno=29,
                                col_offset=8,
                                end_lineno=29,
                                end_col_offset=73,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=8,
                                    end_lineno=29,
                                    end_col_offset=23,
                                    value=Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=12, id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(lineno=29, col_offset=24, end_lineno=29, end_col_offset=30, value='/web', kind=None),
                                    Constant(lineno=29, col_offset=32, end_lineno=29, end_col_offset=57, value='event_configurator_tour', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        lineno=29,
                                        col_offset=59,
                                        end_lineno=29,
                                        end_col_offset=72,
                                        arg='login',
                                        value=Constant(lineno=29, col_offset=65, end_lineno=29, end_col_offset=72, value='admin', kind=None),
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
                    lineno=9,
                    col_offset=1,
                    end_lineno=9,
                    end_col_offset=38,
                    func=Name(lineno=9, col_offset=1, end_lineno=9, end_col_offset=7, id='tagged', ctx=Load()),
                    args=[
                        Constant(lineno=9, col_offset=8, end_lineno=9, end_col_offset=22, value='post_install', kind=None),
                        Constant(lineno=9, col_offset=24, end_lineno=9, end_col_offset=37, value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)