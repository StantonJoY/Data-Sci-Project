Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=38,
            end_col_offset=9,
            name='PosOpenStatement',
            bases=[
                Attribute(
                    lineno=8,
                    col_offset=23,
                    end_lineno=8,
                    end_col_offset=44,
                    value=Name(lineno=8, col_offset=23, end_lineno=8, end_col_offset=29, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=32,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=32, value='pos.open.statement', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=49,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=10, col_offset=19, end_lineno=10, end_col_offset=49, value='Point of Sale Open Statement', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=38,
                    end_col_offset=9,
                    name='open_statement',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=12, col_offset=23, end_lineno=12, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=25,
                            value=Call(
                                lineno=13,
                                col_offset=8,
                                end_lineno=13,
                                end_col_offset=25,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=8,
                                    end_lineno=13,
                                    end_col_offset=23,
                                    value=Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=12, id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=58,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=21, id='BankStatement', ctx=Store())],
                            value=Subscript(
                                lineno=14,
                                col_offset=24,
                                end_lineno=14,
                                end_col_offset=58,
                                value=Attribute(
                                    lineno=14,
                                    col_offset=24,
                                    end_lineno=14,
                                    end_col_offset=32,
                                    value=Name(lineno=14, col_offset=24, end_lineno=14, end_col_offset=28, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=14, col_offset=33, end_lineno=14, end_col_offset=57, value='account.bank.statement', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=84,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=16, id='journals', ctx=Store())],
                            value=Call(
                                lineno=15,
                                col_offset=19,
                                end_lineno=15,
                                end_col_offset=84,
                                func=Attribute(
                                    lineno=15,
                                    col_offset=19,
                                    end_lineno=15,
                                    end_col_offset=53,
                                    value=Subscript(
                                        lineno=15,
                                        col_offset=19,
                                        end_lineno=15,
                                        end_col_offset=46,
                                        value=Attribute(
                                            lineno=15,
                                            col_offset=19,
                                            end_lineno=15,
                                            end_col_offset=27,
                                            value=Name(lineno=15, col_offset=19, end_lineno=15, end_col_offset=23, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=15, col_offset=28, end_lineno=15, end_col_offset=45, value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        lineno=15,
                                        col_offset=54,
                                        end_lineno=15,
                                        end_col_offset=83,
                                        elts=[
                                            Tuple(
                                                lineno=15,
                                                col_offset=55,
                                                end_lineno=15,
                                                end_col_offset=82,
                                                elts=[
                                                    Constant(lineno=15, col_offset=56, end_lineno=15, end_col_offset=70, value='journal_user', kind=None),
                                                    Constant(lineno=15, col_offset=72, end_lineno=15, end_col_offset=75, value='=', kind=None),
                                                    Constant(lineno=15, col_offset=77, end_lineno=15, end_col_offset=81, value=True, kind=None),
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
                            lineno=16,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=402,
                            test=UnaryOp(
                                lineno=16,
                                col_offset=11,
                                end_lineno=16,
                                end_col_offset=23,
                                op=Not(),
                                operand=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=23, id='journals', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=17,
                                    end_col_offset=402,
                                    exc=Call(
                                        lineno=17,
                                        col_offset=18,
                                        end_lineno=17,
                                        end_col_offset=402,
                                        func=Name(lineno=17, col_offset=18, end_lineno=17, end_col_offset=27, id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=17,
                                                col_offset=28,
                                                end_lineno=17,
                                                end_col_offset=401,
                                                func=Name(lineno=17, col_offset=28, end_lineno=17, end_col_offset=29, id='_', ctx=Load()),
                                                args=[Constant(lineno=17, col_offset=30, end_lineno=17, end_col_offset=400, value='You have to define which payment method must be available in the point of sale by reusing existing bank and cash through "Accounting / Configuration / Journals / Journals". Select a journal and check the field "PoS Payment Method" from the "Point of Sale" tab. You can also create new payment methods directly from menu "PoS Backend / Configuration / Payment Methods".', kind=None)],
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
                        For(
                            lineno=19,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=118,
                            target=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=19, id='journal', ctx=Store()),
                            iter=Name(lineno=19, col_offset=23, end_lineno=19, end_col_offset=31, id='journals', ctx=Load()),
                            body=[
                                If(
                                    lineno=20,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=72,
                                    test=Attribute(
                                        lineno=20,
                                        col_offset=15,
                                        end_lineno=20,
                                        end_col_offset=34,
                                        value=Name(lineno=20, col_offset=15, end_lineno=20, end_col_offset=22, id='journal', ctx=Load()),
                                        attr='sequence_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            lineno=21,
                                            col_offset=16,
                                            end_lineno=21,
                                            end_col_offset=57,
                                            targets=[Name(lineno=21, col_offset=16, end_lineno=21, end_col_offset=22, id='number', ctx=Store())],
                                            value=Call(
                                                lineno=21,
                                                col_offset=25,
                                                end_lineno=21,
                                                end_col_offset=57,
                                                func=Attribute(
                                                    lineno=21,
                                                    col_offset=25,
                                                    end_lineno=21,
                                                    end_col_offset=55,
                                                    value=Attribute(
                                                        lineno=21,
                                                        col_offset=25,
                                                        end_lineno=21,
                                                        end_col_offset=44,
                                                        value=Name(lineno=21, col_offset=25, end_lineno=21, end_col_offset=32, id='journal', ctx=Load()),
                                                        attr='sequence_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='next_by_id',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            lineno=23,
                                            col_offset=16,
                                            end_lineno=23,
                                            end_col_offset=72,
                                            exc=Call(
                                                lineno=23,
                                                col_offset=22,
                                                end_lineno=23,
                                                end_col_offset=72,
                                                func=Name(lineno=23, col_offset=22, end_lineno=23, end_col_offset=31, id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        lineno=23,
                                                        col_offset=32,
                                                        end_lineno=23,
                                                        end_col_offset=71,
                                                        func=Name(lineno=23, col_offset=32, end_lineno=23, end_col_offset=33, id='_', ctx=Load()),
                                                        args=[Constant(lineno=23, col_offset=34, end_lineno=23, end_col_offset=70, value='No sequence defined on the journal', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    lineno=24,
                                    col_offset=12,
                                    end_lineno=24,
                                    end_col_offset=118,
                                    target=Name(lineno=24, col_offset=12, end_lineno=24, end_col_offset=25, id='BankStatement', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        lineno=24,
                                        col_offset=29,
                                        end_lineno=24,
                                        end_col_offset=118,
                                        func=Attribute(
                                            lineno=24,
                                            col_offset=29,
                                            end_lineno=24,
                                            end_col_offset=49,
                                            value=Name(lineno=24, col_offset=29, end_lineno=24, end_col_offset=42, id='BankStatement', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=24,
                                                col_offset=50,
                                                end_lineno=24,
                                                end_col_offset=117,
                                                keys=[
                                                    Constant(lineno=24, col_offset=51, end_lineno=24, end_col_offset=63, value='journal_id', kind=None),
                                                    Constant(lineno=24, col_offset=77, end_lineno=24, end_col_offset=86, value='user_id', kind=None),
                                                    Constant(lineno=24, col_offset=102, end_lineno=24, end_col_offset=108, value='name', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        lineno=24,
                                                        col_offset=65,
                                                        end_lineno=24,
                                                        end_col_offset=75,
                                                        value=Name(lineno=24, col_offset=65, end_lineno=24, end_col_offset=72, id='journal', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        lineno=24,
                                                        col_offset=88,
                                                        end_lineno=24,
                                                        end_col_offset=100,
                                                        value=Attribute(
                                                            lineno=24,
                                                            col_offset=88,
                                                            end_lineno=24,
                                                            end_col_offset=96,
                                                            value=Name(lineno=24, col_offset=88, end_lineno=24, end_col_offset=92, id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Name(lineno=24, col_offset=110, end_lineno=24, end_col_offset=116, id='number', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=69,
                            targets=[Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=15, id='tree_id', ctx=Store())],
                            value=Attribute(
                                lineno=26,
                                col_offset=18,
                                end_lineno=26,
                                end_col_offset=69,
                                value=Call(
                                    lineno=26,
                                    col_offset=18,
                                    end_lineno=26,
                                    end_col_offset=66,
                                    func=Attribute(
                                        lineno=26,
                                        col_offset=18,
                                        end_lineno=26,
                                        end_col_offset=30,
                                        value=Attribute(
                                            lineno=26,
                                            col_offset=18,
                                            end_lineno=26,
                                            end_col_offset=26,
                                            value=Name(lineno=26, col_offset=18, end_lineno=26, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=26, col_offset=31, end_lineno=26, end_col_offset=65, value='account.view_bank_statement_tree', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=69,
                            targets=[Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=15, id='form_id', ctx=Store())],
                            value=Attribute(
                                lineno=27,
                                col_offset=18,
                                end_lineno=27,
                                end_col_offset=69,
                                value=Call(
                                    lineno=27,
                                    col_offset=18,
                                    end_lineno=27,
                                    end_col_offset=66,
                                    func=Attribute(
                                        lineno=27,
                                        col_offset=18,
                                        end_lineno=27,
                                        end_col_offset=30,
                                        value=Attribute(
                                            lineno=27,
                                            col_offset=18,
                                            end_lineno=27,
                                            end_col_offset=26,
                                            value=Name(lineno=27, col_offset=18, end_lineno=27, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=27, col_offset=31, end_lineno=27, end_col_offset=65, value='account.view_bank_statement_form', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=28,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=73,
                            targets=[Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=17, id='search_id', ctx=Store())],
                            value=Attribute(
                                lineno=28,
                                col_offset=20,
                                end_lineno=28,
                                end_col_offset=73,
                                value=Call(
                                    lineno=28,
                                    col_offset=20,
                                    end_lineno=28,
                                    end_col_offset=70,
                                    func=Attribute(
                                        lineno=28,
                                        col_offset=20,
                                        end_lineno=28,
                                        end_col_offset=32,
                                        value=Attribute(
                                            lineno=28,
                                            col_offset=20,
                                            end_lineno=28,
                                            end_col_offset=28,
                                            value=Name(lineno=28, col_offset=20, end_lineno=28, end_col_offset=24, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(lineno=28, col_offset=33, end_lineno=28, end_col_offset=69, value='account.view_bank_statement_search', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            lineno=30,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=9,
                            value=Dict(
                                lineno=30,
                                col_offset=15,
                                end_lineno=38,
                                end_col_offset=9,
                                keys=[
                                    Constant(lineno=31, col_offset=12, end_lineno=31, end_col_offset=18, value='type', kind=None),
                                    Constant(lineno=32, col_offset=12, end_lineno=32, end_col_offset=18, value='name', kind=None),
                                    Constant(lineno=33, col_offset=12, end_lineno=33, end_col_offset=23, value='view_mode', kind=None),
                                    Constant(lineno=34, col_offset=12, end_lineno=34, end_col_offset=23, value='res_model', kind=None),
                                    Constant(lineno=35, col_offset=12, end_lineno=35, end_col_offset=20, value='domain', kind=None),
                                    Constant(lineno=36, col_offset=12, end_lineno=36, end_col_offset=19, value='views', kind=None),
                                    Constant(lineno=37, col_offset=12, end_lineno=37, end_col_offset=28, value='search_view_id', kind=None),
                                ],
                                values=[
                                    Constant(lineno=31, col_offset=20, end_lineno=31, end_col_offset=43, value='ir.actions.act_window', kind=None),
                                    Call(
                                        lineno=32,
                                        col_offset=20,
                                        end_lineno=32,
                                        end_col_offset=47,
                                        func=Name(lineno=32, col_offset=20, end_lineno=32, end_col_offset=21, id='_', ctx=Load()),
                                        args=[Constant(lineno=32, col_offset=22, end_lineno=32, end_col_offset=46, value='List of Cash Registers', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(lineno=33, col_offset=25, end_lineno=33, end_col_offset=36, value='tree,form', kind=None),
                                    Constant(lineno=34, col_offset=25, end_lineno=34, end_col_offset=49, value='account.bank.statement', kind=None),
                                    Call(
                                        lineno=35,
                                        col_offset=22,
                                        end_lineno=35,
                                        end_col_offset=60,
                                        func=Name(lineno=35, col_offset=22, end_lineno=35, end_col_offset=25, id='str', ctx=Load()),
                                        args=[
                                            List(
                                                lineno=35,
                                                col_offset=26,
                                                end_lineno=35,
                                                end_col_offset=59,
                                                elts=[
                                                    Tuple(
                                                        lineno=35,
                                                        col_offset=27,
                                                        end_lineno=35,
                                                        end_col_offset=58,
                                                        elts=[
                                                            Constant(lineno=35, col_offset=28, end_lineno=35, end_col_offset=32, value='id', kind=None),
                                                            Constant(lineno=35, col_offset=34, end_lineno=35, end_col_offset=38, value='in', kind=None),
                                                            Attribute(
                                                                lineno=35,
                                                                col_offset=40,
                                                                end_lineno=35,
                                                                end_col_offset=57,
                                                                value=Name(lineno=35, col_offset=40, end_lineno=35, end_col_offset=53, id='BankStatement', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
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
                                    List(
                                        lineno=36,
                                        col_offset=21,
                                        end_lineno=36,
                                        end_col_offset=59,
                                        elts=[
                                            Tuple(
                                                lineno=36,
                                                col_offset=22,
                                                end_lineno=36,
                                                end_col_offset=39,
                                                elts=[
                                                    Name(lineno=36, col_offset=23, end_lineno=36, end_col_offset=30, id='tree_id', ctx=Load()),
                                                    Constant(lineno=36, col_offset=32, end_lineno=36, end_col_offset=38, value='tree', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=36,
                                                col_offset=41,
                                                end_lineno=36,
                                                end_col_offset=58,
                                                elts=[
                                                    Name(lineno=36, col_offset=42, end_lineno=36, end_col_offset=49, id='form_id', ctx=Load()),
                                                    Constant(lineno=36, col_offset=51, end_lineno=36, end_col_offset=57, value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        lineno=37,
                                        col_offset=30,
                                        end_lineno=37,
                                        end_col_offset=41,
                                        elts=[Name(lineno=37, col_offset=31, end_lineno=37, end_col_offset=40, id='search_id', ctx=Load())],
                                        ctx=Load(),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)