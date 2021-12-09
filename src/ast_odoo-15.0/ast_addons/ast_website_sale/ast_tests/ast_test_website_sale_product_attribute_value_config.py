Module(
    body=[
        ImportFrom(
            module='odoo.addons.sale.tests.test_sale_product_attribute_value_config',
            names=[alias(name='TestSaleProductAttributeValueCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.tools',
            names=[alias(name='MockRequest', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWebsiteSaleProductAttributeValueConfig',
            bases=[Name(id='TestSaleProductAttributeValueCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_get_combination_info',
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
                            targets=[Name(id='current_website', ctx=Store())],
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
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='current_website', ctx=Load()),
                                    attr='get_current_pricelist',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='computer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Name(id='current_website', ctx=Load()),
                                            attr='id',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.pricelist.item', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='price_discount', kind=None),
                                            Constant(value='compute_price', kind=None),
                                            Constant(value='pricelist_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value='formula', kind=None),
                                            Attribute(
                                                value=Name(id='pricelist', ctx=Load()),
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
                            targets=[Name(id='discount_rate', ctx=Store())],
                            value=Constant(value=0.9, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                            Constant(value='Test tax', kind=None),
                                            Constant(value=15, kind=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='taxes_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tax', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_ratio', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=100, kind=None),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='tax', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Div(),
                                right=Constant(value=100, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_ratio', ctx=Store())],
                            value=Constant(value=2, kind=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_setup_currency',
                                    ctx=Load(),
                                ),
                                args=[Name(id='currency_ratio', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='discount_policy',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='with_discount', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_tax_included', ctx=Store())],
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
                                        args=[Constant(value='account.group_show_line_subtotals_tax_included', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_tax_excluded', ctx=Store())],
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
                                        args=[Constant(value='account.group_show_line_subtotals_tax_excluded', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_included', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=Sub(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_excluded', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value=2222, kind=None),
                                            op=Mult(),
                                            right=Name(id='discount_rate', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='currency_ratio', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='list_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value=2222, kind=None),
                                            op=Mult(),
                                            right=Name(id='discount_rate', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='currency_ratio', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='has_discounted_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_excluded', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=Sub(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_included', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value=2222, kind=None),
                                                op=Mult(),
                                                right=Name(id='discount_rate', ctx=Load()),
                                            ),
                                            op=Mult(),
                                            right=Name(id='currency_ratio', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='tax_ratio', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='list_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value=2222, kind=None),
                                                op=Mult(),
                                                right=Name(id='discount_rate', ctx=Load()),
                                            ),
                                            op=Mult(),
                                            right=Name(id='currency_ratio', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='tax_ratio', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='has_discounted_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='discount_policy',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='without_discount', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='pricelist', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='compare_amounts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='combination_info', ctx=Load()),
                                                slice=Constant(value='price', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2222, kind=None),
                                                        op=Mult(),
                                                        right=Name(id='discount_rate', ctx=Load()),
                                                    ),
                                                    op=Mult(),
                                                    right=Name(id='currency_ratio', ctx=Load()),
                                                ),
                                                op=Mult(),
                                                right=Name(id='tax_ratio', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='pricelist', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='compare_amounts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='combination_info', ctx=Load()),
                                                slice=Constant(value='list_price', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=2222, kind=None),
                                                    op=Mult(),
                                                    right=Name(id='currency_ratio', ctx=Load()),
                                                ),
                                                op=Mult(),
                                                right=Name(id='tax_ratio', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='has_discounted_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
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
                    name='test_get_combination_info_with_fpos',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
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
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='current_website', ctx=Load()),
                                    attr='get_current_pricelist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='product.pricelist', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='pricelist', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='test_product', ctx=Store())],
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
                                                slice=Constant(value='product.template', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='price', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test Product', kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Name(id='current_website', ctx=Load()),
                                            attr='id',
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
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='item_ids',
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
                                        slice=Constant(value='product.pricelist.item', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='applied_on', kind=None),
                                            Constant(value='base', kind=None),
                                            Constant(value='compute_price', kind=None),
                                            Constant(value='fixed_price', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1_product', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='fixed', kind=None),
                                            Constant(value=500, kind=None),
                                            Attribute(
                                                value=Name(id='test_product', ctx=Load()),
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
                            targets=[Name(id='tax15', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                            Constant(value='Test tax 15', kind=None),
                                            Constant(value=15, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                            Constant(value='Test tax 0', kind=None),
                                            Constant(value=0, kind=None),
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
                                    value=Name(id='test_product', ctx=Load()),
                                    attr='taxes_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tax15', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_tax_included', ctx=Store())],
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
                                        args=[Constant(value='account.group_show_line_subtotals_tax_included', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_tax_excluded', ctx=Store())],
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
                                        args=[Constant(value='account.group_show_line_subtotals_tax_excluded', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_excluded', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=Sub(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='group_tax_included', ctx=Load()),
                                attr='users',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='auto_apply', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value=True, kind=None),
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
                                                    args=[Constant(value='base.be', kind=None)],
                                                    keywords=[],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                                value=Name(id='tax15', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='tax0', ctx=Load()),
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
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_product', ctx=Load()),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=575, kind=None),
                                    Constant(value='500$ + 15% tax', kind=None),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='list_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=575, kind=None),
                                    Constant(value='500$ + 15% tax (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
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
                                    args=[Constant(value='base.be', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_product', ctx=Load()),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=500, kind=None),
                                    Constant(value='500% + 0% tax (mapped from fp 15% -> 0% for BE)', kind=None),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='list_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=500, kind=None),
                                    Constant(value='500% + 0% tax (mapped from fp 15% -> 0% for BE) (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tax15', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='price_include', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_product', ctx=Load()),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=500, kind=None),
                                    Constant(value='434.78$ + 15% tax', kind=None),
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
                                    Subscript(
                                        value=Name(id='combination_info', ctx=Load()),
                                        slice=Constant(value='list_price', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=500, kind=None),
                                    Constant(value='434.78$ + 15% tax (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
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
                                    args=[Constant(value='base.be', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_product', ctx=Load()),
                                    attr='_get_combination_info',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='combination_info', ctx=Load()),
                                                slice=Constant(value='price', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=434.78, kind=None),
                                    Constant(value='434.78$ + 0% tax (mapped from fp 15% -> 0% for BE)', kind=None),
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='combination_info', ctx=Load()),
                                                slice=Constant(value='list_price', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=434.78, kind=None),
                                    Constant(value='434.78$ + 0% tax (mapped from fp 15% -> 0% for BE)', kind=None),
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
        ClassDef(
            name='TestWebsiteSaleProductPricelist',
            bases=[Name(id='TestSaleProductAttributeValueCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_cart_update_with_fpos',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
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
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='current_website', ctx=Load()),
                                    attr='get_current_pricelist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='product.pricelist', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='pricelist', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='tax10', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                            Constant(value='price_include', kind=None),
                                            Constant(value='amount_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test tax 10', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='percent', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                            Constant(value='price_include', kind=None),
                                            Constant(value='amount_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test tax 0', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='percent', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_product', ctx=Store())],
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
                                                slice=Constant(value='product.template', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='price', kind=None),
                                                    Constant(value='taxes_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test Product', kind=None),
                                                    Constant(value=110, kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='tax10', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Name(id='current_website', ctx=Load()),
                                            attr='id',
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
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='item_ids',
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
                                        slice=Constant(value='product.pricelist.item', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='applied_on', kind=None),
                                            Constant(value='base', kind=None),
                                            Constant(value='compute_price', kind=None),
                                            Constant(value='percent_price', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1_product', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='percentage', kind=None),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=Name(id='test_product', ctx=Load()),
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
                                    value=Name(id='pricelist', ctx=Load()),
                                    attr='discount_policy',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='without_discount', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                        values=[Constant(value='test', kind=None)],
                                    ),
                                ],
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
                                                value=Name(id='tax10', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='tax0', ctx=Load()),
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
                            targets=[Name(id='so', ctx=Store())],
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
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
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
                            targets=[Name(id='sol', ctx=Store())],
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
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                            Constant(value='order_id', kind=None),
                                            Constant(value='tax_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_product', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='test_product', ctx=Load()),
                                                    attr='product_variant_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='test_product', ctx=Load()),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='test_product', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='so', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='tax10', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='sol', ctx=Load()),
                                                attr='price_total',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=110.0, kind=None),
                                    Constant(value='110$ with 10% included tax', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='so', ctx=Load()),
                                    attr='pricelist_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='pricelist', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='so', ctx=Load()),
                                    attr='fiscal_position_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='fpos', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sol', ctx=Load()),
                                    attr='product_id_change',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='MockRequest', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='website',
                                                value=Name(id='current_website', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='sale_order_id',
                                                value=Attribute(
                                                    value=Name(id='so', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='so', ctx=Load()),
                                            attr='_cart_update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='product_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='test_product', ctx=Load()),
                                                        attr='product_variant_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='line_id',
                                                value=Attribute(
                                                    value=Name(id='sol', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='set_qty',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='sol', ctx=Load()),
                                                attr='price_total',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=50, kind=None),
                                    Constant(value='100$ with 50% discount + 0% tax (mapped from fp 10% -> 0%)', kind=None),
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
