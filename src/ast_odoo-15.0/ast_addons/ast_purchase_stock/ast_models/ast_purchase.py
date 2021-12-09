Module(
    body=[
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='float_round', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.purchase.models.purchase',
            names=[alias(name='PurchaseOrder', asname='Purchase')],
            level=0,
        ),
        ClassDef(
            name='PurchaseOrder',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='purchase.order', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_picking_type',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_picking_type',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
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
                                                args=[Constant(value='company_id', kind=None)],
                                                keywords=[],
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
                                        ],
                                    ),
                                ],
                                keywords=[],
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
                Assign(
                    targets=[Name(id='incoterm_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.incoterms', kind=None),
                            Constant(value='Incoterm', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='done', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=True, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='International Commercial Terms are a series of predefined commercial terms used in international transactions.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='incoming_picking_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Incoming Shipment count', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_incoming_picking_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='stock.picking', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_picking_ids', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Receptions', kind=None),
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
                    targets=[Name(id='picking_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Deliver To', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='states',
                                value=Attribute(
                                    value=Name(id='Purchase', ctx=Load()),
                                    attr='READONLY_STATES',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_picking_type', ctx=Load()),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="['|', ('warehouse_id', '=', False), ('warehouse_id.company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This will determine operation type of incoming shipment', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='default_location_dest_id_usage', ctx=Store())],
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
                                value=Constant(value='picking_type_id.default_location_dest_id.usage', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Destination Location Type', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to display the Drop Ship Address', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='procurement.group', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Procurement Group', kind=None),
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
                    targets=[Name(id='is_shipped', ctx=Store())],
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
                                value=Constant(value='_compute_is_shipped', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='effective_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Effective Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_effective_date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Completion date of the first receipt order.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='on_time_rate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.on_time_rate', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_picking_ids',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='picking_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='move_ids',
                                            ctx=Load(),
                                        ),
                                        attr='picking_id',
                                        ctx=Load(),
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
                            args=[Constant(value='order_line.move_ids.picking_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_incoming_picking_count',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='incoming_picking_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='picking_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                            args=[Constant(value='picking_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_effective_date',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pickings', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='picking_ids',
                                                ctx=Load(),
                                            ),
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
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='done', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='location_dest_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='usage',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='internal', kind=None)],
                                                        ),
                                                        Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='date_done',
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
                                            value=Name(id='order', ctx=Load()),
                                            attr='effective_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='pickings', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='date_done', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='default',
                                                value=Constant(value=False, kind=None),
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
                            args=[Constant(value='picking_ids.date_done', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_shipped',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='picking_ids',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
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
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='picking_ids',
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
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='is_shipped',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='is_shipped',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
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
                                Constant(value='picking_ids', kind=None),
                                Constant(value='picking_ids.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_picking_type_id',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='default_location_dest_id',
                                        ctx=Load(),
                                    ),
                                    attr='usage',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='customer', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dest_address_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
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
                            args=[Constant(value='picking_type_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_company_id',
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
                            targets=[Name(id='p_type', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='picking_type_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='p_type', ctx=Load()),
                                        Compare(
                                            left=Attribute(
                                                value=Name(id='p_type', ctx=Load()),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='incoming', kind=None)],
                                        ),
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='p_type', ctx=Load()),
                                                            attr='warehouse_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='p_type', ctx=Load()),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_picking_type',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
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
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='order_line', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='purchase', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='order', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='pre_order_line_qty', ctx=Store())],
                                            value=DictComp(
                                                key=Name(id='order_line', ctx=Load()),
                                                value=Attribute(
                                                    value=Name(id='order_line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order_line', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='order_line', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
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
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='order_line', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='purchase', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='order', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='to_log', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='order_line', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='pre_order_line_qty', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='order_line', ctx=Load()),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='float_compare', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='pre_order_line_qty', ctx=Load()),
                                                                            slice=Name(id='order_line', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='product_qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='precision_rounding',
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='order_line', ctx=Load()),
                                                                                    attr='product_uom',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='rounding',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='to_log', ctx=Load()),
                                                                    slice=Name(id='order_line', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='pre_order_line_qty', ctx=Load()),
                                                                        slice=Name(id='order_line', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
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
                                        If(
                                            test=Name(id='to_log', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='_log_decrease_ordered_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='to_log', ctx=Load())],
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
                    name='button_approve',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='button_approve',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='force',
                                        value=Name(id='force', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_picking',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='button_cancel',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='done', kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Unable to cancel purchase order %s as some receptions have already been done.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='draft', kind=None),
                                                    Constant(value='sent', kind=None),
                                                    Constant(value='to approve', kind=None),
                                                    Constant(value='purchase', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='order_line', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='move_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_action_cancel',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='order_line', ctx=Load()),
                                                        attr='move_dest_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='move_dest_ids', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='move_dest_ids',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='propagate_cancel',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move_dest_ids', ctx=Load()),
                                                                            attr='_action_cancel',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move_dest_ids', ctx=Load()),
                                                                            attr='write',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[Constant(value='procure_method', kind=None)],
                                                                                values=[Constant(value='make_to_stock', kind=None)],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='move_dest_ids', ctx=Load()),
                                                                            attr='_recompute_state',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
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
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='pick', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='picking_ids',
                                                ctx=Load(),
                                            ),
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='cancel', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pick', ctx=Load()),
                                                    attr='action_cancel',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='move_dest_ids', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='button_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_picking',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_action_view_picking',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_ids',
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
                FunctionDef(
                    name='_get_action_view_picking',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This function returns an action that display existing picking orders of given purchase order ids. When only one found, show the picking immediately.\n        ', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.action_picking_tree_all', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_partner_id', kind=None),
                                    Constant(value='default_origin', kind=None),
                                    Constant(value='default_picking_type_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                                            attr='picking_type_id',
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
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='pickings', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='pickings', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='pickings', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='pickings', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
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
                                                args=[
                                                    Constant(value='stock.view_picking_form', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='form_view', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='res', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='res', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='views', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Name(id='form_view', ctx=Load()),
                                                op=Add(),
                                                right=ListComp(
                                                    elt=Tuple(
                                                        elts=[
                                                            Name(id='state', ctx=Load()),
                                                            Name(id='view', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Tuple(
                                                                elts=[
                                                                    Name(id='state', ctx=Store()),
                                                                    Name(id='view', ctx=Store()),
                                                                ],
                                                                ctx=Store(),
                                                            ),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='result', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='views', kind=None),
                                                                    List(elts=[], ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ifs=[
                                                                Compare(
                                                                    left=Name(id='view', ctx=Load()),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value='form', kind=None)],
                                                                ),
                                                            ],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='pickings', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
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
                    name='_prepare_invoice',
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
                            targets=[Name(id='invoice_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_prepare_invoice',
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
                                    value=Name(id='invoice_vals', ctx=Load()),
                                    slice=Constant(value='invoice_incoterm_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='incoterm_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='invoice_vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_log_decrease_ordered_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='purchase_order_lines_quantities', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='_keys_in_sorted',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='move', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' sort by picking and the responsible for the product the\n            move.\n            ', kind=None),
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='picking_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='responsible_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                            name='_keys_in_groupby',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='move', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' group by picking and the responsible for the product the\n            move.\n            ', kind=None),
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='picking_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='responsible_id',
                                                ctx=Load(),
                                            ),
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
                            name='_render_note_exception_quantity_po',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='order_exceptions', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='order_line_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='purchase.order.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Name(id='order_line', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='order_exceptions', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                    comprehension(
                                                        target=Name(id='order_line', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='order', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
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
                                Assign(
                                    targets=[Name(id='purchase_order_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='order_line_ids', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='order_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.move', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='concat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='rendering_context', ctx=Load()),
                                                        attr='keys',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='impacted_pickings', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='move_ids', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='picking_id', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='_get_impacted_pickings',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='move_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='move_ids', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='picking_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='purchase_order_ids', kind=None),
                                            Constant(value='order_exceptions', kind=None),
                                            Constant(value='impacted_pickings', kind=None),
                                        ],
                                        values=[
                                            Name(id='purchase_order_ids', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='order_exceptions', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='impacted_pickings', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
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
                                                args=[Constant(value='purchase_stock.exception_on_po', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Name(id='values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='documents', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_log_activity_get_documents',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='purchase_order_lines_quantities', ctx=Load()),
                                    Constant(value='move_ids', kind=None),
                                    Constant(value='DOWN', kind=None),
                                    Name(id='_keys_in_sorted', ctx=Load()),
                                    Name(id='_keys_in_groupby', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filtered_documents', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='parent', ctx=Store()),
                                            Name(id='responsible', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    Name(id='rendering_context', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='documents', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='parent', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='stock.picking', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='parent', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='cancel', kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='filtered_documents', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Name(id='parent', ctx=Load()),
                                                    Name(id='responsible', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='rendering_context', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_log_activity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='_render_note_exception_quantity_po', ctx=Load()),
                                    Name(id='filtered_documents', ctx=Load()),
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
                    name='_get_destination_location',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='dest_address_id',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dest_address_id',
                                                ctx=Load(),
                                            ),
                                            attr='property_stock_customer',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='default_location_dest_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_picking_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='picking_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking.type', kind=None),
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
                                                    Constant(value='code', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='incoming', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='warehouse_id.company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='company_id', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='picking_type', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='picking_type', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.picking.type', kind=None),
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
                                                            Constant(value='code', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='incoming', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='warehouse_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
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
                            value=Subscript(
                                value=Name(id='picking_type', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=1, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
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
                    name='_prepare_picking',
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
                                    attr='group_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='group_id',
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='property_stock_supplier',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='You must set a Vendor Location for this partner %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='origin', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_order',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_destination_location',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='property_stock_supplier',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                    name='_create_picking',
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
                            targets=[Name(id='StockPicking', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.picking', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='po', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='po', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='purchase', kind=None),
                                                        Constant(value='done', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='product', kind=None),
                                                                Constant(value='consu', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='product', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='order_line',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_id',
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
                                    body=[
                                        Assign(
                                            targets=[Name(id='order', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='pickings', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='picking_ids',
                                                        ctx=Load(),
                                                    ),
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
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotIn()],
                                                            comparators=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='done', kind=None),
                                                                        Constant(value='cancel', kind=None),
                                                                    ],
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
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='pickings', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='_prepare_picking',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='picking', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='StockPicking', ctx=Load()),
                                                                    attr='with_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='res', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='picking', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='pickings', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='moves', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_create_stock_moves',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='picking', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='moves', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='moves', ctx=Load()),
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
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='done', kind=None),
                                                                                Constant(value='cancel', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_action_confirm',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='seq', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='move', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='moves', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='key',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='move', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='date',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='seq', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=5, kind=None),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='sequence',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='seq', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='moves', ctx=Load()),
                                                    attr='_action_assign',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='picking', ctx=Load()),
                                                    attr='message_post_with_view',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.message_origin_link', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='values',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='self', kind=None),
                                                                Constant(value='origin', kind=None),
                                                            ],
                                                            values=[
                                                                Name(id='picking', ctx=Load()),
                                                                Name(id='order', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='subtype_id',
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
                                                                args=[Constant(value='mail.mt_note', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_picking_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='activity', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Helper method to add picking info to the Date Updated activity when\n        vender updates date_planned of the po lines.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='validated_picking', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='done', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='validated_picking', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Those dates couldn’t be modified accordingly on the receipt %s which had already been validated.', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='validated_picking', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Corresponding receipt not found.', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Those dates have been updated accordingly on the receipt %s.', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='picking_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
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
                        AugAssign(
                            target=Attribute(
                                value=Name(id='activity', ctx=Load()),
                                attr='note',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Markup', ctx=Load()),
                                        args=[Constant(value='<p>{}</p>', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_update_date_activity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='updated_dates', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='activity', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_create_update_date_activity',
                                    ctx=Load(),
                                ),
                                args=[Name(id='updated_dates', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_picking_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='activity', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_update_date_activity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='updated_dates', annotation=None, type_comment=None),
                            arg(arg='activity', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='note_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='activity', ctx=Load()),
                                        attr='note',
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<p>', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='note_lines', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='activity', ctx=Load()),
                                    attr='note',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Markup', ctx=Load()),
                                        args=[Constant(value='<p>', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='note_lines', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_update_update_date_activity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='updated_dates', ctx=Load()),
                                    Name(id='activity', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_picking_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='activity', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_orders_to_remind',
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
                            value=Constant(value="When auto sending reminder mails, don't send for purchase order with\n        validated receipts.", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_orders_to_remind',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='effective_date',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PurchaseOrderLine',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='purchase.order.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_received_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='stock_moves', kind=None),
                                                Constant(value='Stock Moves', kind=None),
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
                    targets=[Name(id='move_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='purchase_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Reservation', kind=None),
                            ),
                            keyword(
                                arg='readonly',
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
                    targets=[Name(id='orderpoint_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.warehouse.orderpoint', kind=None),
                            Constant(value='Orderpoint', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
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
                    targets=[Name(id='move_dest_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='created_purchase_line_id', kind=None),
                            Constant(value='Downstream Moves', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_description_variants', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Custom Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='propagate_cancel', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Propagate cancellation', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='forecasted_issue', ctx=Store())],
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
                                value=Constant(value='_compute_forecasted_issue', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_received_method',
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
                                            Name(id='PurchaseOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_received_method',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
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
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_received_method',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='stock_moves', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_po_line_moves',
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
                            targets=[Name(id='moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
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
                                Assign(
                                    targets=[Name(id='moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='moves', ctx=Load()),
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
                                                body=Compare(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                            value=Name(id='moves', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_received',
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
                            targets=[Name(id='from_stock_lines', ctx=Store())],
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
                                            args=[arg(arg='order_line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='order_line', ctx=Load()),
                                                attr='qty_received_method',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='stock_moves', kind=None)],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrderLine', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='from_stock_lines', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_received',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='qty_received_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='stock_moves', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='total', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='move', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_get_po_line_moves',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='done', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='location_dest_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='usage',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='supplier', kind=None)],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='to_refund',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='total', ctx=Store()),
                                                                            op=Sub(),
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='move', ctx=Load()),
                                                                                        attr='product_uom',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_compute_quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='move', ctx=Load()),
                                                                                        attr='product_uom_qty',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
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
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='move', ctx=Load()),
                                                                                attr='origin_returned_move_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='move', ctx=Load()),
                                                                                        attr='origin_returned_move_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_is_dropshipped',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='move', ctx=Load()),
                                                                                        attr='_is_dropshipped_returned',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[Pass()],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                attr='location_dest_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='usage',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='internal', kind=None)],
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='move', ctx=Load()),
                                                                                        attr='to_refund',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='move', ctx=Load()),
                                                                                            attr='location_dest_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[NotIn()],
                                                                                        comparators=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='stock.location', kind=None),
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
                                                                                                                    Constant(value='id', kind=None),
                                                                                                                    Constant(value='child_of', kind=None),
                                                                                                                    Attribute(
                                                                                                                        value=Attribute(
                                                                                                                            value=Attribute(
                                                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                                                attr='warehouse_id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            attr='view_location_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
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
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Name(id='total', ctx=Store()),
                                                                                    op=Sub(),
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                attr='product_uom',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='_compute_quantity',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                attr='product_uom_qty',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='line', ctx=Load()),
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
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                AugAssign(
                                                                                    target=Name(id='total', ctx=Store()),
                                                                                    op=Add(),
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                attr='product_uom',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='_compute_quantity',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='move', ctx=Load()),
                                                                                                attr='product_uom_qty',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='line', ctx=Load()),
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
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_track_qty_received',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='total', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='qty_received',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='total', ctx=Load()),
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
                                Constant(value='move_ids.state', kind=None),
                                Constant(value='move_ids.product_uom_qty', kind=None),
                                Constant(value='move_ids.product_uom', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_forecasted_issue',
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
                                    targets=[Name(id='warehouse', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='warehouse_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='forecasted_issue',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='virtual_available', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='warehouse',
                                                            value=Attribute(
                                                                value=Name(id='warehouse', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='to_date',
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='date_planned',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='virtual_available',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='draft', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='virtual_available', ctx=Store()),
                                                    op=Add(),
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_uom_qty',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='virtual_available', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='forecasted_issue',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
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
                                Constant(value='date_planned', kind=None),
                            ],
                            keywords=[],
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
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='purchase', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_create_or_update_picking',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date_planned', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='date_planned', kind=None),
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
                                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='display_type',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_update_move_date_deadline',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new_date', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
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
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='l', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='purchase', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_product_qty', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='line', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='line', ctx=Load()),
                                    attr='product_uom_qty',
                                    ctx=Load(),
                                ),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PurchaseOrderLine', ctx=Load()),
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
                        If(
                            test=Compare(
                                left=Constant(value='product_qty', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lines', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='previous_product_qty',
                                                        value=Name(id='previous_product_qty', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            attr='_create_or_update_picking',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                    name='action_product_forecast_report',
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='action_product_forecast_report',
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
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='active_id', kind=None),
                                    Constant(value='active_model', kind=None),
                                    Constant(value='move_to_match_ids', kind=None),
                                    Constant(value='purchase_line_to_match_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='product.product', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='m', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='warehouse', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='order_id',
                                        ctx=Load(),
                                    ),
                                    attr='picking_type_id',
                                    ctx=Load(),
                                ),
                                attr='warehouse_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='warehouse', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='warehouse', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='warehouse', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_action_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ppg_cancel_lines', ctx=Store())],
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
                                        body=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='propagate_cancel',
                                            ctx=Load(),
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
                                    value=Attribute(
                                        value=Name(id='ppg_cancel_lines', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_action_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='not_ppg_cancel_lines', ctx=Store())],
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='propagate_cancel',
                                                ctx=Load(),
                                            ),
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
                                    value=Attribute(
                                        value=Name(id='not_ppg_cancel_lines', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='procure_method', kind=None)],
                                        values=[Constant(value='make_to_stock', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='not_ppg_cancel_lines', ctx=Load()),
                                        attr='move_dest_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_recompute_state',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_move_date_deadline',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Updates corresponding move picking line deadline dates that are not yet completed. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='moves_to_update', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotIn()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='done', kind=None),
                                                        Constant(value='cancel', kind=None),
                                                    ],
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='moves_to_update', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='moves_to_update', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='move_dest_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='done', kind=None),
                                                                Constant(value='cancel', kind=None),
                                                            ],
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
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='moves_to_update', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='date_deadline',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Name(id='new_date', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='po_lead',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
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
                    name='_create_or_update_picking',
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
                                                            Constant(value='product', kind=None),
                                                            Constant(value='consu', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_received',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='You cannot decrease the ordered quantity below the received quantity.\nCreate a return first.', kind=None)],
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
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='qty_invoiced',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='invoice_lines',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='activity_schedule',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.mail_activity_data_warning', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='note',
                                                                value=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The quantities on your purchase order indicate less than billed. You should ask for a refund.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='pickings', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='picking_ids',
                                                        ctx=Load(),
                                                    ),
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
                                                        body=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='x', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='done', kind=None),
                                                                                Constant(value='cancel', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='location_dest_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='usage',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[In()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='internal', kind=None),
                                                                                Constant(value='transit', kind=None),
                                                                                Constant(value='customer', kind=None),
                                                                            ],
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
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='picking', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='pickings', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='pickings', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='picking', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_prepare_picking',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='picking', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.picking', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='res', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='moves', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='_create_stock_moves',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='picking', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='moves', ctx=Load()),
                                                            attr='_action_confirm',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_action_assign',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_stock_move_price_unit',
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
                            targets=[Name(id='order', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='order_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='price_unit', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='price_unit',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='price_unit_prec', ctx=Store())],
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
                                args=[Constant(value='Product Price', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='taxes_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='qty', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_qty',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='price_unit', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='taxes_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='round',
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='compute_all',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='price_unit', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='currency',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='quantity',
                                                    value=Name(id='qty', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='product',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
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
                                            ],
                                        ),
                                        slice=Constant(value='total_void', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='price_unit', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='price_unit', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='qty', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='price_unit_prec', ctx=Load()),
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
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
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='price_unit', ctx=Store()),
                                    op=Mult(),
                                    value=BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='factor',
                                            ctx=Load(),
                                        ),
                                        op=Div(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='factor',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='currency_id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='price_unit', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='price_unit', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                                        keywords=[
                                            keyword(
                                                arg='round',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='price_unit', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_stock_moves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='picking', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Prepare the stock moves data for one order line. This function returns a list of\n        dictionary ready to be used in stock.move's create()\n        ", kind=None),
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
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='product', kind=None),
                                            Constant(value='consu', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='price_unit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_stock_move_price_unit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='qty', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_qty_procurement',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_dests', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='move_dest_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='move_dests', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_dests', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='move_dest_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
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
                                                                value=Name(id='m', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value='cancel', kind=None)],
                                                        ),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='location_dest_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='usage',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='supplier', kind=None)],
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='move_dests', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='qty_to_attach', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty_to_push', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='qty', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='move_dests_initial_demand', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='move_dests', ctx=Load()),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='m', annotation=None, type_comment=None)],
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
                                                                                        value=Name(id='m', ctx=Load()),
                                                                                        attr='state',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[NotEq()],
                                                                                    comparators=[Constant(value='cancel', kind=None)],
                                                                                ),
                                                                                UnaryOp(
                                                                                    op=Not(),
                                                                                    operand=Compare(
                                                                                        left=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='m', ctx=Load()),
                                                                                                attr='location_dest_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='usage',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='supplier', kind=None)],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='product_qty', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='qty_to_attach', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='move_dests_initial_demand', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='qty', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty_to_push', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='move_dests_initial_demand', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='float_compare', ctx=Load()),
                                    args=[
                                        Name(id='qty_to_attach', ctx=Load()),
                                        Constant(value=0.0, kind=None),
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
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='product_uom_qty', ctx=Store()),
                                                Name(id='product_uom', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='_adjust_uom_quantities',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='qty_to_attach', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
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
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_stock_move_vals',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='picking', ctx=Load()),
                                                    Name(id='price_unit', ctx=Load()),
                                                    Name(id='product_uom_qty', ctx=Load()),
                                                    Name(id='product_uom', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='float_is_zero', ctx=Load()),
                                    args=[Name(id='qty_to_push', ctx=Load())],
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
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='product_uom_qty', ctx=Store()),
                                                Name(id='product_uom', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='_adjust_uom_quantities',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='qty_to_push', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='extra_move_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_stock_move_vals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='picking', ctx=Load()),
                                            Name(id='price_unit', ctx=Load()),
                                            Name(id='product_uom_qty', ctx=Load()),
                                            Name(id='product_uom', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='extra_move_vals', ctx=Load()),
                                            slice=Constant(value='move_dest_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='extra_move_vals', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='_get_qty_procurement',
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
                            targets=[Name(id='qty', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='outgoing_moves', ctx=Store()),
                                        Name(id='incoming_moves', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_outgoing_incoming_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='outgoing_moves', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='qty', ctx=Store()),
                                    op=Sub(),
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Name(id='incoming_moves', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='qty', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='qty', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_orderpoint_picking_type',
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
                            targets=[Name(id='warehouse_loc', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='picking_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='warehouse_id',
                                    ctx=Load(),
                                ),
                                attr='view_location_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dest_loc', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='move_dest_ids',
                                            ctx=Load(),
                                        ),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='orderpoint_id',
                                            ctx=Load(),
                                        ),
                                        attr='location_id',
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
                                    Name(id='warehouse_loc', ctx=Load()),
                                    Name(id='dest_loc', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Attribute(
                                                value=Name(id='warehouse_loc', ctx=Load()),
                                                attr='parent_path',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Subscript(
                                                        value=Name(id='dest_loc', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='parent_path',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
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
                                                args=[
                                                    Constant(value='For the product %s, the warehouse of the operation type (%s) is inconsistent with the location (%s) of the reordering rule (%s). Change the operation type or cancel the request for quotation.', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='orderpoint_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='orderpoint_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_stock_move_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='picking', annotation=None, type_comment=None),
                            arg(arg='price_unit', annotation=None, type_comment=None),
                            arg(arg='product_uom_qty', annotation=None, type_comment=None),
                            arg(arg='product_uom', annotation=None, type_comment=None),
                        ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_orderpoint_picking_type',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='order_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dest_address_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_planned', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_planned',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='date_planned',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='date_deadline', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='picking_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='move_dest_ids', kind=None),
                                    Constant(value='state', kind=None),
                                    Constant(value='purchase_line_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='price_unit', kind=None),
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='group_id', kind=None),
                                    Constant(value='origin', kind=None),
                                    Constant(value='description_picking', kind=None),
                                    Constant(value='propagate_cancel', kind=None),
                                    Constant(value='warehouse_id', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='product_packaging_id', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2000, kind=None),
                                            step=None,
                                        ),
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
                                    Name(id='date_planned', ctx=Load()),
                                    BinOp(
                                        left=Name(id='date_planned', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='order_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='po_lead',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    Attribute(
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
                                            attr='property_stock_supplier',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='orderpoint_id',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='move_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='move_dest_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='orderpoint_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='order_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_destination_location',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='picking', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='dest_address_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Constant(value=4, kind=None),
                                                Name(id='x', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='move_dest_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value='draft', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='price_unit', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='order_id',
                                                ctx=Load(),
                                            ),
                                            attr='group_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='order_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='description_pickingin',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='propagate_cancel',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='order_id',
                                                    ctx=Load(),
                                                ),
                                                attr='picking_type_id',
                                                ctx=Load(),
                                            ),
                                            attr='warehouse_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='product_uom_qty', ctx=Load()),
                                    Attribute(
                                        value=Name(id='product_uom', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_packaging_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
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
                    name='_prepare_purchase_order_line_from_procurement',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='product_qty', annotation=None, type_comment=None),
                            arg(arg='product_uom', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='po', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='line_description', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_description_variants', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line_description', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='product_description_variants', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='supplier', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='supplier', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_purchase_order_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='product_qty', ctx=Load()),
                                    Name(id='product_uom', ctx=Load()),
                                    Name(id='company_id', ctx=Load()),
                                    Name(id='supplier', ctx=Load()),
                                    Name(id='po', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='line_description', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='product_id', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='line_description', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='\n', kind=None),
                                        op=Add(),
                                        right=Name(id='line_description', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='move_dest_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Constant(value=4, kind=None),
                                        Attribute(
                                            value=Name(id='x', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='move_dest_ids', kind=None),
                                                List(elts=[], ctx=Load()),
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
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='orderpoint_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='orderpoint_id', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='orderpoint_id', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='propagate_cancel', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='propagate_cancel', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='product_description_variants', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_description_variants', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
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
                    name='_create_stock_moves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='picking', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='val', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_prepare_stock_moves',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='picking', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='val', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='move_dest_ids',
                                                ctx=Load(),
                                            ),
                                            attr='created_purchase_line_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_candidate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='product_qty', annotation=None, type_comment=None),
                            arg(arg='product_uom', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='origin', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Return the record in self where the procument with values passed as\n        args can be merged. If it returns an empty record then a new line will\n        be created.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='description_picking', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_description_variants', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='description_picking', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='product_description_variants', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
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
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='propagate_cancel',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='propagate_cancel', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        BoolOp(
                                                            op=And(),
                                                            values=[
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Constant(value='orderpoint_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Subscript(
                                                                                value=Name(id='values', ctx=Load()),
                                                                                slice=Constant(value='move_dest_ids', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='l', ctx=Load()),
                                                                        attr='orderpoint_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Constant(value='orderpoint_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        Constant(value=True, kind=None),
                                                    ],
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='lines', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='product_description_variants', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='order_id.partner_id', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=1, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product_lang', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product_id', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='product_lang', ctx=Load()),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='product_lang', ctx=Load()),
                                        attr='description_purchase',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='name', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='\n', kind=None),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='product_lang', ctx=Load()),
                                                    attr='description_purchase',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        BinOp(
                                                            left=BinOp(
                                                                left=Name(id='name', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='\n', kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Name(id='description_picking', ctx=Load()),
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
                                    test=Name(id='lines', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='lines', ctx=Load()),
                                            Subscript(
                                                value=Name(id='lines', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order.line', kind=None),
                                        ctx=Load(),
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
                    name='_get_outgoing_incoming_moves',
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
                            targets=[Name(id='outgoing_moves', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='incoming_moves', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_ids',
                                        ctx=Load(),
                                    ),
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
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='cancel', kind=None)],
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='scrapped',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='product_id',
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
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='usage',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='supplier', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='to_refund',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='outgoing_moves', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='move', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='usage',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='supplier', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='move', ctx=Load()),
                                                                    attr='origin_returned_move_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='origin_returned_move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='to_refund',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='incoming_moves', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='move', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='outgoing_moves', ctx=Load()),
                                    Name(id='incoming_moves', ctx=Load()),
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
                    name='_update_date_planned',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='updated_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='move_to_update', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='m', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotIn()],
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
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                            attr='move_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='move_to_update', ctx=Load()),
                                ],
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
                                            attr='_update_date_planned',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='updated_date', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='move_to_update', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_move_date_deadline',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='updated_date', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_qty_received_method',
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
                            value=Constant(value='Update qty_received_method for old PO before install this module.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_received_method',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
