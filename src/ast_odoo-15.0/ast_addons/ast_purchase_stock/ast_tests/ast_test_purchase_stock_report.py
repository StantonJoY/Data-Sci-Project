Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.stock.tests.test_report',
            names=[alias(name='TestReportsCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPurchaseStockReports',
            bases=[Name(id='TestReportsCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_report_forecast_1_purchase_order_multi_receipt',
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
                            value=Constant(value=' Create a PO for 5 product, receive them then increase the quantity to 10.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
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
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Must have 0 line for now.', kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
                                    Constant(value=5, kind=None),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='document_in', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='po', ctx=Load()),
                                        attr='id',
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='quantity', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='document_out', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='receipt', ctx=Store())],
                            value=Attribute(
                                value=Name(id='po', ctx=Load()),
                                attr='picking_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_dict', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='receipt', ctx=Load()),
                                    attr='button_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Subscript(
                                                            value=Name(id='res_dict', ctx=Load()),
                                                            slice=Constant(value='res_model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='res_dict', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='save',
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='po', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=10, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Must have 1 line for now.', kind=None),
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
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='document_in', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='po', ctx=Load()),
                                        attr='id',
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='quantity', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
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
                    name='test_report_forecast_2_purchase_order_three_step_receipt',
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
                            value=Constant(value=' Create a PO for 4 product, receive them then increase the quantity\n        to 10, but use three steps receipt.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='grp_multi_loc', ctx=Store())],
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
                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grp_multi_routes', ctx=Store())],
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
                                args=[Constant(value='stock.group_adv_location', kind=None)],
                                keywords=[],
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
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='grp_multi_loc', ctx=Load()),
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
                                ],
                                keywords=[],
                            ),
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
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='grp_multi_routes', ctx=Load()),
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
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='warehouse', ctx=Store())],
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
                                args=[Constant(value='stock.warehouse0', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='warehouse', ctx=Load()),
                                    attr='reception_steps',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='three_steps', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
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
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=4, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Must have 0 line for now.', kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
                                    Constant(value=4, kind=None),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='document_in', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='po', ctx=Load()),
                                        attr='id',
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='quantity', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='document_out', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='receipt', ctx=Store())],
                            value=Attribute(
                                value=Name(id='po', ctx=Load()),
                                attr='picking_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_dict', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='receipt', ctx=Load()),
                                    attr='button_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Subscript(
                                                            value=Name(id='res_dict', ctx=Load()),
                                                            slice=Constant(value='res_model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='res_dict', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='save',
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='po', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='edit',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=10, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='report_values', ctx=Store()),
                                        Name(id='docs', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_report_forecast',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='product_template_ids',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_template',
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
                            targets=[Name(id='draft_picking_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='draft_picking_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draft_purchase_qty', ctx=Store())],
                            value=Subscript(
                                value=Name(id='docs', ctx=Load()),
                                slice=Constant(value='draft_purchase_qty', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pending_qty_in', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='docs', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='document_in', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='po', ctx=Load()),
                                        attr='id',
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='quantity', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=6, kind=None),
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
                                    Name(id='draft_picking_qty_in', ctx=Load()),
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
                                    Name(id='draft_purchase_qty', ctx=Load()),
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
                                    Name(id='pending_qty_in', ctx=Load()),
                                    Constant(value=0, kind=None),
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
                    name='test_report_forecast_3_report_line_corresponding_to_po_line_highlighted',
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
                            value=Constant(value=' When accessing the report from a PO line, checks if the correct PO line is highlighted in the report\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
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
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='partner',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='po1', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='po2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po1', ctx=Load()),
                                    attr='copy',
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
                                    value=Name(id='po2', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='po', ctx=Store()),
                            iter=List(
                                elts=[
                                    Name(id='po1', ctx=Load()),
                                    Name(id='po2', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='context', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='po', ctx=Load()),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='action_product_forecast_report',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='context', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                                Name(id='lines', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_report_forecast',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='product_template_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_template',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='context',
                                                value=Name(id='context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Name(id='lines', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='document_in', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='po', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertTrue',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Constant(value='is_matched', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='The corresponding PO line should be matched in the forecast report.', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertFalse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Constant(value='is_matched', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='A line of the forecast report not linked to the PO shoud not be matched.', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
