Module(
    body=[
        Import(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=9,
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
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
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=43,
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=30,
            end_col_offset=41,
            name='PrintPreNumberedChecks',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=29,
                    end_lineno=9,
                    end_col_offset=50,
                    value=Name(lineno=9, col_offset=29, end_lineno=9, end_col_offset=35, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=38,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=38, value='print.prenumbered.checks', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=46,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=46, value='Print Pre-numbered Checks', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=71,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=21, id='next_check_number', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=24,
                        end_lineno=13,
                        end_col_offset=71,
                        func=Attribute(
                            lineno=13,
                            col_offset=24,
                            end_lineno=13,
                            end_col_offset=35,
                            value=Name(lineno=13, col_offset=24, end_lineno=13, end_col_offset=30, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=13, col_offset=36, end_lineno=13, end_col_offset=55, value='Next Check Number', kind=None)],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=57,
                                end_lineno=13,
                                end_col_offset=70,
                                arg='required',
                                value=Constant(lineno=13, col_offset=66, end_lineno=13, end_col_offset=70, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=16,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=91,
                    name='_check_next_check_number',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=16, col_offset=33, end_lineno=16, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            lineno=17,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=91,
                            target=Name(lineno=17, col_offset=12, end_lineno=17, end_col_offset=17, id='check', ctx=Store()),
                            iter=Name(lineno=17, col_offset=21, end_lineno=17, end_col_offset=25, id='self', ctx=Load()),
                            body=[
                                If(
                                    lineno=18,
                                    col_offset=12,
                                    end_lineno=19,
                                    end_col_offset=91,
                                    test=BoolOp(
                                        lineno=18,
                                        col_offset=15,
                                        end_lineno=18,
                                        end_col_offset=93,
                                        op=And(),
                                        values=[
                                            Attribute(
                                                lineno=18,
                                                col_offset=15,
                                                end_lineno=18,
                                                end_col_offset=38,
                                                value=Name(lineno=18, col_offset=15, end_lineno=18, end_col_offset=20, id='check', ctx=Load()),
                                                attr='next_check_number',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                lineno=18,
                                                col_offset=43,
                                                end_lineno=18,
                                                end_col_offset=93,
                                                op=Not(),
                                                operand=Call(
                                                    lineno=18,
                                                    col_offset=47,
                                                    end_lineno=18,
                                                    end_col_offset=93,
                                                    func=Attribute(
                                                        lineno=18,
                                                        col_offset=47,
                                                        end_lineno=18,
                                                        end_col_offset=55,
                                                        value=Name(lineno=18, col_offset=47, end_lineno=18, end_col_offset=49, id='re', ctx=Load()),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(lineno=18, col_offset=56, end_lineno=18, end_col_offset=67, value='^[0-9]+$', kind=None),
                                                        Attribute(
                                                            lineno=18,
                                                            col_offset=69,
                                                            end_lineno=18,
                                                            end_col_offset=92,
                                                            value=Name(lineno=18, col_offset=69, end_lineno=18, end_col_offset=74, id='check', ctx=Load()),
                                                            attr='next_check_number',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            lineno=19,
                                            col_offset=16,
                                            end_lineno=19,
                                            end_col_offset=91,
                                            exc=Call(
                                                lineno=19,
                                                col_offset=22,
                                                end_lineno=19,
                                                end_col_offset=91,
                                                func=Name(lineno=19, col_offset=22, end_lineno=19, end_col_offset=37, id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        lineno=19,
                                                        col_offset=38,
                                                        end_lineno=19,
                                                        end_col_offset=90,
                                                        func=Name(lineno=19, col_offset=38, end_lineno=19, end_col_offset=39, id='_', ctx=Load()),
                                                        args=[Constant(lineno=19, col_offset=40, end_lineno=19, end_col_offset=89, value='Next Check Number should only contains numbers.', kind=None)],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=15,
                            col_offset=5,
                            end_lineno=15,
                            end_col_offset=40,
                            func=Attribute(
                                lineno=15,
                                col_offset=5,
                                end_lineno=15,
                                end_col_offset=19,
                                value=Name(lineno=15, col_offset=5, end_lineno=15, end_col_offset=8, id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(lineno=15, col_offset=20, end_lineno=15, end_col_offset=39, value='next_check_number', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=41,
                    name='print_checks',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=21, end_lineno=21, end_col_offset=25, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=50,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=20, id='check_number', ctx=Store())],
                            value=Call(
                                lineno=22,
                                col_offset=23,
                                end_lineno=22,
                                end_col_offset=50,
                                func=Name(lineno=22, col_offset=23, end_lineno=22, end_col_offset=26, id='int', ctx=Load()),
                                args=[
                                    Attribute(
                                        lineno=22,
                                        col_offset=27,
                                        end_lineno=22,
                                        end_col_offset=49,
                                        value=Name(lineno=22, col_offset=27, end_lineno=22, end_col_offset=31, id='self', ctx=Load()),
                                        attr='next_check_number',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=23,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=54,
                            targets=[Name(lineno=23, col_offset=8, end_lineno=23, end_col_offset=18, id='number_len', ctx=Store())],
                            value=Call(
                                lineno=23,
                                col_offset=21,
                                end_lineno=23,
                                end_col_offset=54,
                                func=Name(lineno=23, col_offset=21, end_lineno=23, end_col_offset=24, id='len', ctx=Load()),
                                args=[
                                    BoolOp(
                                        lineno=23,
                                        col_offset=25,
                                        end_lineno=23,
                                        end_col_offset=53,
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                lineno=23,
                                                col_offset=25,
                                                end_lineno=23,
                                                end_col_offset=47,
                                                value=Name(lineno=23, col_offset=25, end_lineno=23, end_col_offset=29, id='self', ctx=Load()),
                                                attr='next_check_number',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=23, col_offset=51, end_lineno=23, end_col_offset=53, value='', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=86,
                            targets=[Name(lineno=24, col_offset=8, end_lineno=24, end_col_offset=16, id='payments', ctx=Store())],
                            value=Call(
                                lineno=24,
                                col_offset=19,
                                end_lineno=24,
                                end_col_offset=86,
                                func=Attribute(
                                    lineno=24,
                                    col_offset=19,
                                    end_lineno=24,
                                    end_col_offset=53,
                                    value=Subscript(
                                        lineno=24,
                                        col_offset=19,
                                        end_lineno=24,
                                        end_col_offset=46,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=19,
                                            end_lineno=24,
                                            end_col_offset=27,
                                            value=Name(lineno=24, col_offset=19, end_lineno=24, end_col_offset=23, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=24, col_offset=28, end_lineno=24, end_col_offset=45, value='account.payment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=24,
                                        col_offset=54,
                                        end_lineno=24,
                                        end_col_offset=85,
                                        value=Attribute(
                                            lineno=24,
                                            col_offset=54,
                                            end_lineno=24,
                                            end_col_offset=70,
                                            value=Attribute(
                                                lineno=24,
                                                col_offset=54,
                                                end_lineno=24,
                                                end_col_offset=62,
                                                value=Name(lineno=24, col_offset=54, end_lineno=24, end_col_offset=58, id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=24, col_offset=71, end_lineno=24, end_col_offset=84, value='payment_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=69,
                            value=Call(
                                lineno=25,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=69,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=67,
                                    value=Call(
                                        lineno=25,
                                        col_offset=8,
                                        end_lineno=25,
                                        end_col_offset=55,
                                        func=Attribute(
                                            lineno=25,
                                            col_offset=8,
                                            end_lineno=25,
                                            end_col_offset=25,
                                            value=Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=16, id='payments', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                lineno=25,
                                                col_offset=26,
                                                end_lineno=25,
                                                end_col_offset=54,
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(lineno=25, col_offset=33, end_lineno=25, end_col_offset=34, arg='r', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    lineno=25,
                                                    col_offset=36,
                                                    end_lineno=25,
                                                    end_col_offset=54,
                                                    left=Attribute(
                                                        lineno=25,
                                                        col_offset=36,
                                                        end_lineno=25,
                                                        end_col_offset=43,
                                                        value=Name(lineno=25, col_offset=36, end_lineno=25, end_col_offset=37, id='r', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(lineno=25, col_offset=47, end_lineno=25, end_col_offset=54, value='draft', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=109,
                            value=Call(
                                lineno=26,
                                col_offset=8,
                                end_lineno=26,
                                end_col_offset=109,
                                func=Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=85,
                                    value=Call(
                                        lineno=26,
                                        col_offset=8,
                                        end_lineno=26,
                                        end_col_offset=79,
                                        func=Attribute(
                                            lineno=26,
                                            col_offset=8,
                                            end_lineno=26,
                                            end_col_offset=25,
                                            value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=16, id='payments', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                lineno=26,
                                                col_offset=26,
                                                end_lineno=26,
                                                end_col_offset=78,
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(lineno=26, col_offset=33, end_lineno=26, end_col_offset=34, arg='r', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    lineno=26,
                                                    col_offset=36,
                                                    end_lineno=26,
                                                    end_col_offset=78,
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            lineno=26,
                                                            col_offset=36,
                                                            end_lineno=26,
                                                            end_col_offset=55,
                                                            left=Attribute(
                                                                lineno=26,
                                                                col_offset=36,
                                                                end_lineno=26,
                                                                end_col_offset=43,
                                                                value=Name(lineno=26, col_offset=36, end_lineno=26, end_col_offset=37, id='r', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(lineno=26, col_offset=47, end_lineno=26, end_col_offset=55, value='posted', kind=None)],
                                                        ),
                                                        UnaryOp(
                                                            lineno=26,
                                                            col_offset=60,
                                                            end_lineno=26,
                                                            end_col_offset=78,
                                                            op=Not(),
                                                            operand=Attribute(
                                                                lineno=26,
                                                                col_offset=64,
                                                                end_lineno=26,
                                                                end_col_offset=78,
                                                                value=Name(lineno=26, col_offset=64, end_lineno=26, end_col_offset=65, id='r', ctx=Load()),
                                                                attr='is_move_sent',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=26,
                                        col_offset=86,
                                        end_lineno=26,
                                        end_col_offset=108,
                                        keys=[Constant(lineno=26, col_offset=87, end_lineno=26, end_col_offset=101, value='is_move_sent', kind=None)],
                                        values=[Constant(lineno=26, col_offset=103, end_lineno=26, end_col_offset=107, value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            lineno=27,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=29,
                            target=Name(lineno=27, col_offset=12, end_lineno=27, end_col_offset=19, id='payment', ctx=Store()),
                            iter=Name(lineno=27, col_offset=23, end_lineno=27, end_col_offset=31, id='payments', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=28,
                                    col_offset=12,
                                    end_lineno=28,
                                    end_col_offset=76,
                                    targets=[
                                        Attribute(
                                            lineno=28,
                                            col_offset=12,
                                            end_lineno=28,
                                            end_col_offset=32,
                                            value=Name(lineno=28, col_offset=12, end_lineno=28, end_col_offset=19, id='payment', ctx=Load()),
                                            attr='check_number',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        lineno=28,
                                        col_offset=35,
                                        end_lineno=28,
                                        end_col_offset=76,
                                        left=Call(
                                            lineno=28,
                                            col_offset=35,
                                            end_lineno=28,
                                            end_col_offset=61,
                                            func=Attribute(
                                                lineno=28,
                                                col_offset=35,
                                                end_lineno=28,
                                                end_col_offset=49,
                                                value=Constant(lineno=28, col_offset=35, end_lineno=28, end_col_offset=42, value='%0{}d', kind=None),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[Name(lineno=28, col_offset=50, end_lineno=28, end_col_offset=60, id='number_len', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Name(lineno=28, col_offset=64, end_lineno=28, end_col_offset=76, id='check_number', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    lineno=29,
                                    col_offset=12,
                                    end_lineno=29,
                                    end_col_offset=29,
                                    target=Name(lineno=29, col_offset=12, end_lineno=29, end_col_offset=24, id='check_number', ctx=Store()),
                                    op=Add(),
                                    value=Constant(lineno=29, col_offset=28, end_lineno=29, end_col_offset=29, value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=41,
                            value=Call(
                                lineno=30,
                                col_offset=15,
                                end_lineno=30,
                                end_col_offset=41,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=15,
                                    end_lineno=30,
                                    end_col_offset=39,
                                    value=Name(lineno=30, col_offset=15, end_lineno=30, end_col_offset=23, id='payments', ctx=Load()),
                                    attr='do_print_checks',
                                    ctx=Load(),
                                ),
                                args=[],
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