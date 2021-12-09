Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.point_of_sale.tests.common',
            names=[alias(name='TestPoSCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPoSProductsWithTax',
            bases=[Name(id='TestPoSCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test normal configuration PoS selling products with tax\n    ', kind=None),
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
                                            Name(id='TestPoSProductsWithTax', ctx=Load()),
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
                                    attr='product1',
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
                                    Constant(value='Product 1', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='categ_basic',
                                        ctx=Load(),
                                    ),
                                    Constant(value=10.0, kind=None),
                                    Constant(value=5.0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tax_ids',
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='taxes',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='tax7', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product2',
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
                                    Constant(value='Product 2', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='categ_basic',
                                        ctx=Load(),
                                    ),
                                    Constant(value=20.0, kind=None),
                                    Constant(value=10.0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tax_ids',
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='taxes',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='tax10', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product3',
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
                                    Constant(value='Product 3', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='categ_basic',
                                        ctx=Load(),
                                    ),
                                    Constant(value=30.0, kind=None),
                                    Constant(value=15.0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tax_ids',
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='taxes',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='tax_group_7_10', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='adjust_inventory',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product3',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=100, kind=None),
                                            Constant(value=50, kind=None),
                                            Constant(value=50, kind=None),
                                        ],
                                        ctx=Load(),
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
                    name='test_orders_no_invoiced',
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
                            value=Constant(value=' Test for orders without invoice\n\n        Orders\n        ======\n        +---------+----------+-----------+----------+-----+---------+-----------------------+--------+\n        | order   | payments | invoiced? | product  | qty | untaxed | tax                   |  total |\n        +---------+----------+-----------+----------+-----+---------+-----------------------+--------+\n        | order 1 | cash     | no        | product1 |  10 |     100 | 7                     |    107 |\n        |         |          |           | product2 |   5 |   90.91 | 9.09                  |    100 |\n        +---------+----------+-----------+----------+-----+---------+-----------------------+--------+\n        | order 2 | cash     | no        | product2 |   7 |  127.27 | 12.73                 |    140 |\n        |         |          |           | product3 |   4 |  109.09 | 10.91[10%] + 7.64[7%] | 127.64 |\n        +---------+----------+-----------+----------+-----+---------+-----------------------+--------+\n        | order 3 | bank     | no        | product1 |   1 |      10 | 0.7                   |   10.7 |\n        |         |          |           | product2 |   3 |   54.55 | 5.45                  |     60 |\n        |         |          |           | product3 |   5 |  136.36 | 13.64[10%] + 9.55[7%] | 159.55 |\n        +---------+----------+-----------+----------+-----+---------+-----------------------+--------+\n\n        Calculated taxes\n        ================\n            total tax 7% only + group tax (10+7%)\n                (7 + 0.7) + (7.64 + 9.55) = 7.7 + 17.19 = 24.89\n            total tax 10% only + group tax (10+7%)\n                (9.09 + 12.73 + 5.45) + (10.91 + 13.64) = 27.27 + 24.55 = 51.82\n\n        Thus, manually_calculated_taxes = (-24,89, -51.82)\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_before_closing_cb',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=3, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='orders_total', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='amount_total',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='pos_session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='order_ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='orders_total', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='total_payments_amount',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Total order amount should be equal to the total payment amount.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
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
                                            Constant(value='before_closing_cb', kind=None),
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
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=10, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=7, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product3',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=4, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0002', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product3',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=3, kind=None),
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
                                                                            Constant(value=230.25, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0003', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='_before_closing_cb', ctx=Load()),
                                            Dict(keys=[], values=[]),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=24.89, kind=None),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=51.82, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=110, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=272.73, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=245.45, kind=None),
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
                                                                            Constant(value=230.25, kind=None),
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
                                                                            Constant(value=474.64, kind=None),
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
                                                                        elts=[Constant(value=474.64, kind=None)],
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
                                                                                            Constant(value=474.64, kind=None),
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
                                                                                            Constant(value=474.64, kind=None),
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
                                                                        elts=[Constant(value=230.25, kind=None)],
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
                                                                                            Constant(value=230.25, kind=None),
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
                                                                                            Constant(value=230.25, kind=None),
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
                    name='test_orders_with_invoiced',
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
                            value=Constant(value=' Test for orders: one with invoice\n\n        Orders\n        ======\n        +---------+----------+---------------+----------+-----+---------+---------------+--------+\n        | order   | payments | invoiced?     | product  | qty | untaxed | tax           |  total |\n        +---------+----------+---------------+----------+-----+---------+---------------+--------+\n        | order 1 | cash     | no            | product1 |   6 |      60 | 4.2           |   64.2 |\n        |         |          |               | product2 |   3 |   54.55 | 5.45          |     60 |\n        |         |          |               | product3 |   1 |   27.27 | 2.73 + 1.91   |  31.91 |\n        +---------+----------+---------------+----------+-----+---------+---------------+--------+\n        | order 2 | bank     | no            | product1 |   1 |      10 | 0.7           |   10.7 |\n        |         |          |               | product2 |  20 |  363.64 | 36.36         |    400 |\n        +---------+----------+---------------+----------+-----+---------+---------------+--------+\n        | order 3 | bank     | yes, customer | product1 |  10 |     100 | 7             |    107 |\n        |         |          |               | product3 |  10 |  272.73 | 27.27 + 19.09 | 319.09 |\n        +---------+----------+---------------+----------+-----+---------+---------------+--------+\n\n        Calculated taxes\n        ================\n            total tax 7% only\n                4.2 + 0.7 => 4.9 + 1.91 = 6.81\n            total tax 10% only\n                5.45 + 36.36 => 41.81 + 2.73 = 44.54\n\n        Thus, manually_calculated_taxes = (-6.81, -44.54)\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_before_closing_cb',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=3, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='orders_total', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='amount_total',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='pos_session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='order_ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='orders_total', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='total_payments_amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Total order amount should be equal to the total payment amount.', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='invoiced_order', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='order', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Constant(value='09876-098-0987', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='pos_reference',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='invoiced_order', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='Only one order is invoiced in this test.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='invoiced_order', ctx=Load()),
                                        attr='account_move',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='amount_total',
                                                ctx=Load(),
                                            ),
                                            Constant(value=426.09, kind=None),
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
                            name='_after_closing_cb',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[Name(id='session_move', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pos_session',
                                            ctx=Load(),
                                        ),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='session_move', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_received_account',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='manually_calculated_taxes', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=6.81, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=44.54, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[Name(id='manually_calculated_taxes', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='t1', ctx=Store()),
                                            Name(id='t2', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='manually_calculated_taxes', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertAlmostEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='t1', ctx=Load()),
                                                    Name(id='t2', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='msg',
                                                        value=Constant(value='Taxes should be correctly combined.', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='base_amounts', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=97.27, kind=None),
                                            Constant(value=445.46, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[Name(id='base_amounts', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='tax_base_amount', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                            Constant(value='before_closing_cb', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='after_closing_cb', kind=None),
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
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product3',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=6, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=3, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='uid', kind=None),
                                                        ],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=20, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product1',
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
                                                                            Constant(value=410.7, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0002', kind=None),
                                                        ],
                                                    ),
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
                                                                                attr='product1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=10, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product3',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=10, kind=None),
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
                                                                            Constant(value=426.09, kind=None),
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
                                                            Constant(value='09876-098-0987', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='_before_closing_cb', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='09876-098-0987', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='payments', kind=None)],
                                                        values=[
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
                                                                                    Constant(value=426.09, kind=None),
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
                                                                                                    Constant(value=426.09, kind=None),
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
                                                                                                    Constant(value=426.09, kind=None),
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
                                            Name(id='_after_closing_cb', ctx=Load()),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=6.81, kind=None),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=44.54, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=27.27, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=70, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=418.19, kind=None),
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
                                                                            Constant(value=836.79, kind=None),
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
                                                                            Constant(value=156.11, kind=None),
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
                                                                            Constant(value=426.09, kind=None),
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
                                                                        elts=[Constant(value=156.11, kind=None)],
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
                                                                                            Constant(value=156.11, kind=None),
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
                                                                                            Constant(value=156.11, kind=None),
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
                                                                        elts=[Constant(value=836.79, kind=None)],
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
                                                                                            Constant(value=836.79, kind=None),
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
                                                                                            Constant(value=836.79, kind=None),
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
                    name='test_return_order',
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
                            value=Constant(value=' Test return order\n\n        Order (invoiced)\n        ======\n        +----------+----------+---------------+----------+-----+---------+-------------+-------+\n        | order    | payments | invoiced?     | product  | qty | untaxed | tax         | total |\n        +----------+----------+---------------+----------+-----+---------+-------------+-------+\n        | order 1  | cash     | yes, customer | product1 |   3 |      30 | 2.1         |  32.1 |\n        |          |          |               | product2 |   2 |   36.36 | 3.64        |    40 |\n        |          |          |               | product3 |   1 |   27.27 | 2.73 + 1.91 | 31.91 |\n        +----------+----------+---------------+----------+-----+---------+-------------+-------+\n\n        The order is invoiced so the tax of the invoiced order is in the account_move of the order.\n        However, the return order is not invoiced, thus, the journal items are in the session_move,\n        which will contain the tax lines of the returned products.\n\n        manually_calculated_taxes = (4.01, 6.37)\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_before_closing_cb',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='orders_total', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='amount_total',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='pos_session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='order_ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='orders_total', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='total_payments_amount',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Total order amount should be equal to the total payment amount.', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='order_to_return', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='order', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Constant(value='12345-123-1234', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='pos_reference',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_to_return', ctx=Load()),
                                            attr='refund',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='refund_order', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='pos_session',
                                                    ctx=Load(),
                                                ),
                                                attr='order_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='order', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='draft', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='context_make_payment', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='active_ids', kind=None),
                                            Constant(value='active_id', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='refund_order', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='refund_order', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='make_payment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='pos.make.payment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context_make_payment', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='payment_method_id', kind=None),
                                                    Constant(value='amount', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='cash_pm1',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=104.01, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='make_payment', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='refund_order', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            Constant(value='paid', kind=None),
                                            Constant(value='Payment is registered, order should be paid.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='refund_order', ctx=Load()),
                                                attr='amount_paid',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=104.01, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Amount paid for return order should be negative.', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_after_closing_cb',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[Name(id='manually_calculated_taxes', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=4.01, kind=None),
                                            Constant(value=6.37, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pos_session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='account_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_received_account',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[Name(id='manually_calculated_taxes', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='t1', ctx=Store()),
                                            Name(id='t2', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='manually_calculated_taxes', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='balance', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertAlmostEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='t1', ctx=Load()),
                                                    Name(id='t2', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='msg',
                                                        value=Constant(value='Taxes should be correctly combined and should be debit.', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
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
                                            Constant(value='before_closing_cb', kind=None),
                                            Constant(value='journal_entries_before_closing', kind=None),
                                            Constant(value='after_closing_cb', kind=None),
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
                                                                                attr='product1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=3, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=2, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product3',
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
                                                                            Constant(value=104.01, kind=None),
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
                                                            Constant(value='12345-123-1234', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='_before_closing_cb', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='12345-123-1234', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='payments', kind=None)],
                                                        values=[
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
                                                                                    Constant(value=104.01, kind=None),
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
                                                                                                    Constant(value=104.01, kind=None),
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
                                                                                                    Constant(value=104.01, kind=None),
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
                                            Name(id='_after_closing_cb', ctx=Load()),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=4.01, kind=None),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=6.37, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=30, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=36.36, kind=None),
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
                                                                                    attr='sales_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=27.27, kind=None),
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
                                                                                    attr='pos_receivable_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=104.01, kind=None),
                                                                            Constant(value=True, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
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
