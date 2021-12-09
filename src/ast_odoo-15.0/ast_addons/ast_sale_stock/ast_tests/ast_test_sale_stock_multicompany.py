Module(
    body=[
        ImportFrom(
            module='odoo.addons.stock_account.tests.test_anglo_saxon_valuation_reconciliation_common',
            names=[alias(name='ValuationReconciliationTestCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sale.tests.common',
            names=[alias(name='TestSaleCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSaleStockMultiCompany',
            bases=[
                Name(id='TestSaleCommon', ctx=Load()),
                Name(id='ValuationReconciliationTestCommon', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='warehouse_A',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_warehouse', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='warehouse_A2',
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
                                        slice=Constant(value='stock.warehouse', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='WH B', kind=None),
                                            Constant(value='WHB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='warehouse_B',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data_2',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_warehouse', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='groups_id',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.group_stock_user', kind=None)],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='groups_id',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='groups_id',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='sales_team.group_sale_salesman', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='property_warehouse_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='warehouse_A',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_data_2',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='property_warehouse_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='warehouse_B',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_warehouse_definition_on_so',
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
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner_a',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='test_product_order',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_order_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='partner_invoice_id', kind=None),
                                    Constant(value='partner_shipping_id', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='order_line', kind=None),
                                    Constant(value='pricelist_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_qty', kind=None),
                                                            Constant(value='product_uom', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=10, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='list_price',
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_pricelist', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_order', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='sale.order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_no_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sale_order', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sale_order_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_no_user', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='property_warehouse_id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                        value=Attribute(
                                            value=Name(id='so_no_user', ctx=Load()),
                                            attr='warehouse_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='warehouse_A',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sale_order_vals2', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='partner_invoice_id', kind=None),
                                    Constant(value='partner_shipping_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='order_line', kind=None),
                                    Constant(value='pricelist_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_qty', kind=None),
                                                            Constant(value='product_uom', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=10, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='list_price',
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_pricelist', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_company_A', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sale_order', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sale_order_vals2', ctx=Load())],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_company_A', ctx=Load()),
                                            attr='warehouse_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='warehouse_A',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sale_order_vals3', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='partner_invoice_id', kind=None),
                                    Constant(value='partner_shipping_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='order_line', kind=None),
                                    Constant(value='pricelist_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data_2',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_qty', kind=None),
                                                            Constant(value='product_uom', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=10, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='list_price',
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='default_pricelist', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_company_B', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sale_order', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_data_2',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sale_order_vals3', ctx=Load())],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_company_B', ctx=Load()),
                                            attr='warehouse_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='warehouse_B',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
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
