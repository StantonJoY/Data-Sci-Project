Module(
    body=[
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='formatLang', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sale.controllers',
            names=[alias(name='portal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='CustomerPortal',
            bases=[
                Attribute(
                    value=Name(id='portal', ctx=Load()),
                    attr='CustomerPortal',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_portal_order_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_sudo', annotation=None, type_comment=None),
                            arg(arg='order_line', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Attribute(
                                value=Name(id='order_sudo', ctx=Load()),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='format_price', ctx=Store())],
                            value=Call(
                                func=Name(id='partial', ctx=Load()),
                                args=[
                                    Name(id='formatLang', ctx=Load()),
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='digits',
                                        value=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='decimal_places',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='order_amount_total', kind=None),
                                    Constant(value='order_amount_untaxed', kind=None),
                                    Constant(value='order_amount_tax', kind=None),
                                    Constant(value='order_amount_undiscounted', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='format_price', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order_sudo', ctx=Load()),
                                                attr='amount_total',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='format_price', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order_sudo', ctx=Load()),
                                                attr='amount_untaxed',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='format_price', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order_sudo', ctx=Load()),
                                                attr='amount_tax',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='format_price', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order_sudo', ctx=Load()),
                                                attr='amount_undiscounted',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='order_line', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='order_line_product_uom_qty', kind=None),
                                                    Constant(value='order_line_price_total', kind=None),
                                                    Constant(value='order_line_price_subtotal', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='product_uom_qty',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='format_price', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='price_total',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='format_price', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='price_subtotal',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='results', ctx=Load()),
                                                    slice=Constant(value='order_totals_table', kind=None),
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
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_render_template',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='sale.sale_order_portal_content_totals_table', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='sale_order', kind=None)],
                                                        values=[Name(id='order_sudo', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_line_dict',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='remove', annotation=None, type_comment=None),
                            arg(arg='unlink', annotation=None, type_comment=None),
                            arg(arg='order_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='input_quantity', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='order_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='sale.order', kind=None),
                                            Name(id='order_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/my', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='order_sudo', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='sent', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='order_line', ctx=Store())],
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
                                                slice=Constant(value='sale.order.line', kind=None),
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
                                        args=[Name(id='line_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='order_line', ctx=Load()),
                                    attr='order_id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='order_sudo', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='input_quantity', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='quantity', ctx=Store())],
                                    value=Name(id='input_quantity', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='remove', ctx=Load()),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        orelse=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quantity', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='order_line', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='number', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='unlink', ctx=Load()),
                                    Compare(
                                        left=Name(id='quantity', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_line', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_portal_order_details',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='order_sudo', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='results', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='unlink', kind=None),
                                                    Constant(value='sale_template', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.ui.view', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_render_template',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='sale.sale_order_portal_content', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='sale_order', kind=None),
                                                                    Constant(value='report_type', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='order_sudo', ctx=Load()),
                                                                    Constant(value='html', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order_line', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_uom_qty', kind=None)],
                                        values=[Name(id='quantity', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_portal_order_details',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='order_sudo', ctx=Load()),
                                    Name(id='order_line', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                            args=[
                                List(
                                    elts=[Constant(value='/my/orders/<int:order_id>/update_line_dict', kind=None)],
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
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order_id', annotation=None, type_comment=None),
                            arg(arg='option_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='order_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='sale.order', kind=None),
                                            Name(id='order_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/my', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='option_sudo', ctx=Store())],
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
                                                slice=Constant(value='sale.order.option', kind=None),
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
                                args=[Name(id='option_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='order_sudo', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='option_sudo', ctx=Load()),
                                        attr='order_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='order_sudo', ctx=Load()),
                                                    attr='get_portal_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='option_sudo', ctx=Load()),
                                    attr='add_option_to_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_portal_order_details',
                                    ctx=Load(),
                                ),
                                args=[Name(id='order_sudo', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='results', ctx=Load()),
                                    slice=Constant(value='sale_template', kind=None),
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
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sale.sale_order_portal_content', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='sale_order', kind=None),
                                            Constant(value='report_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='option_sudo', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='html', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                            args=[
                                List(
                                    elts=[Constant(value='/my/orders/<int:order_id>/add_option/<int:option_id>', kind=None)],
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
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
