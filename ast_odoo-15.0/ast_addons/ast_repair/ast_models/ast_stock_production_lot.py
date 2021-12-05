Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=35,
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=39,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=39,
            end_col_offset=21,
            name='ProductionLot',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=20,
                    end_lineno=6,
                    end_col_offset=32,
                    value=Name(lineno=6, col_offset=20, end_lineno=6, end_col_offset=26, id='models', ctx=Load()),
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
                    end_col_offset=37,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=7, col_offset=15, end_lineno=7, end_col_offset=37, value='stock.production.lot', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=116,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=20, id='repair_order_ids', ctx=Store())],
                    value=Call(
                        lineno=9,
                        col_offset=23,
                        end_lineno=9,
                        end_col_offset=116,
                        func=Attribute(
                            lineno=9,
                            col_offset=23,
                            end_lineno=9,
                            end_col_offset=39,
                            value=Name(lineno=9, col_offset=23, end_lineno=9, end_col_offset=29, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=9, col_offset=40, end_lineno=9, end_col_offset=54, value='repair.order', kind=None)],
                        keywords=[
                            keyword(
                                lineno=9,
                                col_offset=56,
                                end_lineno=9,
                                end_col_offset=78,
                                arg='string',
                                value=Constant(lineno=9, col_offset=63, end_lineno=9, end_col_offset=78, value='Repair Orders', kind=None),
                            ),
                            keyword(
                                lineno=9,
                                col_offset=80,
                                end_lineno=9,
                                end_col_offset=115,
                                arg='compute',
                                value=Constant(lineno=9, col_offset=88, end_lineno=9, end_col_offset=115, value='_compute_repair_order_ids', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=98,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=22, id='repair_order_count', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=25,
                        end_lineno=10,
                        end_col_offset=98,
                        func=Attribute(
                            lineno=10,
                            col_offset=25,
                            end_lineno=10,
                            end_col_offset=39,
                            value=Name(lineno=10, col_offset=25, end_lineno=10, end_col_offset=31, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=10, col_offset=40, end_lineno=10, end_col_offset=60, value='Repair order count', kind=None)],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=62,
                                end_lineno=10,
                                end_col_offset=97,
                                arg='compute',
                                value=Constant(lineno=10, col_offset=70, end_lineno=10, end_col_offset=97, value='_compute_repair_order_ids', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=62,
                    name='_compute_repair_order_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=34, end_lineno=13, end_col_offset=38, arg='self', annotation=None, type_comment=None)],
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
                            end_lineno=14,
                            end_col_offset=69,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=21, id='repair_orders', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=24,
                                end_lineno=14,
                                end_col_offset=69,
                                func=Name(lineno=14, col_offset=24, end_lineno=14, end_col_offset=35, id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        lineno=14,
                                        col_offset=36,
                                        end_lineno=14,
                                        end_col_offset=68,
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            lineno=14,
                                            col_offset=44,
                                            end_lineno=14,
                                            end_col_offset=68,
                                            value=Attribute(
                                                lineno=14,
                                                col_offset=44,
                                                end_lineno=14,
                                                end_col_offset=52,
                                                value=Name(lineno=14, col_offset=44, end_lineno=14, end_col_offset=48, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=14, col_offset=53, end_lineno=14, end_col_offset=67, value='repair.order', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            lineno=15,
                            col_offset=8,
                            end_lineno=16,
                            end_col_offset=73,
                            target=Name(lineno=15, col_offset=12, end_lineno=15, end_col_offset=23, id='repair_line', ctx=Store()),
                            iter=Call(
                                lineno=15,
                                col_offset=27,
                                end_lineno=15,
                                end_col_offset=111,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=27,
                                    end_lineno=15,
                                    end_col_offset=57,
                                    value=Subscript(
                                        lineno=15,
                                        col_offset=27,
                                        end_lineno=15,
                                        end_col_offset=50,
                                        value=Attribute(
                                            lineno=15,
                                            col_offset=27,
                                            end_lineno=15,
                                            end_col_offset=35,
                                            value=Name(lineno=15, col_offset=27, end_lineno=15, end_col_offset=31, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=15, col_offset=36, end_lineno=15, end_col_offset=49, value='repair.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=15,
                                        col_offset=58,
                                        end_lineno=15,
                                        end_col_offset=110,
                                        elts=[
                                            Tuple(
                                                lineno=15,
                                                col_offset=59,
                                                end_lineno=15,
                                                end_col_offset=85,
                                                elts=[
                                                    Constant(lineno=15, col_offset=60, end_lineno=15, end_col_offset=68, value='lot_id', kind=None),
                                                    Constant(lineno=15, col_offset=70, end_lineno=15, end_col_offset=74, value='in', kind=None),
                                                    Attribute(
                                                        lineno=15,
                                                        col_offset=76,
                                                        end_lineno=15,
                                                        end_col_offset=84,
                                                        value=Name(lineno=15, col_offset=76, end_lineno=15, end_col_offset=80, id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=15,
                                                col_offset=87,
                                                end_lineno=15,
                                                end_col_offset=109,
                                                elts=[
                                                    Constant(lineno=15, col_offset=88, end_lineno=15, end_col_offset=95, value='state', kind=None),
                                                    Constant(lineno=15, col_offset=97, end_lineno=15, end_col_offset=100, value='=', kind=None),
                                                    Constant(lineno=15, col_offset=102, end_lineno=15, end_col_offset=108, value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=73,
                                    target=Subscript(
                                        lineno=16,
                                        col_offset=12,
                                        end_lineno=16,
                                        end_col_offset=48,
                                        value=Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=25, id='repair_orders', ctx=Load()),
                                        slice=Attribute(
                                            lineno=16,
                                            col_offset=26,
                                            end_lineno=16,
                                            end_col_offset=47,
                                            value=Attribute(
                                                lineno=16,
                                                col_offset=26,
                                                end_lineno=16,
                                                end_col_offset=44,
                                                value=Name(lineno=16, col_offset=26, end_lineno=16, end_col_offset=37, id='repair_line', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Attribute(
                                        lineno=16,
                                        col_offset=52,
                                        end_lineno=16,
                                        end_col_offset=73,
                                        value=Name(lineno=16, col_offset=52, end_lineno=16, end_col_offset=63, id='repair_line', ctx=Load()),
                                        attr='repair_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=62,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=15, id='lot', ctx=Store()),
                            iter=Name(lineno=17, col_offset=19, end_lineno=17, end_col_offset=23, id='self', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=18,
                                    end_col_offset=56,
                                    targets=[
                                        Attribute(
                                            lineno=18,
                                            col_offset=12,
                                            end_lineno=18,
                                            end_col_offset=32,
                                            value=Name(lineno=18, col_offset=12, end_lineno=18, end_col_offset=15, id='lot', ctx=Load()),
                                            attr='repair_order_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        lineno=18,
                                        col_offset=35,
                                        end_lineno=18,
                                        end_col_offset=56,
                                        value=Name(lineno=18, col_offset=35, end_lineno=18, end_col_offset=48, id='repair_orders', ctx=Load()),
                                        slice=Attribute(
                                            lineno=18,
                                            col_offset=49,
                                            end_lineno=18,
                                            end_col_offset=55,
                                            value=Name(lineno=18, col_offset=49, end_lineno=18, end_col_offset=52, id='lot', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    lineno=19,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=62,
                                    targets=[
                                        Attribute(
                                            lineno=19,
                                            col_offset=12,
                                            end_lineno=19,
                                            end_col_offset=34,
                                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=15, id='lot', ctx=Load()),
                                            attr='repair_order_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=19,
                                        col_offset=37,
                                        end_lineno=19,
                                        end_col_offset=62,
                                        func=Name(lineno=19, col_offset=37, end_lineno=19, end_col_offset=40, id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                lineno=19,
                                                col_offset=41,
                                                end_lineno=19,
                                                end_col_offset=61,
                                                value=Name(lineno=19, col_offset=41, end_lineno=19, end_col_offset=44, id='lot', ctx=Load()),
                                                attr='repair_order_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=12,
                            col_offset=5,
                            end_lineno=12,
                            end_col_offset=24,
                            func=Attribute(
                                lineno=12,
                                col_offset=5,
                                end_lineno=12,
                                end_col_offset=16,
                                value=Name(lineno=12, col_offset=5, end_lineno=12, end_col_offset=8, id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=12, col_offset=17, end_lineno=12, end_col_offset=23, value='name', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=39,
                    end_col_offset=21,
                    name='action_view_ro',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=23, end_lineno=21, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=25,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=22,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=23,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=9,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=14, id='action', ctx=Store())],
                            value=Dict(
                                lineno=24,
                                col_offset=17,
                                end_lineno=27,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=25, col_offset=12, end_lineno=25, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=18, value='type', kind=None),
                                ],
                                values=[
                                    Constant(lineno=25, col_offset=25, end_lineno=25, end_col_offset=39, value='repair.order', kind=None),
                                    Constant(lineno=26, col_offset=20, end_lineno=26, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=28,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=14,
                            test=Compare(
                                lineno=28,
                                col_offset=11,
                                end_lineno=28,
                                end_col_offset=42,
                                left=Call(
                                    lineno=28,
                                    col_offset=11,
                                    end_lineno=28,
                                    end_col_offset=37,
                                    func=Name(lineno=28, col_offset=11, end_lineno=28, end_col_offset=14, id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=28,
                                            col_offset=15,
                                            end_lineno=28,
                                            end_col_offset=36,
                                            value=Name(lineno=28, col_offset=15, end_lineno=28, end_col_offset=19, id='self', ctx=Load()),
                                            attr='repair_order_ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(lineno=28, col_offset=41, end_lineno=28, end_col_offset=42, value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    lineno=29,
                                    col_offset=12,
                                    end_lineno=32,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=29,
                                        col_offset=12,
                                        end_lineno=32,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=29,
                                            col_offset=12,
                                            end_lineno=29,
                                            end_col_offset=25,
                                            value=Name(lineno=29, col_offset=12, end_lineno=29, end_col_offset=18, id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=29,
                                                col_offset=26,
                                                end_lineno=32,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=30, col_offset=16, end_lineno=30, end_col_offset=27, value='view_mode', kind=None),
                                                    Constant(lineno=31, col_offset=16, end_lineno=31, end_col_offset=24, value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(lineno=30, col_offset=29, end_lineno=30, end_col_offset=35, value='form', kind=None),
                                                    Attribute(
                                                        lineno=31,
                                                        col_offset=26,
                                                        end_lineno=31,
                                                        end_col_offset=53,
                                                        value=Subscript(
                                                            lineno=31,
                                                            col_offset=26,
                                                            end_lineno=31,
                                                            end_col_offset=50,
                                                            value=Attribute(
                                                                lineno=31,
                                                                col_offset=26,
                                                                end_lineno=31,
                                                                end_col_offset=47,
                                                                value=Name(lineno=31, col_offset=26, end_lineno=31, end_col_offset=30, id='self', ctx=Load()),
                                                                attr='repair_order_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(lineno=31, col_offset=48, end_lineno=31, end_col_offset=49, value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    lineno=34,
                                    col_offset=12,
                                    end_lineno=38,
                                    end_col_offset=14,
                                    value=Call(
                                        lineno=34,
                                        col_offset=12,
                                        end_lineno=38,
                                        end_col_offset=14,
                                        func=Attribute(
                                            lineno=34,
                                            col_offset=12,
                                            end_lineno=34,
                                            end_col_offset=25,
                                            value=Name(lineno=34, col_offset=12, end_lineno=34, end_col_offset=18, id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=34,
                                                col_offset=26,
                                                end_lineno=38,
                                                end_col_offset=13,
                                                keys=[
                                                    Constant(lineno=35, col_offset=16, end_lineno=35, end_col_offset=22, value='name', kind=None),
                                                    Constant(lineno=36, col_offset=16, end_lineno=36, end_col_offset=24, value='domain', kind=None),
                                                    Constant(lineno=37, col_offset=16, end_lineno=37, end_col_offset=27, value='view_mode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        lineno=35,
                                                        col_offset=24,
                                                        end_lineno=35,
                                                        end_col_offset=59,
                                                        func=Name(lineno=35, col_offset=24, end_lineno=35, end_col_offset=25, id='_', ctx=Load()),
                                                        args=[
                                                            Constant(lineno=35, col_offset=26, end_lineno=35, end_col_offset=47, value='Repair orders of %s', kind=None),
                                                            Attribute(
                                                                lineno=35,
                                                                col_offset=49,
                                                                end_lineno=35,
                                                                end_col_offset=58,
                                                                value=Name(lineno=35, col_offset=49, end_lineno=35, end_col_offset=53, id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        lineno=36,
                                                        col_offset=26,
                                                        end_lineno=36,
                                                        end_col_offset=67,
                                                        elts=[
                                                            Tuple(
                                                                lineno=36,
                                                                col_offset=27,
                                                                end_lineno=36,
                                                                end_col_offset=66,
                                                                elts=[
                                                                    Constant(lineno=36, col_offset=28, end_lineno=36, end_col_offset=32, value='id', kind=None),
                                                                    Constant(lineno=36, col_offset=34, end_lineno=36, end_col_offset=38, value='in', kind=None),
                                                                    Attribute(
                                                                        lineno=36,
                                                                        col_offset=40,
                                                                        end_lineno=36,
                                                                        end_col_offset=65,
                                                                        value=Attribute(
                                                                            lineno=36,
                                                                            col_offset=40,
                                                                            end_lineno=36,
                                                                            end_col_offset=61,
                                                                            value=Name(lineno=36, col_offset=40, end_lineno=36, end_col_offset=44, id='self', ctx=Load()),
                                                                            attr='repair_order_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(lineno=37, col_offset=29, end_lineno=37, end_col_offset=40, value='tree,form', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=21,
                            value=Name(lineno=39, col_offset=15, end_lineno=39, end_col_offset=21, id='action', ctx=Load()),
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