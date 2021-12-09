Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.point_of_sale.tests.common',
            names=[alias(name='TestPoSCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPosSimpleInvoicedOrders',
            bases=[Name(id='TestPoSCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Each test case only make a single **invoiced** order.\n    Name of each test corresponds to a sheet in: https://docs.google.com/spreadsheets/d/1mt2jRSDU7OONPBFjwyTcnhRjITQI8rGMLLQA5K3fAjo/edit?usp=sharing\n    ', kind=None),
                ),
                FunctionDef(
                    name='setUp',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestPosSimpleInvoicedOrders', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='config',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='basic_config',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product100',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_product',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Product_100', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='categ_basic',
                                        ctx=Load(),
                                    ),
                                    Constant(value=100, kind=None),
                                    Constant(value=50, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cash_pm1',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=100, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_02b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_pm1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='journal_id', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='config',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='invoice_journal_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='journal_id', kind=None),
                                                                                    Constant(value='line_ids', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='config',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='journal_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='journal_id', kind=None),
                                                            Constant(value='line_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='config',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='journal_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=100, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='journal_id', kind=None),
                                                                            Constant(value='line_ids', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='journal_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_03b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='journal_id', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='config',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='invoice_journal_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_04b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_split_pm1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='journal_id', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='config',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='invoice_journal_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='journal_id', kind=None),
                                                                                    Constant(value='line_ids', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='config',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='journal_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='journal_id', kind=None),
                                                            Constant(value='line_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='config',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='journal_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=100, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='journal_id', kind=None),
                                                                            Constant(value='line_ids', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='journal_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_split_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_05b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cash_split_pm1',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=100, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_split_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_10b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=100, kind=None),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_11b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cash_pm1',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bank_pm1',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=100, kind=None),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_12b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_split_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=100, kind=None),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_split_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_13b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cash_pm1',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bank_split_pm1',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=100, kind=None),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                    Constant(value='amount_residual', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_split_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_14b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cash_pm1',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=100, kind=None),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=100, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_15b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_pm1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=100, kind=None),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_16b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bank_split_pm1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=100, kind=None),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_split_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_17b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cash_split_pm1',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=200, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=200, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=100, kind=None),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=100, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=200, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=100, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=200, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_split_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=200, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=100, kind=None),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_split_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=100, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_18b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=50, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='cash_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_19b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cash_pm1',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bank_pm1',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='receivable_account_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=50, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='receivable_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_20b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cash_pm1',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bank_split_pm1',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='bank_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=50, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='bank_split_pm1',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='outstanding_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_21b',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='payment_methods', kind=None),
                                            Constant(value='orders', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='journal_entries_after_closing', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cash_split_pm1',
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pay_later_pm',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='customer', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product100',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='cash_split_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='pay_later_pm',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='00100-010-0001', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='account_id', kind=None),
                                                                                    Constant(value='partner_id', kind=None),
                                                                                    Constant(value='debit', kind=None),
                                                                                    Constant(value='credit', kind=None),
                                                                                    Constant(value='reconciled', kind=None),
                                                                                    Constant(value='amount_residual', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='c1_receivable',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=100, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=False, kind=None),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='cash_split_pm1',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=50, kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='line_ids', kind=None)],
                                                                                values=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='c1_receivable',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=True, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='account_id', kind=None),
                                                                                                    Constant(value='partner_id', kind=None),
                                                                                                    Constant(value='debit', kind=None),
                                                                                                    Constant(value='credit', kind=None),
                                                                                                    Constant(value='reconciled', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='pos_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=50, kind=None),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='session_journal_entry', kind=None),
                                                    Constant(value='cash_statement', kind=None),
                                                    Constant(value='bank_payments', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='line_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='c1_receivable',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='customer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                            Constant(value='debit', kind=None),
                                                                            Constant(value='credit', kind=None),
                                                                            Constant(value='reconciled', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=50, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[Constant(value=50, kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Dict(
                                                                        keys=[Constant(value='line_ids', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='cash_split_pm1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='journal_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='default_account_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='account_id', kind=None),
                                                                                            Constant(value='partner_id', kind=None),
                                                                                            Constant(value='debit', kind=None),
                                                                                            Constant(value='credit', kind=None),
                                                                                            Constant(value='reconciled', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='c1_receivable',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='customer',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                            Constant(value=50, kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
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
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
