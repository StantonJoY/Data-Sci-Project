Module(
    body=[
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.controllers.backend',
            names=[alias(name='WebsiteBackend', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteSaleBackend',
            bases=[Name(id='WebsiteBackend', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='fetch_dashboard_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                            arg(arg='date_from', annotation=None, type_comment=None),
                            arg(arg='date_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Website', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Website', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='website_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Website', ctx=Load()),
                                            attr='get_current_website',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteSaleBackend', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='fetch_dashboard_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='website_id', ctx=Load()),
                                    Name(id='date_from', ctx=Load()),
                                    Name(id='date_to', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_date_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='date_from', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_date_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='date_to', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_diff_days', ctx=Store())],
                            value=Attribute(
                                value=BinOp(
                                    left=Name(id='date_date_to', ctx=Load()),
                                    op=Sub(),
                                    right=Name(id='date_date_from', ctx=Load()),
                                ),
                                attr='days',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='datetime_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='combine',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='date_date_from', ctx=Load()),
                                    Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='min',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='datetime_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='combine',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='date_date_to', ctx=Load()),
                                    Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='max',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sales_values', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='graph',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='best_sellers',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='summary',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='order_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_carts_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_unpaid_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_to_invoice_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_carts_abandoned_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='payment_to_capture_count',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='total_sold',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_per_day_ratio',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_sold_ratio',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='order_convertion_pctg',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='dashboards', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='sales', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='sales_values', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='groups', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='sale_salesman', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='sales_team.group_sale_salesman', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value='groups', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='sale_salesman', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='results', ctx=Load()),
                                            slice=Constant(value='dashboards', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sales', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='utm_graph', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='fetch_utm_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='datetime_from', ctx=Load()),
                                    Name(id='datetime_to', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_report_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='current_website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='datetime_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='<=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_product_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=Name(id='sale_report_domain', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='product_tmpl_id', kind=None),
                                                Constant(value='product_uom_qty', kind=None),
                                                Constant(value='price_subtotal', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='product_tmpl_id', kind=None),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Constant(value='product_uom_qty desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product_line', ctx=Store()),
                            iter=Name(id='report_product_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product_tmpl_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.template', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='product_line', ctx=Load()),
                                                    slice=Constant(value='product_tmpl_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
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
                                                value=Name(id='sales_values', ctx=Load()),
                                                slice=Constant(value='best_sellers', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='qty', kind=None),
                                                    Constant(value='sales', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product_tmpl_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='product_tmpl_id', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='product_line', ctx=Load()),
                                                        slice=Constant(value='product_uom_qty', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='product_line', ctx=Load()),
                                                        slice=Constant(value='price_subtotal', kind=None),
                                                        ctx=Load(),
                                                    ),
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
                            targets=[Name(id='sale_order_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='current_website', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_order', kind=None),
                                            Constant(value='>=', kind=None),
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
                                                args=[Name(id='datetime_from', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_order', kind=None),
                                            Constant(value='<=', kind=None),
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
                                                args=[Name(id='datetime_to', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_group_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sale_order_domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='state', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='state', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='res', ctx=Store()),
                            iter=Name(id='so_group_data', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='state', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sent', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='sales_values', ctx=Load()),
                                                    slice=Constant(value='summary', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='order_unpaid_count', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='state_count', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='res', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='state', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='sale', kind=None),
                                                            Constant(value='done', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='sales_values', ctx=Load()),
                                                            slice=Constant(value='summary', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='order_count', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='state_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Subscript(
                                            value=Name(id='sales_values', ctx=Load()),
                                            slice=Constant(value='summary', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='order_carts_count', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='state_count', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_price_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='website_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='current_website', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='state', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Constant(value='sale', kind=None),
                                                                Constant(value='done', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='date', kind=None),
                                                        Constant(value='>=', kind=None),
                                                        Name(id='datetime_from', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='date', kind=None),
                                                        Constant(value='<=', kind=None),
                                                        Name(id='datetime_to', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='team_id', kind=None),
                                                Constant(value='price_subtotal', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='team_id', kind=None)],
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
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='order_to_invoice_count',
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sale.order', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Name(id='sale_order_domain', ctx=Load()),
                                                    op=Add(),
                                                    right=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='sale', kind=None),
                                                                            Constant(value='done', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='order_line', kind=None),
                                                                    Constant(value='!=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='partner_id', kind=None),
                                                                    Constant(value='!=', kind=None),
                                                                    Attribute(
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
                                                                            args=[Constant(value='base.public_partner', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='invoice_status', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='to invoice', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='order_carts_abandoned_count',
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sale.order', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Name(id='sale_order_domain', ctx=Load()),
                                                    op=Add(),
                                                    right=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='is_abandoned_cart', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='cart_recovery_email_sent', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='payment_to_capture_count',
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='payment.transaction', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='search_count',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='state', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value='authorized', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='sale_order_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='request', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='sale.order', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Name(id='sale_order_domain', ctx=Load()),
                                                                                op=Add(),
                                                                                right=List(
                                                                                    elts=[
                                                                                        Tuple(
                                                                                            elts=[
                                                                                                Constant(value='state', kind=None),
                                                                                                Constant(value='!=', kind=None),
                                                                                                Constant(value='cancel', kind=None),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
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
                                    ),
                                    keyword(
                                        arg='total_sold',
                                        value=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='price_line', ctx=Load()),
                                                        slice=Constant(value='price_subtotal', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='price_line', ctx=Store()),
                                                            iter=Name(id='report_price_lines', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='order_per_day_ratio', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='float', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='sales_values', ctx=Load()),
                                                        slice=Constant(value='summary', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='order_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Name(id='date_diff_days', ctx=Load()),
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='order_sold_ratio', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Subscript(
                                    value=Subscript(
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='order_count', kind=None),
                                    ctx=Load(),
                                ),
                                body=Call(
                                    func=Name(id='round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='sales_values', ctx=Load()),
                                                            slice=Constant(value='summary', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='total_sold', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Div(),
                                            right=Subscript(
                                                value=Subscript(
                                                    value=Name(id='sales_values', ctx=Load()),
                                                    slice=Constant(value='summary', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='order_count', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                        Constant(value=2, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value=0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='order_convertion_pctg', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Subscript(
                                    value=Subscript(
                                        value=Name(id='sales_values', ctx=Load()),
                                        slice=Constant(value='summary', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='order_carts_count', kind=None),
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=BinOp(
                                        left=Constant(value=100.0, kind=None),
                                        op=Mult(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='sales_values', ctx=Load()),
                                                slice=Constant(value='summary', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='order_count', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    op=Div(),
                                    right=Subscript(
                                        value=Subscript(
                                            value=Name(id='sales_values', ctx=Load()),
                                            slice=Constant(value='summary', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='order_carts_count', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value=0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='date_diff_days', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=7, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='previous_sale_label', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Previous Week', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='date_diff_days', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=7, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='date_diff_days', ctx=Load()),
                                                ops=[LtE()],
                                                comparators=[Constant(value=31, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='previous_sale_label', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Previous Month', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='previous_sale_label', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Previous Year', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='sales_values', ctx=Load()),
                                slice=Constant(value='graph', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='values', kind=None),
                                            Constant(value='key', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compute_sale_graph',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='date_date_from', ctx=Load()),
                                                    Name(id='date_date_to', ctx=Load()),
                                                    Name(id='sale_report_domain', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='Untaxed Total', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='values', kind=None),
                                            Constant(value='key', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compute_sale_graph',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='date_date_from', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Name(id='date_diff_days', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Name(id='date_date_from', ctx=Load()),
                                                    Name(id='sale_report_domain', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='previous',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Name(id='previous_sale_label', ctx=Load()),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
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
                    name='fetch_utm_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date_from', annotation=None, type_comment=None),
                            arg(arg='date_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sale_utm_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_order', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='date_from', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_order', kind=None),
                                            Constant(value='<=', kind=None),
                                            Name(id='date_to', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orders_data_groupby_campaign_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=BinOp(
                                            left=Name(id='sale_utm_domain', ctx=Load()),
                                            op=Add(),
                                            right=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='campaign_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='amount_total', kind=None),
                                                Constant(value='id', kind=None),
                                                Constant(value='campaign_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='campaign_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orders_data_groupby_medium_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=BinOp(
                                            left=Name(id='sale_utm_domain', ctx=Load()),
                                            op=Add(),
                                            right=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='medium_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='amount_total', kind=None),
                                                Constant(value='id', kind=None),
                                                Constant(value='medium_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='medium_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orders_data_groupby_source_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=BinOp(
                                            left=Name(id='sale_utm_domain', ctx=Load()),
                                            op=Add(),
                                            right=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='source_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='amount_total', kind=None),
                                                Constant(value='id', kind=None),
                                                Constant(value='source_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='source_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='campaign_id', kind=None),
                                    Constant(value='medium_id', kind=None),
                                    Constant(value='source_id', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='compute_utm_graph_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='campaign_id', kind=None),
                                            Name(id='orders_data_groupby_campaign_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='compute_utm_graph_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='medium_id', kind=None),
                                            Name(id='orders_data_groupby_medium_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='compute_utm_graph_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='source_id', kind=None),
                                            Name(id='orders_data_groupby_source_id', ctx=Load()),
                                        ],
                                        keywords=[],
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
                    name='compute_utm_graph_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='utm_type', annotation=None, type_comment=None),
                            arg(arg='utm_graph_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='utm_type', kind=None),
                                        Constant(value='amount_total', kind=None),
                                    ],
                                    values=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Name(id='utm_type', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='amount_total', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='data', ctx=Store()),
                                        iter=Name(id='utm_graph_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                    name='_compute_sale_graph',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date_from', annotation=None, type_comment=None),
                            arg(arg='date_to', annotation=None, type_comment=None),
                            arg(arg='sales_domain', annotation=None, type_comment=None),
                            arg(arg='previous', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='days_between', ctx=Store())],
                            value=Attribute(
                                value=BinOp(
                                    left=Name(id='date_to', ctx=Load()),
                                    op=Sub(),
                                    right=Name(id='date_from', ctx=Load()),
                                ),
                                attr='days',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_list', ctx=Store())],
                            value=ListComp(
                                elt=BinOp(
                                    left=Name(id='date_from', ctx=Load()),
                                    op=Add(),
                                    right=Call(
                                        func=Name(id='timedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Name(id='x', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=0, kind=None),
                                                BinOp(
                                                    left=Name(id='days_between', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='daily_sales', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=Name(id='sales_domain', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='price_subtotal', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='date:day', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='daily_sales_dict', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='p', ctx=Load()),
                                    slice=Constant(value='date:day', kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='p', ctx=Load()),
                                    slice=Constant(value='price_subtotal', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='p', ctx=Store()),
                                        iter=Name(id='daily_sales', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sales_graph', ctx=Store())],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='0', kind=None),
                                        Constant(value='1', kind=None),
                                    ],
                                    values=[
                                        IfExp(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='previous', ctx=Load()),
                                            ),
                                            body=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='d', ctx=Load())],
                                                keywords=[],
                                            ),
                                            orelse=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='d', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Name(id='days_between', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='daily_sales_dict', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='babel', ctx=Load()),
                                                            attr='dates',
                                                            ctx=Load(),
                                                        ),
                                                        attr='format_date',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='d', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='format',
                                                            value=Constant(value='dd MMM yyyy', kind=None),
                                                        ),
                                                        keyword(
                                                            arg='locale',
                                                            value=Attribute(
                                                                value=Call(
                                                                    func=Name(id='get_lang', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='code',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='d', ctx=Store()),
                                        iter=Name(id='date_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='sales_graph', ctx=Load()),
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
