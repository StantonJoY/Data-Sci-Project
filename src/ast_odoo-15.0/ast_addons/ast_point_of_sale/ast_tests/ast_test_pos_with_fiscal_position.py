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
            name='TestPoSWithFiscalPosition',
            bases=[Name(id='TestPoSCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Tests to pos orders with fiscal position.\n\n    keywords/phrases: fiscal position\n    ', kind=None),
                ),
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='TestPoSWithFiscalPosition', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='config',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='basic_config',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='new_tax_17',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='New Tax 17%', kind=None),
                                            Constant(value=17, kind=None),
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='new_tax_17',
                                            ctx=Load(),
                                        ),
                                        attr='invoice_repartition_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='account_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='tax_received_account',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fpos',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_create_fiscal_position',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fpos_no_tax_dest',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_create_fiscal_position_no_tax_dest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='create_product',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Product 1', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
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
                                                    value=Name(id='cls', ctx=Load()),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='create_product',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Product 2', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
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
                                                    value=Name(id='cls', ctx=Load()),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product3',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='create_product',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Product 3', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
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
                                                    value=Name(id='cls', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='adjust_inventory',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='product2',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
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
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_fiscal_position',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Fiscal Position', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='position_id', kind=None),
                                            Constant(value='account_src_id', kind=None),
                                            Constant(value='account_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='fpos', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='sale_account',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='other_sale_account',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='position_id', kind=None),
                                            Constant(value='tax_src_id', kind=None),
                                            Constant(value='tax_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='fpos', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='taxes',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='tax7', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='new_tax_17',
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fpos', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='account_ids', kind=None),
                                            Constant(value='tax_ids', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='account_fpos', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
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
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='tax_fpos', ctx=Load()),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='fpos', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_fiscal_position_no_tax_dest',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fpos_no_tax_dest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Fiscal Position', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='position_id', kind=None),
                                            Constant(value='account_src_id', kind=None),
                                            Constant(value='account_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='fpos_no_tax_dest', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='sale_account',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='other_sale_account',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='position_id', kind=None),
                                            Constant(value='tax_src_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='fpos_no_tax_dest', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='taxes',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='tax7', kind=None),
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fpos_no_tax_dest', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='account_ids', kind=None),
                                            Constant(value='tax_ids', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='account_fpos', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
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
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='tax_fpos', ctx=Load()),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='fpos_no_tax_dest', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_no_invoice_fpos',
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
                            value=Constant(value=' orders without invoice\n\n        Orders\n        ======\n        +---------+----------+---------------+----------+-----+---------+-----------------+--------+\n        | order   | payments | invoiced?     | product  | qty | untaxed | tax             |  total |\n        +---------+----------+---------------+----------+-----+---------+-----------------+--------+\n        | order 1 | cash     | yes, customer | product1 |  10 |  109.90 | 18.68 [7%->17%] | 128.58 |\n        |         |          |               | product2 |  10 |  181.73 | 18.17 [10%]     | 199.90 |\n        |         |          |               | product3 |  10 |  309.90 | 52.68 [7%->17%] | 362.58 |\n        +---------+----------+---------------+----------+-----+---------+-----------------+--------+\n        | order 2 | cash     | yes, customer | product1 |   5 |   54.95 | 9.34 [7%->17%]  |  64.29 |\n        |         |          |               | product2 |   5 |   90.86 | 9.09 [10%]      |  99.95 |\n        +---------+----------+---------------+----------+-----+---------+-----------------+--------+\n        | order 3 | bank     | no            | product2 |   5 |   90.86 | 9.09 [10%]      |  99.95 |\n        |         |          |               | product3 |   5 |  154.95 | 10.85 [7%]      |  165.8 |\n        +---------+----------+---------------+----------+-----+---------+-----------------+--------+\n\n        Expected Result\n        ===============\n        +---------------------+---------+\n        | account             | balance |\n        +---------------------+---------+\n        | sale_account        | -154.95 |  (for the 7% base amount)\n        | sale_account        |  -90.86 |  (for the 10% base amount)\n        | other_sale_account  | -474.75 |  (for the 17% base amount)\n        | other_sale_account  | -272.59 |  (for the 10% base amount)\n        | tax 17%             |  -80.70 |\n        | tax 10%             |  -36.35 |\n        | tax 7%              |  -10.85 |\n        | pos receivable bank |  265.75 |\n        | pos receivable cash |  855.30 |\n        +---------------------+---------+\n        | Total balance       |     0.0 |\n        +---------------------+---------+\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='customer',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='property_account_position_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fpos',
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
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
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
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
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
                                                                            Constant(value=265.75, kind=None),
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
                                                                            Constant(value=80.7, kind=None),
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
                                                                            Constant(value=36.35, kind=None),
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
                                                                            Constant(value=10.85, kind=None),
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
                                                                            Constant(value=474.75, kind=None),
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
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=154.95, kind=None),
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
                                                                            Constant(value=265.75, kind=None),
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
                                                                            Constant(value=855.3, kind=None),
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
                                                                        elts=[Constant(value=855.3, kind=None)],
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
                                                                                            Constant(value=855.3, kind=None),
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
                                                                                            Constant(value=855.3, kind=None),
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
                                                                        elts=[Constant(value=265.75, kind=None)],
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
                                                                                            Constant(value=265.75, kind=None),
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
                                                                                            Constant(value=265.75, kind=None),
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
                    name='test_02_no_invoice_fpos_no_tax_dest',
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
                            value=Constant(value=' Customer with fiscal position that maps a tax to no tax.\n\n        Orders\n        ======\n        +---------+----------+---------------+----------+-----+---------+-------------+--------+\n        | order   | payments | invoiced?     | product  | qty | untaxed | tax         |  total |\n        +---------+----------+---------------+----------+-----+---------+-------------+--------+\n        | order 1 | bank     | yes, customer | product1 |  10 |  109.90 | 0           | 109.90 |\n        |         |          |               | product2 |  10 |  181.73 | 18.17 [10%] | 199.90 |\n        |         |          |               | product3 |  10 |  309.90 | 0           | 309.90 |\n        +---------+----------+---------------+----------+-----+---------+-------------+--------+\n        | order 2 | cash     | yes, customer | product1 |   5 |   54.95 | 0           |  54.95 |\n        |         |          |               | product2 |   5 |   90.86 | 9.09 [10%]  |  99.95 |\n        +---------+----------+---------------+----------+-----+---------+-------------+--------+\n        | order 3 | bank     | no            | product2 |   5 |   90.86 | 9.09 [10%]  |  99.95 |\n        |         |          |               | product3 |   5 |  154.95 | 10.85 [7%]  | 165.80 |\n        +---------+----------+---------------+----------+-----+---------+-------------+--------+\n\n        Expected Result\n        ===============\n        +---------------------+---------+\n        | account             | balance |\n        +---------------------+---------+\n        | sale_account        | -154.95 |  (for the 7% base amount)\n        | sale_account        |  -90.86 |  (for the 10% base amount)\n        | other_sale_account  | -272.59 |  (for the 10% base amount)\n        | other_sale_account  | -474.75 |  (no tax)\n        | tax 10%             |  -36.35 |\n        | tax 7%              |  -10.85 |\n        | pos receivable bank |  885.45 |\n        | pos receivable cash |   154.9 |\n        +---------------------+---------+\n        | Total balance       |     0.0 |\n        +---------------------+---------+\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='customer',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='property_account_position_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fpos_no_tax_dest',
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
                                                            Constant(value='payments', kind=None),
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
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=619.7, kind=None),
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
                                                            Constant(value='00100-010-0001', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
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
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
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
                                                                            Constant(value=265.75, kind=None),
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
                                                                            Constant(value=36.35, kind=None),
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
                                                                            Constant(value=10.85, kind=None),
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
                                                                            Constant(value=474.75, kind=None),
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
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Constant(value=154.95, kind=None),
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
                                                                            Constant(value=885.45, kind=None),
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
                                                                            Constant(value=154.9, kind=None),
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
                                                                        elts=[Constant(value=154.9, kind=None)],
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
                                                                                            Constant(value=154.9, kind=None),
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
                                                                                            Constant(value=154.9, kind=None),
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
                                                                        elts=[Constant(value=885.45, kind=None)],
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
                                                                                            Constant(value=885.45, kind=None),
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
                                                                                            Constant(value=885.45, kind=None),
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
                    name='test_03_invoiced_fpos',
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
                            value=Constant(value=' Invoice 2 orders.\n\n        Orders\n        ======\n        +---------+----------+---------------------+----------+-----+---------+-----------------+--------+\n        | order   | payments | invoiced?           | product  | qty | untaxed | tax             |  total |\n        +---------+----------+---------------------+----------+-----+---------+-----------------+--------+\n        | order 1 | bank     | yes, customer       | product1 |  10 |  109.90 | 18.68 [7%->17%] | 128.58 |\n        |         |          |                     | product2 |  10 |  181.73 | 18.17 [10%]     | 199.90 |\n        |         |          |                     | product3 |  10 |  309.90 | 52.68 [7%->17%] | 362.58 |\n        +---------+----------+---------------------+----------+-----+---------+-----------------+--------+\n        | order 2 | cash     | no, customer        | product1 |   5 |   54.95 | 9.34 [7%->17%]  |  64.29 |\n        |         |          |                     | product2 |   5 |   90.86 | 9.09 [10%]      |  99.95 |\n        +---------+----------+---------------------+----------+-----+---------+-----------------+--------+\n        | order 3 | cash     | yes, other_customer | product2 |   5 |   90.86 | 9.09 [10%]      |  99.95 |\n        |         |          |                     | product3 |   5 |  154.95 | 10.85 [7%]      | 165.80 |\n        +---------+----------+---------------------+----------+-----+---------+-----------------+--------+\n\n        Expected Result\n        ===============\n        +---------------------+---------+\n        | account             | balance |\n        +---------------------+---------+\n        | other_sale_account  |  -54.95 |  (for the 17% base amount)\n        | other_sale_account  |  -90.86 |  (for the 10% base amount)\n        | tax 10%             |   -9.09 |\n        | tax 17%             |   -9.34 |\n        | pos receivable cash |  429.99 |\n        | pos receivable bank |  691.06 |\n        | receivable          | -691.06 |\n        | other receivable    | -265.75 |\n        +---------------------+---------+\n        | Total balance       |     0.0 |\n        +---------------------+---------+\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='customer',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='property_account_position_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fpos',
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
                                    targets=[Name(id='invoiced_order_1', ctx=Store())],
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
                                                    left=Constant(value='00100-010-0001', kind=None),
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
                                Assign(
                                    targets=[Name(id='invoiced_order_2', ctx=Store())],
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
                                                    left=Constant(value='00100-010-0003', kind=None),
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoiced_order_1', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Invoiced order 1 should exist.', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoiced_order_2', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Invoiced order 2 should exist.', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='invoiced_order_1', ctx=Load()),
                                                attr='account_move',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Invoiced order 1 should have invoice (account_move).', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='invoiced_order_2', ctx=Load()),
                                                attr='account_move',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='Invoiced order 2 should have invoice (account_move).', kind=None),
                                            ),
                                        ],
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
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='bank_pm1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=691.06, kind=None),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
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
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='00100-010-0002', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_quantity_pairs', kind=None),
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
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='other_customer',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Constant(value='00100-010-0003', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='_before_closing_cb', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='00100-010-0001', kind=None),
                                                    Constant(value='00100-010-0003', kind=None),
                                                ],
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
                                                                                    Constant(value=691.06, kind=None),
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
                                                                                                    Constant(value=691.06, kind=None),
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
                                                                                                    Constant(value=691.06, kind=None),
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
                                                                                    Constant(value=265.75, kind=None),
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
                                                                                                    Constant(value=265.75, kind=None),
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
                                                                                                    Constant(value=265.75, kind=None),
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
                                                                            Constant(value=9.34, kind=None),
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
                                                                            Constant(value=9.09, kind=None),
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
                                                                            Constant(value=False, kind=None),
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
                                                                            Constant(value=691.06, kind=None),
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
                                                                            Constant(value=429.99, kind=None),
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
                                                                            Constant(value=691.06, kind=None),
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
                                                                            Constant(value=265.75, kind=None),
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
                                                                        elts=[Constant(value=429.99, kind=None)],
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
                                                                                            Constant(value=429.99, kind=None),
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
                                                                                            Constant(value=429.99, kind=None),
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
                                                                        elts=[Constant(value=691.06, kind=None)],
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
                                                                                            Constant(value=691.06, kind=None),
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
                                                                                            Constant(value=691.06, kind=None),
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
