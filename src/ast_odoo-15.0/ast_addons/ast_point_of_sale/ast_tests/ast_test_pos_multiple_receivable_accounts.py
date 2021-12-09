Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.point_of_sale.tests.common',
            names=[alias(name='TestPoSCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPoSMultipleReceivableAccounts',
            bases=[Name(id='TestPoSCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test for invoiced orders with customers having receivable account different from default\n\n    Thus, for this test, there are two receivable accounts involved and are set in the\n    customers.\n        self.customer -> self.receivable_account\n        self.other_customer -> self.other_receivable_account\n\n    ADDITIONALLY, this tests different sales account on the products.\n\n    NOTE That both receivable accounts above are different from the pos receivable account.\n    ', kind=None),
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
                                            Name(id='TestPoSMultipleReceivableAccounts', ctx=Load()),
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='lst_price',
                                        value=Constant(value=10.99, kind=None),
                                    ),
                                    keyword(
                                        arg='standard_price',
                                        value=Constant(value=5.0, kind=None),
                                    ),
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='lst_price',
                                        value=Constant(value=19.99, kind=None),
                                    ),
                                    keyword(
                                        arg='standard_price',
                                        value=Constant(value=10.0, kind=None),
                                    ),
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
                                    keyword(
                                        arg='sale_account',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='other_sale_account',
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='lst_price',
                                        value=Constant(value=30.99, kind=None),
                                    ),
                                    keyword(
                                        arg='standard_price',
                                        value=Constant(value=15.0, kind=None),
                                    ),
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
                    name='test_01_invoiced_order_from_other_customer',
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
                            value=Constant(value='\n        Orders\n        ======\n        +---------+----------+-----------+----------+-----+---------+--------------------------+--------+\n        | order   | payments | invoiced? | product  | qty | untaxed | tax                      | total  |\n        +---------+----------+-----------+----------+-----+---------+--------------------------+--------+\n        | order 1 | cash     | no        | product1 | 10  | 109.9   | 7.69 [7%]                | 117.59 |\n        |         |          |           | product2 | 10  | 181.73  | 18.17 [10%]              | 199.9  |\n        |         |          |           | product3 | 10  | 281.73  | 19.72 [7%] + 28.17 [10%] | 329.62 |\n        +---------+----------+-----------+----------+-----+---------+--------------------------+--------+\n        | order 2 | bank     | no        | product1 | 5   | 54.95   | 3.85 [7%]                | 58.80  |\n        |         |          |           | product2 | 5   | 90.86   | 9.09 [10%]               | 99.95  |\n        +---------+----------+-----------+----------+-----+---------+--------------------------+--------+\n        | order 3 | bank     | yes       | product2 | 5   | 90.86   | 9.09 [10%]               | 99.95  |\n        |         |          |           | product3 | 5   | 140.86  | 9.86 [7%] + 14.09 [10%]  | 164.81 |\n        +---------+----------+-----------+----------+-----+---------+--------------------------+--------+\n\n        Expected Result\n        ===============\n        +---------------------+---------+\n        | account             | balance |\n        +---------------------+---------+\n        | sale_account        | -164.85 |\n        | sale_account        | -281.73 |\n        | other_sale_account  | -272.59 |\n        | tax 7%              |  -31.26 |\n        | tax 10%             |  -55.43 |\n        | pos receivable cash |  647.11 |\n        | pos receivable bank |  423.51 |\n        | other receivable    | -264.76 |\n        +---------------------+---------+\n        | Total balance       |    0.00 |\n        +---------------------+---------+\n        ', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Call(
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
                                                                    comparators=[Constant(value='invoiced', kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
                                            Constant(value='There should only be one invoiced order.', kind=None),
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
                                                                                attr='product1',
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
                                                                            Constant(value=5, kind=None),
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
                                                                            Constant(value=158.75, kind=None),
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
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='customer', kind=None),
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
                                                                            Constant(value=5, kind=None),
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
                                                                            Constant(value=264.76, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='other_customer',
                                                                ctx=Load(),
                                                            ),
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
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='line_ids_predicate', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
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
                                                                            ops=[In()],
                                                                            comparators=[
                                                                                BinOp(
                                                                                    left=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=BitOr(),
                                                                                        right=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    op=BitOr(),
                                                                                    right=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='other_receivable_account',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
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
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=90.86, kind=None),
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
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=140.86, kind=None),
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
                                                                                            attr='other_receivable_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=264.76, kind=None),
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
                                                                                    Constant(value=264.76, kind=None),
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
                                                                                                            attr='other_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='other_customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=264.76, kind=None),
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
                                                                                                    Constant(value=264.76, kind=None),
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
                                                                                    attr='tax_received_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=31.26, kind=None),
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
                                                                            Constant(value=55.43, kind=None),
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
                                                                            Constant(value=164.85, kind=None),
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
                                                                                    attr='other_sale_account',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=272.59, kind=None),
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
                                                                            Constant(value=281.73, kind=None),
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
                                                                            Constant(value=423.51, kind=None),
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
                                                                            Constant(value=647.11, kind=None),
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
                                                                            Constant(value=264.76, kind=None),
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
                                                                        elts=[Constant(value=647.11, kind=None)],
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
                                                                                            Constant(value=647.11, kind=None),
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
                                                                                            Constant(value=647.11, kind=None),
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
                                                                        elts=[Constant(value=423.51, kind=None)],
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
                                                                                            Constant(value=423.51, kind=None),
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
                                                                                            Constant(value=423.51, kind=None),
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
                    name='test_02_all_orders_invoiced_mixed_customers',
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
                            value=Constant(value='\n        Orders\n        ======\n        +---------+----------+---------------------+----------+-----+---------+--------------------------+--------+\n        | order   | payments | invoiced?           | product  | qty | untaxed | tax                      |  total |\n        +---------+----------+---------------------+----------+-----+---------+--------------------------+--------+\n        | order 1 | cash     | yes, other_customer | product1 |  10 |  109.90 | 7.69 [7%]                | 117.59 |\n        |         |          |                     | product2 |  10 |  181.73 | 18.17 [10%]              | 199.90 |\n        |         |          |                     | product3 |  10 |  281.73 | 19.72 [7%] + 28.17 [10%] | 329.62 |\n        +---------+----------+---------------------+----------+-----+---------+--------------------------+--------+\n        | order 2 | bank     | yes, customer       | product1 |   5 |   54.95 | 3.85 [7%]                |  58.80 |\n        |         |          |                     | product2 |   5 |   90.86 | 9.09 [10%]               |  99.95 |\n        +---------+----------+---------------------+----------+-----+---------+--------------------------+--------+\n        | order 3 | bank     | yes, other customer | product2 |   5 |   90.86 | 9.09 [10%]               |  99.95 |\n        |         |          |                     | product3 |   5 |  140.86 | 9.86 [7%] + 14.09 [10%]  | 164.81 |\n        +---------+----------+---------------------+----------+-----+---------+--------------------------+--------+\n\n        Expected Result\n        ===============\n        +----------------------+---------+\n        | account              | balance |\n        +----------------------+---------+\n        | pos receivable cash  |  647.11 |\n        | pos receivable bank  |  423.51 |\n        | received bank        | -423.51 |\n        | received cash        | -647.11 |\n        +----------------------+---------+\n        | Total balance        |    0.00 |\n        +----------------------+---------+\n\n        ', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Call(
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
                                                                    comparators=[Constant(value='invoiced', kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=3, kind=None),
                                            Constant(value='All orders should be invoiced.', kind=None),
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
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='customer', kind=None),
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
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='other_customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='09876-098-0987', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='customer', kind=None),
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
                                                                            Constant(value=5, kind=None),
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
                                                                            Constant(value=158.75, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='09876-098-0988', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
                                                            Constant(value='payments', kind=None),
                                                            Constant(value='is_invoiced', kind=None),
                                                            Constant(value='customer', kind=None),
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
                                                                            Constant(value=5, kind=None),
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
                                                                            Constant(value=264.76, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='other_customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='09876-098-0989', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='_before_closing_cb', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='09876-098-0987', kind=None),
                                                    Constant(value='09876-098-0988', kind=None),
                                                    Constant(value='09876-098-0989', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='line_ids_predicate', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
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
                                                                            ops=[In()],
                                                                            comparators=[
                                                                                BinOp(
                                                                                    left=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=BitOr(),
                                                                                        right=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    op=BitOr(),
                                                                                    right=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='other_receivable_account',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
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
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=109.9, kind=None),
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
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=181.73, kind=None),
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
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=281.73, kind=None),
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
                                                                                            attr='other_receivable_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=647.11, kind=None),
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
                                                                                    Constant(value=647.11, kind=None),
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
                                                                                                            attr='other_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='other_customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=647.11, kind=None),
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
                                                                                                    Constant(value=647.11, kind=None),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='line_ids_predicate', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
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
                                                                            ops=[In()],
                                                                            comparators=[
                                                                                BinOp(
                                                                                    left=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=BitOr(),
                                                                                        right=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    op=BitOr(),
                                                                                    right=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='c1_receivable',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
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
                                                                                    Constant(value=54.95, kind=None),
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
                                                                                            attr='other_sale_account',
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
                                                                                    Constant(value=90.86, kind=None),
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
                                                                                    Constant(value=158.75, kind=None),
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
                                                                                    Constant(value=158.75, kind=None),
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
                                                                                                    Constant(value=158.75, kind=None),
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
                                                                                                    Constant(value=158.75, kind=None),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='invoice', kind=None),
                                                            Constant(value='payments', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='line_ids_predicate', kind=None),
                                                                    Constant(value='line_ids', kind=None),
                                                                ],
                                                                values=[
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
                                                                            ops=[In()],
                                                                            comparators=[
                                                                                BinOp(
                                                                                    left=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=BitOr(),
                                                                                        right=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='sales_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    op=BitOr(),
                                                                                    right=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='other_receivable_account',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
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
                                                                                            attr='other_sale_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=90.86, kind=None),
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
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0, kind=None),
                                                                                    Constant(value=140.86, kind=None),
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
                                                                                            attr='other_receivable_account',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='other_customer',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=264.76, kind=None),
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
                                                                                    Constant(value=264.76, kind=None),
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
                                                                                                            attr='other_receivable_account',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='other_customer',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value=0, kind=None),
                                                                                                    Constant(value=264.76, kind=None),
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
                                                                                                    Constant(value=264.76, kind=None),
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
                                                                            Constant(value=423.51, kind=None),
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
                                                                            Constant(value=647.11, kind=None),
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
                                                                            Constant(value=647.11, kind=None),
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
                                                                            Constant(value=423.51, kind=None),
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
                                                                        elts=[Constant(value=647.11, kind=None)],
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
                                                                                            Constant(value=647.11, kind=None),
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
                                                                                            Constant(value=647.11, kind=None),
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
                                                                        elts=[Constant(value=423.51, kind=None)],
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
                                                                                            Constant(value=423.51, kind=None),
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
                                                                                            Constant(value=423.51, kind=None),
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
