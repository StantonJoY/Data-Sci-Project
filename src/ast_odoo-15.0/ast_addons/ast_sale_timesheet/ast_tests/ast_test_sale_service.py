Module(
    body=[
        ImportFrom(
            module='odoo.addons.sale_timesheet.tests.common',
            names=[alias(name='TestCommonSaleTimesheet', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSaleService',
            bases=[Name(id='TestCommonSaleTimesheet', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' This test suite provide checks for miscellaneous small things. ', kind=None),
                ),
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
                                    attr='sale_order',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sale.order', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_notrack',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='mail_create_nolog',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='partner_invoice_id', kind=None),
                                            Constant(value='partner_shipping_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
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
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sale_service',
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
                            value=Constant(value=' Test task creation when confirming a sale_order with the corresponding product ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sale_order_line', ctx=Store())],
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
                                            Constant(value='order_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet2',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_product_updatable',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='product_updatable',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_product_updatable',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_product_updatable',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='product_updatable',
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='invoice_status',
                                        ctx=Load(),
                                    ),
                                    Constant(value='no', kind=None),
                                    Constant(value='Sale Service: there should be nothing to invoice after validation', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='project_global',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='task_ids',
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
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                BinOp(
                                                    left=Constant(value='%s: %s', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sale_order',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_delivery_timesheet2',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                                args=[
                                    Name(id='task', ctx=Load()),
                                    Constant(value='Sale Service: task is not created, or it badly named', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Sale Service: customer should be the same on task and on SO', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='email_from',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_order',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Sale Service: Task Email should be the same as the SO customer Email', kind=None),
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
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_manager',
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='invoice_status',
                                        ctx=Load(),
                                    ),
                                    Constant(value='to invoice', kind=None),
                                    Constant(value='Sale Service: there should be sale_ordermething to invoice after registering timesheets', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='_create_invoices',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='sale_order_line', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                        ops=[
                                            Eq(),
                                            Eq(),
                                        ],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='sale_order_line', ctx=Load()),
                                                attr='qty_delivered',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='sale_order_line', ctx=Load()),
                                                attr='qty_invoiced',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Sale Service: line should be invoiced completely', kind=None),
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='invoice_status',
                                        ctx=Load(),
                                    ),
                                    Constant(value='invoiced', kind=None),
                                    Constant(value='Sale Service: SO should be invoiced', kind=None),
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='tasks_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='A task should have been created on SO confirmation.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='product_service_task', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='invoice_policy', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='service_type', kind=None),
                                            Constant(value='service_tracking', kind=None),
                                            Constant(value='project_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Delivered Service', kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=90, kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='delivery', kind=None),
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
                                                    args=[Constant(value='uom.product_uom_hour', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='uom.product_uom_hour', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='SERV-DELI', kind=None),
                                            Constant(value='timesheet', kind=None),
                                            Constant(value='task_global_project', kind=None),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='product_service_task', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product_service_task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='product_service_task', ctx=Load()),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product_service_task', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='tasks_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Adding a new service line on a confirmer SO should create a new task.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='timesheet_ids',
                                        ctx=Load(),
                                    ),
                                    attr='unlink',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_timesheet_uom',
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
                            value=Constant(value=' Test timesheet invoicing and uom conversion ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_days', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_day', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_order_line', ctx=Store())],
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
                                            Constant(value='order_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Name(id='uom_days', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
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
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='sale_order_line', ctx=Load()),
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
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=16, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_manager',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Sale: uom conversion of timesheets is wrong', kind=None),
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
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=24, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='_create_invoices',
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='invoice_status',
                                        ctx=Load(),
                                    ),
                                    Constant(value='invoiced', kind=None),
                                    Constant(value='Sale Timesheet: "invoice on delivery" timesheets should not modify the invoice_status of the so', kind=None),
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
                    name='test_task_so_line_assignation',
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
                            targets=[Name(id='so_line_deliver_global_project', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet2',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Name(id='so_line_deliver_global_project', ctx=Load()),
                                    attr='product_id_change',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_serv2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
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
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='so_line_deliver_global_project', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheets', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.analytic.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='timesheets', ctx=Store()),
                            op=BitOr(),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_serv2', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
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
                        AugAssign(
                            target=Name(id='timesheets', ctx=Store()),
                            op=BitOr(),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_serv2', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_manager',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Compare(
                                                    left=Name(id='billing_type', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='billable_time', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='billing_type', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='timesheets', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='timesheet_invoice_type', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value="All timesheets linked to the task should be on 'billable time'", kind=None),
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
                                        value=Name(id='so_line_deliver_global_project', ctx=Load()),
                                        attr='qty_to_invoice',
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
                                    Constant(value='Quantity to invoice should have been increased when logging timesheet on delivered quantities task', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='_create_invoices',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task_serv2', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
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
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Compare(
                                                    left=Name(id='billing_type', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='billable_time', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='billing_type', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='timesheets', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='timesheet_invoice_type', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='billable type of timesheet should not change when tranfering task into another project', kind=None),
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
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='timesheet_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='so_line', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='so_line_deliver_global_project', ctx=Load()),
                                    Constant(value='Old invoiced timesheet are not modified when changing the task SO line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='timesheets', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='so_line', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_delivered_quantity',
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
                            targets=[Name(id='so_line_deliver_new_task_project', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                    attr='product_id_change',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_serv2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
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
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='timesheet1', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_serv2', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='timesheet1', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Delivered quantity should be the same then its only related timesheet.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timesheet1', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                    Constant(value='Delivered quantity should be reset to zero, since there is no more timesheet.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='timesheet2', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line 2', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_serv2', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
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
                            targets=[Name(id='timesheet3', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Line 3', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='task_serv2', ctx=Load()),
                                                    attr='project_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task_serv2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='employee_user',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='timesheet2', ctx=Load()),
                                            attr='unit_amount',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='timesheet3', ctx=Load()),
                                            attr='unit_amount',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='Delivered quantity should be the sum of the 2 timesheets unit amounts.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timesheet2', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                        attr='qty_delivered',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='timesheet3', ctx=Load()),
                                        attr='unit_amount',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Delivered quantity should be reset to the sum of remaining timesheets unit amounts.', kind=None),
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
                    name='test_sale_create_task',
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
                            value=Constant(value=' Check that confirming SO create correctly a task, and reconfirming it does not create a second one. Also check changing\n            the ordered quantity of a SO line that have created a task should update the planned hours of this task.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='so_line1', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=7, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO confirmation should create a task and link it to SOL', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO confirmation should create a project and link it to SOL', kind=None),
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='tasks_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='The SO should have only one task', kind=None),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line1', ctx=Load()),
                                    Constant(value='The created task is also linked to its origin sale line, for invoicing purpose.', kind=None),
                                ],
                                keywords=[],
                            ),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The created task should be unassigned', kind=None),
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should be the same as the ordered quantity of the native SO line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='so_line1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_uom_qty', kind=None)],
                                        values=[Constant(value=20, kind=None)],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should have changed when updating the ordered quantity of the native SO line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_cancel',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO cancellation should keep the task', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO cancellation should create a project', kind=None),
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='tasks_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='The SO should still have only one task', kind=None),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line1', ctx=Load()),
                                    Constant(value='The created task is also linked to its origin sale line, for invoicing purpose.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='so_line1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_uom_qty', kind=None)],
                                        values=[Constant(value=30, kind=None)],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should have changed when updating the ordered quantity, even after SO cancellation', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_draft',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO reconfirmation should not have create another task', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='SO reconfirmation should bit have create another project', kind=None),
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
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='tasks_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='The SO should still have only one task', kind=None),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line1', ctx=Load()),
                                    Constant(value='The created task is also linked to its origin sale line, for invoicing purpose.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_done',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='product_uom_qty', kind=None)],
                                                values=[Constant(value=20, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sale_create_project',
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
                            value=Constant(value=" A SO with multiple product that should create project (with and without template) like ;\n                Line 1 : Service 1 create project with Template A ===> project created with template A\n                Line 2 : Service 2 create project no template ==> empty project created\n                Line 3 : Service 3 create project with Template A ===> Don't create any project because line 1 has already created a project with template A\n                Line 4 : Service 4 create project no template ==> Don't create any project because line 2 has already created an empty project\n                Line 5 : Service 5 create project with Template B ===> project created with template B\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='project_template2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.project', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='allow_timesheets', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Second Project TEMPLATE for services', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Stage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_project_id',
                                        value=Attribute(
                                            value=Name(id='project_template2', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stage1_tmpl2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Stage 1', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stage2_tmpl2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Stage', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Stage 2', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_deli_ts_tmpl', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='invoice_policy', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='service_type', kind=None),
                                            Constant(value='service_tracking', kind=None),
                                            Constant(value='project_template_id', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                            Constant(value='property_account_income_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Service delivered, create project only based on template B', kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=34, kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='delivery', kind=None),
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
                                                    args=[Constant(value='uom.product_uom_hour', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='uom.product_uom_hour', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='SERV-DELI4', kind=None),
                                            Constant(value='timesheet', kind=None),
                                            Constant(value='project_only', kind=None),
                                            Attribute(
                                                value=Name(id='project_template2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='account_sale',
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
                            targets=[Name(id='so_line1', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=11, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet5',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line2', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_order_timesheet4',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line3', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet5',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet5',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line4', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_manual3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_manual3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line5', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='product_deli_ts_tmpl', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product_deli_ts_tmpl', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=8, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='product_deli_ts_tmpl', ctx=Load()),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='product_deli_ts_tmpl', ctx=Load()),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line1 should have create a project based on template A', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line2', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line2 should have create an empty project', kind=None),
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
                                        value=Name(id='so_line3', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line3 should reuse project of line1', kind=None),
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
                                        value=Name(id='so_line4', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='so_line2', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line4 should reuse project of line2', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line4', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line4 should have create a new task, even if no project created.', kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line5', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Line5 should have create a project based on template B', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Project of Line1 should be active', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line2', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Project of Line2 should be active', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line5', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Project of Line5 should be active', kind=None),
                                ],
                                keywords=[],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_template_state',
                                                    ctx=Load(),
                                                ),
                                                attr='project_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Stage 1 from template B should be part of project from so line 1', kind=None),
                                ],
                                keywords=[],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_template_state',
                                                    ctx=Load(),
                                                ),
                                                attr='project_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Stage 1 from template B should be part of project from so line 1', kind=None),
                                ],
                                keywords=[],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='so_line5', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='stage1_tmpl2', ctx=Load()),
                                                attr='project_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Stage 1 from template B should be part of project from so line 5', kind=None),
                                ],
                                keywords=[],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='so_line5', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='stage2_tmpl2', ctx=Load()),
                                                attr='project_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Stage 2 from template B should be part of project from so line 5', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='allow_timesheets',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Create project should allow timesheets', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line2', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='allow_timesheets',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Create project should allow timesheets', kind=None),
                                ],
                                keywords=[],
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
                                        value=Attribute(
                                            value=Name(id='so_line5', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='allow_timesheets',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Create project should allow timesheets', kind=None),
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
                                            value=Name(id='so_line4', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='so_line2', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Task created with line 4 should have the project based on template A of the SO.', kind=None),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line1', ctx=Load()),
                                    Constant(value='SO line of project with template A should be the one that create it.', kind=None),
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
                                            value=Name(id='so_line2', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line2', ctx=Load()),
                                    Constant(value='SO line of project should be the one that create it.', kind=None),
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
                                            value=Name(id='so_line5', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line5', ctx=Load()),
                                    Constant(value='SO line of project with template B should be the one that create it.', kind=None),
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
                    name='test_sale_task_in_project_with_project',
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
                            value=Constant(value=" This will test the new 'task_in_project' service tracking correctly creates tasks and projects\n            when a project_id is configured on the parent sale_order (ref task #1915660).\n\n            Setup:\n            - Configure a project_id on the SO\n            - SO line 1: a product with its delivery tracking set to 'task_in_project'\n            - SO line 2: the same product as SO line 1\n            - SO line 3: a product with its delivery tracking set to 'project_only'\n            - Confirm sale_order\n\n            Expected result:\n            - 2 tasks created on the project_id configured on the SO\n            - 1 project created with the correct template for the 'project_only' product\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_global',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='_onchange_project_id',
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sale_order',
                                            ctx=Load(),
                                        ),
                                        attr='analytic_account_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='analytic_account_sale',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Changing the project on the SO should set the analytic account accordingly.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='so_line1', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=11, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_order_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line2', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_order_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line3', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_order_timesheet4',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet4',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_order_timesheet4',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_template_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_template',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_order_timesheet4',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_template_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value="so_line1 should create a task as its product's service_tracking is set as 'task_in_project'", kind=None),
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
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_global',
                                        ctx=Load(),
                                    ),
                                    Constant(value="The project on so_line1's task should be project_global as configured on its parent sale_order", kind=None),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line2', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value="so_line2 should create a task as its product's service_tracking is set as 'task_in_project'", kind=None),
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
                                            value=Name(id='so_line2', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_global',
                                        ctx=Load(),
                                    ),
                                    Constant(value="The project on so_line2's task should be project_global as configured on its parent sale_order", kind=None),
                                ],
                                keywords=[],
                            ),
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
                                            value=Name(id='so_line3', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value="so_line3 should not create a task as its product's service_tracking is set as 'project_only'", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line3', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_template',
                                        ctx=Load(),
                                    ),
                                    Constant(value='so_line3 should create a new project and not directly use the configured template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='project_template',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line3', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The created project for so_line3 should use the configured template', kind=None),
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
                    name='test_sale_task_in_project_without_project',
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
                            value=Constant(value=" This will test the new 'task_in_project' service tracking correctly creates tasks and projects\n            when the parent sale_order does NOT have a configured project_id (ref task #1915660).\n\n            Setup:\n            - SO line 1: a product with its delivery tracking set to 'task_in_project'\n            - Confirm sale_order\n\n            Expected result:\n            - 1 project created with the correct template for the 'task_in_project' because the SO\n              does not have a configured project_id\n            - 1 task created from this new project\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='so_line1', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_order_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_order_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_order_timesheet3',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_template_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_template',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_order_timesheet3',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='project_template_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
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
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='task_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value="so_line1 should create a task as its product's service_tracking is set as 'task_in_project'", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='so_line1', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_template',
                                        ctx=Load(),
                                    ),
                                    Constant(value='so_line1 should create a new project and not directly use the configured template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='project_template',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='so_line1', ctx=Load()),
                                            attr='project_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The created project for so_line1 should use the configured template', kind=None),
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
                    name='test_billable_task_and_subtask',
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
                            value=Constant(value=' Test if subtasks and tasks are billed on the correct SO line ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='so_line_deliver_new_task_project', ctx=Store())],
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
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                            targets=[Name(id='so_line_deliver_new_task_project_2', ctx=Store())],
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
                                        ],
                                        values=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='(2)', kind=None),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
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
                                    value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                    attr='product_id_change',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='so_line_deliver_new_task_project_2', ctx=Load()),
                                    attr='product_id_change',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='project', ctx=Store())],
                            value=Attribute(
                                value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Attribute(
                                value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                attr='task_id',
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
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                    Constant(value='The created project should be linked to the so line', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                    Constant(value='The created task should be linked to the so line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='subtask', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s: substask1', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='task', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='project_id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s: substask1', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='task', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                                    Attribute(
                                        value=Name(id='subtask', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='By, default, a child task should have the same SO line as its mother', kind=None),
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
                                        value=Name(id='task2', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='project', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='A new task in a billable project should have the same SO line as its project', kind=None),
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
                                        value=Name(id='task2', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                        attr='order_partner_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='A new task in a billable project should have the same SO line as its project', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subtask', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='display_project_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_global',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='subtask', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='A child task should always have the same SO line as its mother, even when changing project', kind=None),
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
                                        value=Name(id='subtask', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='so_line_deliver_new_task_project_2', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='subtask', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project', ctx=Load()),
                                    Constant(value='A child task is not impacted by the change of SO line of its mother', kind=None),
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project_2', ctx=Load()),
                                    Constant(value='A mother task can have its SO line set manually', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subtask', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='so_line_deliver_new_task_project_2', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='subtask', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='so_line_deliver_new_task_project_2', ctx=Load()),
                                    Constant(value='A child can have its SO line set manually', kind=None),
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
                    name='test_change_ordered_qty',
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
                            value=Constant(value=' Changing the ordered quantity of a SO line that have created a task should update the planned hours of this task ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sale_order_line', ctx=Store())],
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
                                            Constant(value='order_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet2',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet2',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
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
                                    Attribute(
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='sale_order_line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should be the same as the ordered quantity of the native SO line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sale_order_line', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_uom_qty', kind=None)],
                                        values=[Constant(value=20, kind=None)],
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
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='sale_order_line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should have changed when updating the ordered quantity of the native SO line', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sale_order_line', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_uom_qty', kind=None)],
                                        values=[Constant(value=30, kind=None)],
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
                                        value=Name(id='sale_order_line', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='sale_order_line', ctx=Load()),
                                            attr='task_id',
                                            ctx=Load(),
                                        ),
                                        attr='planned_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The planned hours should have changed when updating the ordered quantity, even after SO cancellation', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_done',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sale_order_line', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='product_uom_qty', kind=None)],
                                                values=[Constant(value=20, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_copy_billable_project_and_task',
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
                            targets=[Name(id='sale_order_line', ctx=Store())],
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
                                            Constant(value='order_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='price_unit', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sale_order',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_delivery_timesheet3',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_delivery_timesheet3',
                                                    ctx=Load(),
                                                ),
                                                attr='list_price',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sale_order',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
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
                                                    Constant(value='sale_line_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='sale_order_line', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project', ctx=Store())],
                            value=Attribute(
                                value=Name(id='sale_order_line', ctx=Load()),
                                attr='project_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='project_copy', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='project', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='project_copy', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Duplicating project should erase its Sale line', kind=None),
                                ],
                                keywords=[],
                            ),
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
                                        value=Name(id='project_copy', ctx=Load()),
                                        attr='sale_order_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Duplicating project should erase its Sale order', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='project', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='project_copy', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Copied project must have the same number of tasks', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='project_copy', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sale_line_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='The tasks of the duplicated project should not have a Sale Line set.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_copy', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task_copy', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='sale_line_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Duplicating task should keep its Sale line', kind=None),
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
                    name='test_remaining_hours_prepaid_services',
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
                            value=Constant(value=' Test if the remaining hours is correctly computed\n\n            Test Case:\n            =========\n            1) Check the remaining hours in the SOL containing a prepaid service product,\n            2) Create task in project with pricing type is equal to "task rate" and has the customer in the SO\n                and check if the remaining hours is equal to the remaining hours in the SOL,\n            3) Create timesheet in the task for this SOL and check if the remaining hours correctly decrease,\n            4) Change the SOL in the task and see if the remaining hours is correctly recomputed.\n            5) Create without storing the timesheet to check if remaining hours in SOL does not change.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='prepaid_service_sol', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so',
                                            ctx=Load(),
                                        ),
                                        attr='order_line',
                                        ctx=Load(),
                                    ),
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
                                                value=Attribute(
                                                    value=Name(id='sol', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='service_policy',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='ordered_timesheet', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='prepaid_service_sol', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='It should only have one SOL with prepaid service product in this SO.', kind=None),
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
                                        value=Name(id='prepaid_service_sol', ctx=Load()),
                                        attr='remaining_hours',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='prepaid_service_sol', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='prepaid_service_sol', ctx=Load()),
                                            attr='qty_delivered',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='The remaining hours of this SOL should be equal to the ordered quantity minus the delivered quantity.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test task', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_task_rate',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='project_task_rate',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='so',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='remaining_hours_so',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='prepaid_service_sol', ctx=Load()),
                                        attr='remaining_hours',
                                        ctx=Load(),
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
                                        slice=Constant(value='account.analytic.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Timesheet', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_task_rate',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
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
                                        value=Name(id='task', ctx=Load()),
                                        attr='remaining_hours_so',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Before the creation of a timesheet, the remaining hours was 2 hours, when we timesheet 1 hour, the remaining hours should be equal to 1 hour.', kind=None),
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
                                        value=Name(id='prepaid_service_sol', ctx=Load()),
                                        attr='remaining_hours',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='remaining_hours_so',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The remaining hours on the SOL should also be equal to 1 hour.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='task', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sale_line_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='so',
                                                            ctx=Load(),
                                                        ),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='remaining_hours_so',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value="Since the SOL doesn't contain a prepaid service product, the remaining_hours_so should be equal to False.", kind=None),
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
                                        value=Name(id='prepaid_service_sol', ctx=Load()),
                                        attr='remaining_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Since the timesheet on task has the same SOL than the one in the task, the remaining_hours should increase of 1 hour to be equal to 2 hours.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='timesheet', ctx=Store())],
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
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='project_id', kind=None),
                                            Constant(value='task_id', kind=None),
                                            Constant(value='unit_amount', kind=None),
                                            Constant(value='so_line', kind=None),
                                            Constant(value='is_so_line_edited', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Timesheet', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='project_task_rate',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                            Attribute(
                                                value=Name(id='prepaid_service_sol', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    Attribute(
                                        value=Name(id='timesheet', ctx=Load()),
                                        attr='so_line',
                                        ctx=Load(),
                                    ),
                                    Name(id='prepaid_service_sol', ctx=Load()),
                                    Constant(value='The SOL should be the same than one containing the prepaid service product.', kind=None),
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
                                        value=Name(id='prepaid_service_sol', ctx=Load()),
                                        attr='remaining_hours',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='The remaining hours should not change.', kind=None),
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
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
