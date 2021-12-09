Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_is_zero', asname=None),
                alias(name='float_compare', asname=None),
                alias(name='float_round', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SaleOrderLine',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='sale.order.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Sales Order Line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='order_id, sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_invoice_status',
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
                            value=Constant(value="\n        Compute the invoice status of a SO line. Possible statuses:\n        - no: if the SO is not in status 'sale' or 'done', we consider that there is nothing to\n          invoice. This is also hte default value if the conditions of no other status is met.\n        - to invoice: we refer to the quantity to invoice of the line. Refer to method\n          `_get_to_invoice_qty()` for more information on how this quantity is calculated.\n        - upselling: this is possible only for a product invoiced on ordered quantities for which\n          we delivered more than expected. The could arise if, for example, a project took more\n          time than expected but we decided not to invoice the extra cost to the client. This\n          occurs onyl in state 'sale', so that when a SO is set to done, the upselling opportunity\n          is removed from the list.\n        - invoiced: the quantity invoiced is larger or equal to the quantity ordered.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='precision', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='decimal.precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='precision_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='invoice_status',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='no', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='is_downpayment',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='untaxed_amount_to_invoice',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='invoice_status',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='invoiced', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='float_is_zero', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='qty_to_invoice',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_digits',
                                                                    value=Name(id='precision', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='invoice_status',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='to invoice', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='state',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='sale', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='invoice_policy',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='order', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Call(
                                                                            func=Name(id='float_compare', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='qty_delivered',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='product_uom_qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='precision_digits',
                                                                                    value=Name(id='precision', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='invoice_status',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='upselling', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Name(id='float_compare', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='qty_invoiced',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='product_uom_qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='precision_digits',
                                                                                    value=Name(id='precision', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        ops=[GtE()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='invoice_status',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='invoiced', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='invoice_status',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='no', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='state', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='qty_delivered', kind=None),
                                Constant(value='qty_to_invoice', kind=None),
                                Constant(value='qty_invoiced', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_expected_date',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='order_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='date_order',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='state',
                                                        ctx=Load(),
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
                                            ],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='date_order',
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
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
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='order_date', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='customer_lead',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_amount',
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
                            value=Constant(value='\n        Compute the amounts of the SO line.\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            left=Constant(value=1, kind=None),
                                            op=Sub(),
                                            right=BinOp(
                                                left=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='discount',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=0.0, kind=None),
                                                    ],
                                                ),
                                                op=Div(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='tax_id',
                                                ctx=Load(),
                                            ),
                                            attr='compute_all',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='price', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='product',
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='partner',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_shipping_id',
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
                                            value=Name(id='line', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='price_tax', kind=None),
                                                    Constant(value='price_total', kind=None),
                                                    Constant(value='price_subtotal', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='taxes', ctx=Load()),
                                                            slice=Constant(value='total_included', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Subscript(
                                                            value=Name(id='taxes', ctx=Load()),
                                                            slice=Constant(value='total_excluded', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='taxes', ctx=Load()),
                                                        slice=Constant(value='total_included', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='taxes', ctx=Load()),
                                                        slice=Constant(value='total_excluded', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='import_file', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user_has_groups',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='account.group_account_manager', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='tax_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='invalidate_cache',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Constant(value='invoice_repartition_line_ids', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='tax_id',
                                                                    ctx=Load(),
                                                                ),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='discount', kind=None),
                                Constant(value='price_unit', kind=None),
                                Constant(value='tax_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_product_updatable',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='done', kind=None),
                                                            Constant(value='cancel', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='sale', kind=None)],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='qty_invoiced',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='qty_delivered',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_updatable',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_updatable',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_id', kind=None),
                                Constant(value='order_id.state', kind=None),
                                Constant(value='qty_invoiced', kind=None),
                                Constant(value='qty_delivered', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_to_invoice_qty',
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
                            value=Constant(value='\n        Compute the quantity to invoice. If the invoice policy is order, the quantity to invoice is\n        calculated from the ordered quantity. Otherwise, the quantity delivered is used.\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='state',
                                            ctx=Load(),
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
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='invoice_policy',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='order', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_to_invoice',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_uom_qty',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_to_invoice',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_delivered',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_to_invoice',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='qty_invoiced', kind=None),
                                Constant(value='qty_delivered', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='order_id.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_invoiced',
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
                            value=Constant(value="\n        Compute the quantity invoiced. If case of a refund, the quantity invoiced is decreased. Note\n        that this is the case only if the refund is generated from the SO and that is intentional: if\n        a refund made would automatically decrease the invoiced quantity, then there is a risk of reinvoicing\n        it automatically, which may not be wanted at all. That's why the refund has to be created from the SO\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='qty_invoiced', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='invoice_line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_get_invoice_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice_line', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='cancel', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice_line', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='move_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='out_invoice', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='qty_invoiced', ctx=Store()),
                                                            op=Add(),
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='product_uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_compute_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='quantity',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_uom',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='move_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='out_refund', kind=None)],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='is_downpayment',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='untaxed_amount_to_invoice',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='qty_invoiced', ctx=Store()),
                                                                            op=Sub(),
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                                        attr='product_uom_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_compute_quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                                        attr='quantity',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_uom',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='qty_invoiced',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='qty_invoiced', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='invoice_lines.move_id.state', kind=None),
                                Constant(value='invoice_lines.quantity', kind=None),
                                Constant(value='untaxed_amount_to_invoice', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_lines',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='accrual_entry_date', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='invoice_lines',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='l', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='invoice_date',
                                                            ctx=Load(),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='l', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='invoice_date',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[LtE()],
                                                            comparators=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='accrual_entry_date', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice_lines',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_price_reduce',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price_reduce',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            left=Constant(value=1.0, kind=None),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='discount',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='price_unit', kind=None),
                                Constant(value='discount', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_price_reduce_taxinc',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price_reduce_taxinc',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='price_total',
                                                ctx=Load(),
                                            ),
                                            op=Div(),
                                            right=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='price_total', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_price_reduce_taxexcl',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price_reduce_taxexcl',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                        body=BinOp(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='price_subtotal',
                                                ctx=Load(),
                                            ),
                                            op=Div(),
                                            right=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                        ),
                                        orelse=Constant(value=0.0, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='price_subtotal', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_tax_id',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='fiscal_position_id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='fiscal_position_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_fiscal_position',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='order_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
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
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='tax_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fpos', ctx=Load()),
                                            attr='map_tax',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='taxes', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                FunctionDef(
                    name='_prepare_add_missing_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Deduce missing required fields from the onchange ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='onchange_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='name', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='tax_id', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='order_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='product_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='f', ctx=Load()),
                                                    ops=[NotIn()],
                                                    comparators=[Name(id='values', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=Name(id='onchange_fields', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id_change',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='onchange_fields', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='values', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='_fields',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='field', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='convert_to_write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Name(id='field', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='line', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='display_type', kind=None),
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='default_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[Constant(value='display_type', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value='display_type', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='product_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='price_unit',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='product_uom_qty',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='product_uom',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='customer_lead',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_add_missing_fields',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
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
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='lines', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sale', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Extra line with %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
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
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='msg', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='expense_policy',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='no', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='analytic_account_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_create_analytic_account',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='accountable_required_fields', kind=None),
                                    Constant(value='CHECK(display_type IS NOT NULL OR (product_id IS NOT NULL AND product_uom IS NOT NULL))', kind=None),
                                    Constant(value='Missing required fields on accountable sale order line.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='non_accountable_null_fields', kind=None),
                                    Constant(value='CHECK(display_type IS NULL OR (product_id IS NULL AND price_unit = 0 AND product_uom_qty = 0 AND product_uom IS NULL AND customer_lead = 0))', kind=None),
                                    Constant(value='Forbidden values on non-accountable sale order line', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_line_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='order_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='orders', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='order_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='order', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Constant(value='<b>', kind=None),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The ordered quantity has been updated.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value='</b><ul>', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Name(id='order_lines', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='msg', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='<li> %s: <br/>', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='display_name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='msg', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Ordered Quantity: %(old_qty)s -> %(new_qty)s', kind=None)],
                                                    keywords=[
                                                        keyword(
                                                            arg='old_qty',
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_uom_qty',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='new_qty',
                                                            value=Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='product_uom_qty', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                op=Add(),
                                                right=Constant(value='<br/>', kind=None),
                                            ),
                                        ),
                                        If(
                                            test=Compare(
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='consu', kind=None),
                                                            Constant(value='product', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='msg', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[
                                                                Constant(value='Delivered Quantity: %s', kind=None),
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='qty_delivered',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='<br/>', kind=None),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='msg', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='Invoiced Quantity: %s', kind=None),
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value='<br/>', kind=None),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='msg', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='</ul>', kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Name(id='msg', ctx=Load()),
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
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='display_type', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='display_type', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You cannot change the type of a sale order line. Instead you should delete the current line and create a new line of the proper type.', kind=None)],
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
                        If(
                            test=Compare(
                                left=Constant(value='product_uom_qty', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='precision', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='decimal.precision', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='precision_get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Product Unit of Measure', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='r', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='sale', kind=None)],
                                                                ),
                                                                Compare(
                                                                    left=Call(
                                                                        func=Name(id='float_compare', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='r', ctx=Load()),
                                                                                attr='product_uom_qty',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Subscript(
                                                                                value=Name(id='values', ctx=Load()),
                                                                                slice=Constant(value='product_uom_qty', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='precision_digits',
                                                                                value=Name(id='precision', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value=0, kind=None)],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_update_line_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='protected_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_protected_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='done', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='order_id.state', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='f', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='keys',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=Name(id='protected_fields', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='protected_fields_modified', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[Name(id='protected_fields', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=BitAnd(),
                                                right=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='keys',
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.fields', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='protected_fields_modified', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_name',
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
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='It is forbidden to modify the following fields in a locked order:\n%s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value='\n', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='field_description', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sale.order', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Order Reference', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Description', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sequence', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_lines', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.move.line', kind=None),
                            Constant(value='sale_order_line_invoice_rel', kind=None),
                            Constant(value='order_line_id', kind=None),
                            Constant(value='invoice_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Lines', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_status', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='upselling', kind=None),
                                            Constant(value='Upselling Opportunity', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='invoiced', kind=None),
                                            Constant(value='Fully Invoiced', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='to invoice', kind=None),
                                            Constant(value='To Invoice', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='no', kind=None),
                                            Constant(value='Nothing to Invoice', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Status', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_invoice_status', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='no', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_unit', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Unit Price', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Price', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_subtotal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_amount', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Subtotal', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_tax', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_amount', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Tax', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_amount', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_reduce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_price_reduce', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Price Reduce', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Price', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.tax', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Taxes', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Constant(value='|', kind=None),
                                        Tuple(
                                            elts=[
                                                Constant(value='active', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='active', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=True, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_reduce_taxinc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_price_reduce_taxinc', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Price Reduce Tax inc', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_reduce_taxexcl', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_price_reduce_taxexcl', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Price Reduce Tax excl', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Discount (%)', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Discount', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='change_default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.template', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product Template', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.product_tmpl_id', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='sale_ok', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=True, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_updatable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_updatable', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Can Edit Product', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Quantity', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='uom.uom', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('category_id', '=', product_uom_category_id)]", kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_category_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.uom_id.category_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_readonly', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_uom_readonly', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_custom_attribute_value_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.attribute.custom.value', kind=None),
                            Constant(value='sale_order_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Custom Values', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_no_variant_attribute_value_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.template.attribute.value', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Extra Values', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_delivered_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='manual', kind=None),
                                            Constant(value='Manual', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='analytic', kind=None),
                                            Constant(value='Analytic From Expenses', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Method to update delivered qty', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_qty_delivered_method', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='According to product configuration, the delivered quantity can be automatically computed by mechanism :\n  - Manual: the quantity is set manually on the line\n  - Analytic From expenses: the quantity is the quantity sum from posted expenses\n  - Timesheet: the quantity is the sum of hours recorded on tasks linked to this sale line\n  - Stock Moves: the quantity comes from confirmed pickings\n', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_delivered', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Delivered Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_qty_delivered', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_qty_delivered', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_delivered_manual', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Delivered Manually', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_to_invoice', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_to_invoice_qty', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='To Invoice Quantity', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_qty_invoiced', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Invoiced Quantity', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='untaxed_amount_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Untaxed Invoiced Amount', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_untaxed_amount_invoiced', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='untaxed_amount_to_invoice', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Untaxed Amount To Invoice', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_untaxed_amount_to_invoice', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='salesman_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='order_id.user_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Salesperson', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='order_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='depends',
                                value=List(
                                    elts=[Constant(value='order_id.currency_id', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='order_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='order_partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='order_id.partner_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Customer', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='analytic_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.analytic.tag', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Tags', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='analytic_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.analytic.line', kind=None),
                            Constant(value='so_line', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic lines', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_expense', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is expense', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Is true if the sales order line comes from an expense or a vendor bills', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_downpayment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Is a down payment', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Down payments are made when creating invoices from a sales order. They are not copied when duplicating a sales order.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='order_id.state', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Order Status', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='customer_lead', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lead Time', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Number of days between the order confirmation and the shipping of the products to the customer', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='line_section', kind=None),
                                            Constant(value='Section', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='line_note', kind=None),
                                            Constant(value='Note', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field for UX purpose.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_packaging_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.packaging', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Packaging', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('sales', '=', True), ('product_id','=',product_id)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_packaging_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Packaging Quantity', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_product_uom_readonly',
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
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_readonly',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='sale', kind=None),
                                                    Constant(value='done', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='state', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_delivered_method',
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
                            value=Constant(value=" Sale module compute delivered qty for product [('type', 'in', ['consu']), ('service_type', '=', 'manual')]\n                - consu + expense_policy : analytic (sum of analytic unit_amount)\n                - consu + no expense_policy : manual (set manually on SOL)\n                - service (+ service_type='manual', the only available option) : manual\n\n            This is true when only sale is installed: sale_stock redifine the behavior for 'consu' type,\n            and sale_timesheet implements the behavior of 'service' + service_type=timesheet.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='is_expense',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered_method',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='analytic', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered_method',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='manual', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='state', kind=None),
                                Constant(value='is_expense', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_delivered',
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
                            value=Constant(value=' This method compute the delivered quantity of the SO lines: it covers the case provide by sale module, aka\n            expense/vendor bills (sum of unit_amount of AAL), and manual case.\n            This method should be overridden to provide other way to automatically compute delivered qty. Overrides should\n            take their concerned so lines, compute and set the `qty_delivered` field, and call super with the remaining\n            records.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lines_by_analytic', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='sol', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='sol', ctx=Load()),
                                                attr='qty_delivered_method',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='analytic', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lines_by_analytic', ctx=Load()),
                                    attr='_get_delivered_quantity_by_analytic',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='so_line', ctx=Store()),
                            iter=Name(id='lines_by_analytic', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='so_line', ctx=Load()),
                                            attr='qty_delivered',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mapping', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='so_line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='so_line', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0.0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='qty_delivered_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='manual', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='qty_delivered_manual',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='qty_delivered_method', kind=None),
                                Constant(value='qty_delivered_manual', kind=None),
                                Constant(value='analytic_line_ids.so_line', kind=None),
                                Constant(value='analytic_line_ids.unit_amount', kind=None),
                                Constant(value='analytic_line_ids.product_uom_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_delivered_quantity_by_analytic',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='additional_domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compute and write the delivered quantity of current SO lines, based on their related\n            analytic lines.\n            :param additional_domain: domain to restrict AAL to include in computation (required since timesheet is an AAL with a project ...)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='so_line', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='additional_domain', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='so_line', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='so_line', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lazy',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Subscript(
                                                value=Name(id='item', ctx=Load()),
                                                slice=Constant(value='so_line', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='item', ctx=Store()),
                                                iter=Name(id='data', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='lines_map', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='line', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Name(id='line', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='line', ctx=Store()),
                                        iter=Name(id='lines', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_uom_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Subscript(
                                        value=Name(id='item', ctx=Load()),
                                        slice=Constant(value='product_uom_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='item', ctx=Store()),
                                        iter=Name(id='data', ctx=Load()),
                                        ifs=[
                                            Subscript(
                                                value=Name(id='item', ctx=Load()),
                                                slice=Constant(value='product_uom_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_uom_map', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='uom', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Name(id='uom', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='uom', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='uom.uom', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='product_uom_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Name(id='data', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='item', ctx=Load()),
                                            slice=Constant(value='product_uom_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='so_line_id', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='item', ctx=Load()),
                                            slice=Constant(value='so_line', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='so_line', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='lines_map', ctx=Load()),
                                        slice=Name(id='so_line_id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='so_line_id', ctx=Load()),
                                            Constant(value=0.0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='uom', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product_uom_map', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value='product_uom_id', kind=None),
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='so_line', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='category_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='uom', ctx=Load()),
                                                attr='category_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='uom', ctx=Load()),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='item', ctx=Load()),
                                                        slice=Constant(value='unit_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='so_line', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='rounding_method',
                                                        value=Constant(value='HALF-UP', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='qty', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='item', ctx=Load()),
                                                slice=Constant(value='unit_amount', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Name(id='so_line_id', ctx=Load()),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Name(id='qty', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_inverse_qty_delivered',
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
                            value=Constant(value=" When writing on qty_delivered, if the value should be modify manually (`qty_delivered_method` = 'manual' only),\n            then we put the value in `qty_delivered_manual`. Otherwise, `qty_delivered_manual` should be False since the\n            delivered qty is automatically compute by other mecanisms.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='qty_delivered_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='manual', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='qty_delivered',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='qty_delivered', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_suggest_packaging',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_packaging_id',
                                        ctx=Load(),
                                    ),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='packaging_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='sales', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_find_suitable_product_packaging',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_id', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='product_uom', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_product_packaging_id',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_packaging_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='newqty', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_packaging_id',
                                                ctx=Load(),
                                            ),
                                            attr='_check_qty',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            Constant(value='UP', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='newqty', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='warning', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='title', kind=None),
                                                            Constant(value='message', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Warning', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='This product is packaged by %(pack_size).2f %(pack_name)s. You should sell %(quantity).2f %(unit)s.', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='pack_size',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_packaging_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='pack_name',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='uom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='quantity',
                                                                        value=Name(id='newqty', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='unit',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_uom',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_packaging_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_update_product_packaging_qty',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_packaging_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='packaging_uom', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='packaging_uom_qty', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Name(id='packaging_uom', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='packaging_uom_qty', ctx=Load()),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_packaging_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Name(id='packaging_uom', ctx=Load()),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_packaging_id', kind=None),
                                Constant(value='product_uom', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_product_packaging_qty',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_packaging_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='packaging_uom', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Load(),
                                        ),
                                        attr='product_uom_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty_per_packaging', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Load(),
                                        ),
                                        attr='qty',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product_uom_qty', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='packaging_uom', ctx=Load()),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_packaging_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='qty_per_packaging', ctx=Load()),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='product_uom_qty', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='rounding',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='product_uom_qty', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_packaging_qty', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_untaxed_amount_invoiced',
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
                            value=Constant(value=' Compute the untaxed amount already invoiced from the sale order line, taking the refund attached\n            the so line into account. This amount is computed as\n                SUM(inv_line.price_subtotal) - SUM(ref_line.price_subtotal)\n            where\n                `inv_line` is a customer invoice line linked to the SO line\n                `ref_line` is a customer credit note (refund) line linked to the SO line\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='amount_invoiced', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='invoice_line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_get_invoice_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice_line', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='posted', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='invoice_date', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='invoice_line', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='invoice_date',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice_line', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='move_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='out_invoice', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='amount_invoiced', ctx=Store()),
                                                            op=Add(),
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_convert',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='price_subtotal',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='invoice_date', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line', ctx=Load()),
                                                                        attr='move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='move_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='out_refund', kind=None)],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='amount_invoiced', ctx=Store()),
                                                                    op=Sub(),
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='invoice_line', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='invoice_line', ctx=Load()),
                                                                                attr='price_subtotal',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='company_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='invoice_date', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='untaxed_amount_invoiced',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='amount_invoiced', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='invoice_lines', kind=None),
                                Constant(value='invoice_lines.price_total', kind=None),
                                Constant(value='invoice_lines.move_id.state', kind=None),
                                Constant(value='invoice_lines.move_id.move_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_untaxed_amount_to_invoice',
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
                            value=Constant(value=" Total of remaining amount to invoice on the sale order line (taxes excl.) as\n                total_sol - amount already invoiced\n            where Total_sol depends on the invoice policy of the product.\n\n            Note: Draft invoice are ignored on purpose, the 'to invoice' amount should\n            come only from the SO lines.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='amount_to_invoice', ctx=Store())],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
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
                                        Assign(
                                            targets=[Name(id='price_subtotal', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='uom_qty_to_consider', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='invoice_policy',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='delivery', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_delivered',
                                                    ctx=Load(),
                                                ),
                                                orelse=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='price_reduce', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='price_unit',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Constant(value=1, kind=None),
                                                    op=Sub(),
                                                    right=BinOp(
                                                        left=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='discount',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=0.0, kind=None),
                                                            ],
                                                        ),
                                                        op=Div(),
                                                        right=Constant(value=100.0, kind=None),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='price_subtotal', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='price_reduce', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='uom_qty_to_consider', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='tax_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='tax', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Attribute(
                                                                        value=Name(id='tax', ctx=Load()),
                                                                        attr='price_include',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='price_subtotal', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='tax_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='compute_all',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='price_reduce', ctx=Load())],
                                                            keywords=[
                                                                keyword(
                                                                    arg='currency',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='order_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                keyword(
                                                                    arg='quantity',
                                                                    value=Name(id='uom_qty_to_consider', ctx=Load()),
                                                                ),
                                                                keyword(
                                                                    arg='product',
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                keyword(
                                                                    arg='partner',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='order_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='partner_shipping_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Constant(value='total_excluded', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='inv_lines', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_get_invoice_lines',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='inv_lines', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='l', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='l', ctx=Load()),
                                                                        attr='discount',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotEq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='discount',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='amount', ctx=Store())],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='l', ctx=Store()),
                                                    iter=Name(id='inv_lines', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='tax_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='tax', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Attribute(
                                                                                        value=Name(id='tax', ctx=Load()),
                                                                                        attr='price_include',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='amount', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Subscript(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='tax_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='compute_all',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                BinOp(
                                                                                    left=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                attr='currency_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='_convert',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='l', ctx=Load()),
                                                                                                attr='price_unit',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='line', ctx=Load()),
                                                                                                attr='currency_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='line', ctx=Load()),
                                                                                                attr='company_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            BoolOp(
                                                                                                op=Or(),
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='l', ctx=Load()),
                                                                                                        attr='date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='fields', ctx=Load()),
                                                                                                                attr='Date',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='today',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='round',
                                                                                                value=Constant(value=False, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    op=Mult(),
                                                                                    right=Attribute(
                                                                                        value=Name(id='l', ctx=Load()),
                                                                                        attr='quantity',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        slice=Constant(value='total_excluded', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                AugAssign(
                                                                    target=Name(id='amount', ctx=Store()),
                                                                    op=Add(),
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='currency_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='_convert',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='l', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='currency_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='company_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                BoolOp(
                                                                                    op=Or(),
                                                                                    values=[
                                                                                        Attribute(
                                                                                            value=Name(id='l', ctx=Load()),
                                                                                            attr='date',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='fields', ctx=Load()),
                                                                                                    attr='Date',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='today',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='round',
                                                                                    value=Constant(value=False, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Attribute(
                                                                            value=Name(id='l', ctx=Load()),
                                                                            attr='quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='amount_to_invoice', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='price_subtotal', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='amount', ctx=Load()),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='amount_to_invoice', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='price_subtotal', ctx=Load()),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='untaxed_amount_invoiced',
                                                            ctx=Load(),
                                                        ),
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
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='untaxed_amount_to_invoice',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='amount_to_invoice', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='state', kind=None),
                                Constant(value='price_reduce', kind=None),
                                Constant(value='product_id', kind=None),
                                Constant(value='untaxed_amount_invoiced', kind=None),
                                Constant(value='qty_delivered', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_invoice_line_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new', annotation=None, type_comment=None),
                            arg(arg='old', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Method intended to be overridden in third-party module if we want to prevent the resequencing\n        of invoice lines.\n\n        :param int new:   the new line sequence\n        :param int old:   the old line sequence\n\n        :return:          the sequence of the SO line, by default the new one.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='new', ctx=Load()),
                                    Name(id='old', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_invoice_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='optional_values', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Prepare the dict of values to create the new invoice line for a sales order line.\n\n        :param qty: float quantity to invoice\n        :param optional_values: any parameter that should be added to the returned invoice line\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='display_type', kind=None),
                                    Constant(value='sequence', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_uom_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='discount', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='tax_ids', kind=None),
                                    Constant(value='analytic_account_id', kind=None),
                                    Constant(value='analytic_tag_ids', kind=None),
                                    Constant(value='sale_line_ids', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='display_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='qty_to_invoice',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='discount',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='price_unit',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tax_id',
                                                            ctx=Load(),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='analytic_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='analytic_tag_ids',
                                                            ctx=Load(),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=4, kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='optional_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='optional_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='display_type',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='account_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_procurement_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='group_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare specific key for moves or other components that will be created from a stock rule\n        comming from a sale order line. This method could be override in order to add other custom key that could\n        be used in move/po creation.\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_display_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='no_variant_attributes_price_extra', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='ptav', ctx=Load()),
                                    attr='price_extra',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='ptav', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_no_variant_attribute_value_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='ptav', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='ptav', ctx=Load()),
                                                                attr='price_extra',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Name(id='ptav', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='product_template_attribute_value_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
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
                        If(
                            test=Name(id='no_variant_attributes_price_extra', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='no_variant_attributes_price_extra',
                                                value=Call(
                                                    func=Name(id='tuple', ctx=Load()),
                                                    args=[Name(id='no_variant_attributes_price_extra', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='pricelist_id',
                                        ctx=Load(),
                                    ),
                                    attr='discount_policy',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='with_discount', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='pricelist',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='pricelist_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='uom',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        attr='price',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='product_context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='date',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='date_order',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='uom',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
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
                                Tuple(
                                    elts=[
                                        Name(id='final_price', ctx=Store()),
                                        Name(id='rule_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get_product_price_rule',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='product', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='base_price', ctx=Store()),
                                        Name(id='currency', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_get_real_price_currency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product', ctx=Load()),
                                    Name(id='rule_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='pricelist_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='currency', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='pricelist_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='base_price', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='base_price', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pricelist_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
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
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='date_order',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Name(id='base_price', ctx=Load()),
                                    Name(id='final_price', ctx=Load()),
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
                    name='product_id_change',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='valid_values', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='product_tmpl_id',
                                        ctx=Load(),
                                    ),
                                    attr='valid_product_template_attribute_line_ids',
                                    ctx=Load(),
                                ),
                                attr='product_template_value_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='pacv', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_custom_attribute_value_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='pacv', ctx=Load()),
                                            attr='custom_product_template_attribute_value_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='valid_values', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_custom_attribute_value_ids',
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=Name(id='pacv', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ptav', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_no_variant_attribute_value_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='ptav', ctx=Load()),
                                            attr='_origin',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='valid_values', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_no_variant_attribute_value_ids',
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=Name(id='ptav', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='product_uom', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='uom_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='product_uom_qty', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Attribute(
                                            value=Call(
                                                func=Name(id='get_lang', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='lang',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='quantity',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='product_uom_qty', kind=None)],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='date',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='date_order',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='pricelist',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='uom',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_sale_order_line_multiline_description_sale',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='product', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_tax_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='pricelist_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='price_unit', kind=None),
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
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_fix_tax_included_price_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_display_price',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='product', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='taxes_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='product', ctx=Load()),
                                    attr='sale_line_warn',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='no-message', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='sale_line_warn',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='block', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='warning', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Warning for %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='sale_line_warn_msg',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='product_uom_change',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0.0, kind=None),
                                    type_comment=None,
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='pricelist_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='partner',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='date',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='date_order',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='pricelist',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='pricelist_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='uom',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='fiscal_position',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='context',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='fiscal_position', kind=None)],
                                                    keywords=[],
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
                                            attr='price_unit',
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
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_fix_tax_included_price_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_display_price',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='product', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='taxes_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_uom', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name_get',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='so_line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s - %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='so_line', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='so_line', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='so_line', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='split',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='\n', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='so_line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line', ctx=Load()),
                                            attr='order_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s (%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Load()),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='so_line', ctx=Load()),
                                                                attr='order_partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='so_line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_name_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='name_get_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='ilike', kind=None),
                            Constant(value=100, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='ilike', kind=None),
                                            Constant(value='like', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='=like', kind=None),
                                            Constant(value='=ilike', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='args', ctx=Load()),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='order_id.name', kind=None),
                                                                    Name(id='operator', ctx=Load()),
                                                                    Name(id='name', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Name(id='operator', ctx=Load()),
                                                                    Name(id='name', ctx=Load()),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_name_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='args',
                                        value=Name(id='args', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='operator',
                                        value=Name(id='operator', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='name_get_uid',
                                        value=Name(id='name_get_uid', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_line_unlink',
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
                            value=Constant(value='\n        Check wether a line can be deleted or not.\n\n        Lines cannot be deleted if the order is confirmed; downpayment\n        lines who have not yet been invoiced bypass that exception.\n        :rtype: recordset sale.order.line\n        :returns: set of lines that cannot be deleted\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='sale', kind=None),
                                                                Constant(value='done', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='invoice_lines',
                                                            ctx=Load(),
                                                        ),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='is_downpayment',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
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
                    name='_unlink_except_confirmed',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_line_unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You can not remove an order line once the sales order is confirmed.\nYou should rather set the quantity to 0.', kind=None)],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_real_price_currency',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='rule_id', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='uom', annotation=None, type_comment=None),
                            arg(arg='pricelist_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Retrieve the price before applying the pricelist\n            :param obj product: object of current product record\n            :parem float qty: total quentity of product\n            :param tuple price_and_rule: tuple(price, suitable_rule) coming from pricelist computation\n            :param obj uom: unit of measure of current order line\n            :param integer pricelist_id: pricelist id of sales order', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='PricelistItem', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.pricelist.item', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_name', ctx=Store())],
                            value=Constant(value='lst_price', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_id', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_currency', ctx=Store())],
                            value=Attribute(
                                value=Name(id='product', ctx=Load()),
                                attr='currency_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='rule_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pricelist_item', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='PricelistItem', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rule_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='pricelist_item', ctx=Load()),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='discount_policy',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='without_discount', kind=None)],
                                    ),
                                    body=[
                                        While(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='pricelist_item', ctx=Load()),
                                                            attr='base',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='pricelist', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='pricelist_item', ctx=Load()),
                                                        attr='base_pricelist_id',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pricelist_item', ctx=Load()),
                                                                attr='base_pricelist_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='discount_policy',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='without_discount', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='_price', ctx=Store()),
                                                                Name(id='rule_id', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='pricelist_item', ctx=Load()),
                                                                        attr='base_pricelist_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='uom',
                                                                        value=Attribute(
                                                                            value=Name(id='uom', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='get_product_price_rule',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='product', ctx=Load()),
                                                            Name(id='qty', ctx=Load()),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='pricelist_item', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='PricelistItem', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='rule_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='pricelist_item', ctx=Load()),
                                            attr='base',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='standard_price', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Constant(value='standard_price', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='product_currency', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='cost_currency_id',
                                                ctx=Load(),
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
                                                        left=Attribute(
                                                            value=Name(id='pricelist_item', ctx=Load()),
                                                            attr='base',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='pricelist', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='pricelist_item', ctx=Load()),
                                                        attr='base_pricelist_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='field_name', ctx=Store())],
                                                    value=Constant(value='price', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='product', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='pricelist',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='pricelist_item', ctx=Load()),
                                                                        attr='base_pricelist_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='product_currency', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='pricelist_item', ctx=Load()),
                                                            attr='base_pricelist_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='currency_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='pricelist_item', ctx=Load()),
                                            attr='pricelist_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='currency_id', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='currency_id', ctx=Store())],
                                    value=Name(id='product_currency', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cur_factor', ctx=Store())],
                                    value=Constant(value=1.0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='currency_id', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='product_currency', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cur_factor', ctx=Store())],
                                            value=Constant(value=1.0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='cur_factor', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='currency_id', ctx=Load()),
                                                    attr='_get_conversion_rate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='product_currency', ctx=Load()),
                                                    Name(id='currency_id', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
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
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='date_order',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='product_uom', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='uom', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='uom', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='product_uom', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='uom_factor', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='uom', ctx=Load()),
                                            attr='_compute_price',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1.0, kind=None),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='uom_factor', ctx=Store())],
                                    value=Constant(value=1.0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    BinOp(
                                        left=BinOp(
                                            left=Subscript(
                                                value=Name(id='product', ctx=Load()),
                                                slice=Name(id='field_name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            op=Mult(),
                                            right=Name(id='uom_factor', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='cur_factor', ctx=Load()),
                                    ),
                                    Name(id='currency_id', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_protected_fields',
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
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='tax_id', kind=None),
                                    Constant(value='analytic_tag_ids', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_product_id_set_customer_lead',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_discount',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='pricelist_id',
                                            ctx=Load(),
                                        ),
                                        Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pricelist_id',
                                                    ctx=Load(),
                                                ),
                                                attr='discount_policy',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='without_discount', kind=None)],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='product.group_discount_per_so_line', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='discount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='quantity',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='date',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='date_order',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='pricelist',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='uom',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fiscal_position',
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='fiscal_position', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='date',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='date_order',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='uom',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
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
                                Tuple(
                                    elts=[
                                        Name(id='price', ctx=Store()),
                                        Name(id='rule_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get_product_price_rule',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='new_list_price', ctx=Store()),
                                        Name(id='currency', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_get_real_price_currency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product', ctx=Load()),
                                    Name(id='rule_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='pricelist_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='new_list_price', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='pricelist_id',
                                                ctx=Load(),
                                            ),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='currency', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_list_price', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='currency', ctx=Load()),
                                                    attr='_convert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='new_list_price', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='pricelist_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
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
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='date_order',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='discount', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='new_list_price', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='price', ctx=Load()),
                                            ),
                                            op=Div(),
                                            right=Name(id='new_list_price', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=100, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='discount', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='new_list_price', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='discount', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='new_list_price', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='discount',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='discount', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_id', kind=None),
                                Constant(value='price_unit', kind=None),
                                Constant(value='product_uom', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='tax_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_delivery',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_sale_order_line_multiline_description_sale',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compute a default multiline description for this sales order line.\n\n        In most cases the product description is enough but sometimes we need to append information that only\n        exists on the sale order line itself.\n        e.g:\n        - custom attributes and attributes that don\'t create variants, both introduced by the "product configurator"\n        - in event_sale we need to know specifically the sales order line as well as the product to generate the name:\n          the product is not sufficient because we also need to know the event_id and the event_ticket_id (both which belong to the sale order line).\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='get_product_multiline_description_sale',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_sale_order_line_multiline_description_variants',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_sale_order_line_multiline_description_variants',
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
                            value=Constant(value='When using no_variant attributes or is_custom values, the product\n        itself is not sufficient to create the description: we need to add\n        information about those special attributes and values.\n\n        :return: the description related to special variant attributes/values\n        :rtype: string\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_custom_attribute_value_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_no_variant_attribute_value_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Constant(value='\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='custom_ptavs', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_custom_attribute_value_ids',
                                    ctx=Load(),
                                ),
                                attr='custom_product_template_attribute_value_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='no_variant_ptavs', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_no_variant_attribute_value_ids',
                                    ctx=Load(),
                                ),
                                attr='_origin',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ptav', ctx=Store()),
                            iter=BinOp(
                                left=Name(id='no_variant_ptavs', ctx=Load()),
                                op=Sub(),
                                right=Name(id='custom_ptavs', ctx=Load()),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='name', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='\n', kind=None),
                                        op=Add(),
                                        right=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ptav', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='display_name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='custom_values', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_custom_attribute_value_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='r', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='custom_product_template_attribute_value_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='pacv', ctx=Store()),
                            iter=Name(id='custom_values', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='name', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='\n', kind=None),
                                        op=Add(),
                                        right=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pacv', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='order_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='display_name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='name', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_not_sellable_line',
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
                        Return(
                            value=Constant(value=False, kind=None),
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
