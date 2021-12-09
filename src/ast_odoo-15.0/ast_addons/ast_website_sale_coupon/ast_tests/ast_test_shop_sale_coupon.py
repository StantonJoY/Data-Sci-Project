Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
                alias(name='TransactionCase', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sale.tests.test_sale_product_attribute_value_config',
            names=[alias(name='TestSaleProductAttributeValueCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestUi',
            bases=[
                Name(id='TestSaleProductAttributeValueCommon', ctx=Load()),
                Name(id='HttpCase', ctx=Load()),
            ],
            keywords=[],
            body=[
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
                                            Name(id='TestUi', ctx=Load()),
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
                                    attr='currency_ratio',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist', ctx=Store())],
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
                                args=[Constant(value='product.list0', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_setup_currency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='currency_ratio',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new_currency', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_admin_shop_sale_coupon_tour',
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
                            targets=[Name(id='public_category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.public.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Public Category', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='large_cabinet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='sale_ok', kind=None),
                                            Constant(value='public_categ_ids', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Small Cabinet', kind=None),
                                            Constant(value=320.0, kind=None),
                                            Constant(value='consu', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='public_category', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='free_large_cabinet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                            Constant(value='supplier_taxes_id', kind=None),
                                            Constant(value='sale_ok', kind=None),
                                            Constant(value='purchase_ok', kind=None),
                                            Constant(value='invoice_policy', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='categ_id', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Free Product - Small Cabinet', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='order', kind=None),
                                            Constant(value='FREELARGECABINET', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='product.product_category_all', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ten_percent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                            Constant(value='supplier_taxes_id', kind=None),
                                            Constant(value='sale_ok', kind=None),
                                            Constant(value='purchase_ok', kind=None),
                                            Constant(value='invoice_policy', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='categ_id', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='10.0% discount on total amount', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='order', kind=None),
                                            Constant(value='10PERCENTDISC', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='product.product_category_all', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='coupon.program', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='reward_type', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='reward_product_id', kind=None),
                                            Constant(value='rule_min_quantity', kind=None),
                                            Constant(value='rule_products_domain', kind=None),
                                            Constant(value='discount_line_product_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Buy 3 Small Cabinets, get one for free', kind=None),
                                            Constant(value='no_code_needed', kind=None),
                                            Constant(value='on_order', kind=None),
                                            Constant(value='product', kind=None),
                                            Constant(value='promotion_program', kind=None),
                                            Attribute(
                                                value=Name(id='large_cabinet', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
                                            Constant(value="[['name', 'ilike', 'Small Cabinet']]", kind=None),
                                            Attribute(
                                                value=Name(id='free_large_cabinet', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='promo_code', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='discount_type', kind=None),
                                            Constant(value='discount_percentage', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='discount_line_product_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Code for 10% on orders', kind=None),
                                            Constant(value='code_needed', kind=None),
                                            Constant(value='testcode', kind=None),
                                            Constant(value='on_order', kind=None),
                                            Constant(value='percentage', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Constant(value='promotion_program', kind=None),
                                            Attribute(
                                                value=Name(id='ten_percent', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_sale.search_count_box', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='shop_sale_coupon', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
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
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestWebsiteSaleCoupon',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
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
                                            Name(id='TestWebsiteSaleCoupon', ctx=Load()),
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
                            targets=[Name(id='program', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='discount_type', kind=None),
                                            Constant(value='discount_percentage', kind=None),
                                            Constant(value='program_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='10% TEST Discount', kind=None),
                                            Constant(value='code_needed', kind=None),
                                            Constant(value='on_order', kind=None),
                                            Constant(value='percentage', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Constant(value='coupon_program', kind=None),
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
                                                        slice=Constant(value='coupon.generate.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_id',
                                                        value=Attribute(
                                                            value=Name(id='program', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Dict(keys=[], values=[])],
                                        keywords=[],
                                    ),
                                    attr='generate_coupon',
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
                                    attr='coupon',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='program', ctx=Load()),
                                    attr='coupon_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='steve',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Steve Bucknor', kind=None),
                                            Constant(value='steve.bucknor@example.com', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='empty_order',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='partner_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='steve',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_gc_coupon',
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
                            targets=[Name(id='order', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='empty_order',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='website_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='order_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='product.product', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='list_price', kind=None),
                                                                Constant(value='sale_ok', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='Product A', kind=None),
                                                                Constant(value=100, kind=None),
                                                                Constant(value=True, kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Product A', kind=None),
                                            Constant(value=2.0, kind=None),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='sale.coupon.apply.code', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_id',
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='coupon_code', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='coupon',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='process_coupon',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='recompute_coupon_lines',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='applied_coupon_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value="The coupon should've been applied on the order", kind=None),
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='coupon',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='applied_coupon_ids',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='used', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='_gc_abandoned_coupons',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='applied_coupon_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value="The coupon shouldn't have been removed from the order no more than 4 days", kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='used', kind=None),
                                    Constant(value='Should not have been changed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.config_parameter', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='icp_validity', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='key', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='website_sale_coupon.abandonned_coupon_validity', kind=None),
                                            Constant(value=5, kind=None),
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
                                    value=Name(id='order', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='UPDATE %s SET write_date = %%s WHERE id = %%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='datetime',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='now',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=4, kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='hours',
                                                                    value=Constant(value=2, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='_gc_abandoned_coupons',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='applied_coupon_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value="The coupon shouldn't have been removed from the order the order is 4 days old but icp validity is 5 days", kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='used', kind=None),
                                    Constant(value='Should not have been changed (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='icp_validity', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='_gc_abandoned_coupons',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='applied_coupon_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value="The coupon should've been removed from the order as more than 4 days", kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
                                    Constant(value='Should have been reset.', kind=None),
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
