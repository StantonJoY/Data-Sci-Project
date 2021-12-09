Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_sale.controllers.main',
            names=[alias(name='WebsiteSale', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteSaleDelivery',
            bases=[Name(id='WebsiteSale', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='shop_payment',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='sale_get_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='carrier_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='post', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='carrier_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='carrier_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='carrier_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='carrier_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='order', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='_check_carrier_quotation',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='force_carrier_id',
                                                value=Name(id='carrier_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                If(
                                    test=Name(id='carrier_id', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/shop/payment', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteSaleDelivery', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='shop_payment',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_eshop_carrier',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='sale_get_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='carrier_id', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='post', ctx=Load()),
                                        slice=Constant(value='carrier_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='order', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='_check_carrier_quotation',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='force_carrier_id',
                                                value=Name(id='carrier_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_website_sale_delivery_return',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/shop/update_carrier', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cart_carrier_rate_shipment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='carrier_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='sale_get_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='force_create',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='carrier_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='_get_delivery_methods',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='It seems that a delivery method is not compatible with your address. Please refresh the page and try again.', kind=None)],
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
                        Assign(
                            targets=[Name(id='Monetary', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb.field.monetary', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='carrier_id', kind=None)],
                                values=[Name(id='carrier_id', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='carrier', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='delivery.carrier', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='carrier_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rate', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='carrier', ctx=Load()),
                                    attr='rate_shipment',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='rate', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='success', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='carrier', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='taxes_id',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='t', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='company_id',
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
                                If(
                                    test=Name(id='tax_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='fpos', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='fiscal_position_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tax_ids', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fpos', ctx=Load()),
                                                    attr='map_tax',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tax_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='taxes', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tax_ids', ctx=Load()),
                                                    attr='compute_all',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='rate', ctx=Load()),
                                                        slice=Constant(value='price', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='currency',
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='quantity',
                                                        value=Constant(value=1.0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='product',
                                                        value=Attribute(
                                                            value=Name(id='carrier', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='partner',
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='partner_shipping_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='has_group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='account.group_show_line_subtotals_tax_excluded', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rate', ctx=Load()),
                                                            slice=Constant(value='price', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='taxes', ctx=Load()),
                                                        slice=Constant(value='total_excluded', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rate', ctx=Load()),
                                                            slice=Constant(value='price', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='taxes', ctx=Load()),
                                                        slice=Constant(value='total_included', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='status', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='new_amount_delivery', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Monetary', ctx=Load()),
                                            attr='value_to_html',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='rate', ctx=Load()),
                                                slice=Constant(value='price', kind=None),
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='display_currency', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='currency_id',
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
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='is_free_delivery', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='bool', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='rate', ctx=Load()),
                                                    slice=Constant(value='price', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='error_message', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='rate', ctx=Load()),
                                        slice=Constant(value='warning_message', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='status', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='new_amount_delivery', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Monetary', ctx=Load()),
                                            attr='value_to_html',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0.0, kind=None),
                                            Dict(
                                                keys=[Constant(value='display_currency', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='currency_id',
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
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='error_message', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='rate', ctx=Load()),
                                        slice=Constant(value='error_message', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/shop/carrier_rate_shipment', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='order_lines_2_google_api',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_lines', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Transforms a list of order lines into a dict for google analytics ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='order_lines_not_delivery', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order_lines', ctx=Load()),
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='is_delivery',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteSaleDelivery', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='order_lines_2_google_api',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order_lines_not_delivery', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='order_2_return_dict',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the tracking_cart dict of the order for Google analytics ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ret', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteSaleDelivery', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='order_2_return_dict',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='delivery_line', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='is_delivery', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='delivery_line', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ret', ctx=Load()),
                                            slice=Constant(value='shipping', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='delivery_line', ctx=Load()),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='ret', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_shop_payment_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteSaleDelivery', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_shop_payment_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_storable_products', ctx=Store())],
                            value=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                List(
                                                    elts=[
                                                        Constant(value='consu', kind=None),
                                                        Constant(value='product', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='line', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='order_line',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='_get_delivery_methods',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    Name(id='has_storable_products', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='errors', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Sorry, we are unable to ship your order', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='No shipping method is available for your current order and shipping address. Please contact us for more information.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='has_storable_products', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='carrier_id',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='delivery_rating_success',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='_remove_delivery_line',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='delivery_carriers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='_get_delivery_methods',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='deliveries', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='delivery_carriers', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='delivery_has_storable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='has_storable_products', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='delivery_action_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='delivery.action_delivery_carrier_form', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_website_sale_delivery_return',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Monetary', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb.field.monetary', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='carrier_id', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='post', ctx=Load()),
                                        slice=Constant(value='carrier_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Attribute(
                                value=Name(id='order', ctx=Load()),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='order', ctx=Load()),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='status', kind=None),
                                            Constant(value='error_message', kind=None),
                                            Constant(value='carrier_id', kind=None),
                                            Constant(value='is_free_delivery', kind=None),
                                            Constant(value='new_amount_delivery', kind=None),
                                            Constant(value='new_amount_untaxed', kind=None),
                                            Constant(value='new_amount_tax', kind=None),
                                            Constant(value='new_amount_total', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='delivery_rating_success',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='delivery_message',
                                                ctx=Load(),
                                            ),
                                            Name(id='carrier_id', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='bool', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='amount_delivery',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Monetary', ctx=Load()),
                                                    attr='value_to_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='amount_delivery',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='display_currency', kind=None)],
                                                        values=[Name(id='currency', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Monetary', ctx=Load()),
                                                    attr='value_to_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='amount_untaxed',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='display_currency', kind=None)],
                                                        values=[Name(id='currency', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Monetary', ctx=Load()),
                                                    attr='value_to_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='amount_tax',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='display_currency', kind=None)],
                                                        values=[Name(id='currency', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Monetary', ctx=Load()),
                                                    attr='value_to_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='amount_total',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='display_currency', kind=None)],
                                                        values=[Name(id='currency', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
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
