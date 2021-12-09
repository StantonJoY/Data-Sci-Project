Module(
    body=[
        ImportFrom(
            module='json',
            names=[alias(name='dumps', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='AND', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='get_month', asname=None),
                alias(name='subtract', asname=None),
                alias(name='format_date', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='StockReplenishmentInfo',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.replenishment.info', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock supplier replenishment information', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='orderpoint_id', kind=None),
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
                        args=[Constant(value='stock.warehouse.orderpoint', kind=None)],
                        keywords=[],
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
                                arg='related',
                                value=Constant(value='orderpoint_id.product_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_to_order', ctx=Store())],
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
                                value=Constant(value='orderpoint_id.qty_to_order', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='json_lead_days', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_json_lead_days', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='json_replenishment_history', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_json_replenishment_history', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_json_lead_days',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='json_lead_days',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='replenishment_report', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='replenishment_report', ctx=Load()),
                                                        attr='orderpoint_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='replenishment_report', ctx=Load()),
                                                        attr='orderpoint_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='orderpoint', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='replenishment_report', ctx=Load()),
                                        attr='orderpoint_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='orderpoints_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='orderpoint', ctx=Load()),
                                            attr='_get_lead_days_values',
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
                                                Name(id='dummy', ctx=Store()),
                                                Name(id='lead_days_description', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='orderpoint', ctx=Load()),
                                                attr='rule_ids',
                                                ctx=Load(),
                                            ),
                                            attr='_get_lead_days',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='orderpoint', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='orderpoints_values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='replenishment_report', ctx=Load()),
                                            attr='json_lead_days',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='dumps', ctx=Load()),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='template', kind=None),
                                                    Constant(value='lead_days_date', kind=None),
                                                    Constant(value='lead_days_description', kind=None),
                                                    Constant(value='today', kind=None),
                                                    Constant(value='trigger', kind=None),
                                                    Constant(value='qty_forecast', kind=None),
                                                    Constant(value='qty_to_order', kind=None),
                                                    Constant(value='product_min_qty', kind=None),
                                                    Constant(value='product_max_qty', kind=None),
                                                    Constant(value='product_uom_name', kind=None),
                                                    Constant(value='virtual', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='stock.leadDaysPopOver', kind=None),
                                                    Call(
                                                        func=Name(id='format_date', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='replenishment_report', ctx=Load()),
                                                                    attr='orderpoint_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='lead_days_date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='lead_days_description', ctx=Load()),
                                                    Call(
                                                        func=Name(id='format_date', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
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
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='orderpoint', ctx=Load()),
                                                        attr='trigger',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.qweb.field.float', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='value_to_html',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='orderpoint', ctx=Load()),
                                                                attr='qty_forecast',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='decimal_precision', kind=None)],
                                                                values=[Constant(value='Product Unit of Measure', kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.qweb.field.float', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='value_to_html',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='orderpoint', ctx=Load()),
                                                                attr='qty_to_order',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='decimal_precision', kind=None)],
                                                                values=[Constant(value='Product Unit of Measure', kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.qweb.field.float', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='value_to_html',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='orderpoint', ctx=Load()),
                                                                attr='product_min_qty',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='decimal_precision', kind=None)],
                                                                values=[Constant(value='Product Unit of Measure', kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.qweb.field.float', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='value_to_html',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='orderpoint', ctx=Load()),
                                                                attr='product_max_qty',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='decimal_precision', kind=None)],
                                                                values=[Constant(value='Product Unit of Measure', kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='orderpoint', ctx=Load()),
                                                        attr='product_uom_name',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='orderpoint', ctx=Load()),
                                                                    attr='trigger',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='manual', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='orderpoint', ctx=Load()),
                                                                        attr='create_uid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                            ),
                                                        ],
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
                            args=[Constant(value='orderpoint_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_json_replenishment_history',
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
                            target=Name(id='replenishment_report', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='replenishment_history', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='today', ctx=Store())],
                                    value=Call(
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='first_month', ctx=Store())],
                                    value=Call(
                                        func=Name(id='subtract', ctx=Load()),
                                        args=[Name(id='today', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='month',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='date_from', ctx=Store()),
                                                Name(id='dummy', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='get_month', ctx=Load()),
                                        args=[Name(id='first_month', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='dummy', ctx=Store()),
                                                Name(id='date_to', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='get_month', ctx=Load()),
                                        args=[Name(id='today', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='replenishment_report', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='date_from', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='combine',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='date_to', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='time', ctx=Load()),
                                                                attr='max',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='done', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='replenishment_report', ctx=Load()),
                                                                attr='orderpoint_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company_id',
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quantity_by_month_out', ctx=Store())],
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
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='AND', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='location_dest_id.usage', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='customer', kind=None),
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
                                            List(
                                                elts=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='product_qty', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='date:month', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quantity_by_month_returned', ctx=Store())],
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
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='AND', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='location_id.usage', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='customer', kind=None),
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
                                            List(
                                                elts=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='product_qty', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='date:month', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quantity_by_month_returned', ctx=Store())],
                                    value=DictComp(
                                        key=Subscript(
                                            value=Name(id='g', ctx=Load()),
                                            slice=Constant(value='date:month', kind=None),
                                            ctx=Load(),
                                        ),
                                        value=Subscript(
                                            value=Name(id='g', ctx=Load()),
                                            slice=Constant(value='product_qty', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='g', ctx=Store()),
                                                iter=Name(id='quantity_by_month_returned', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='group', ctx=Store()),
                                    iter=Name(id='quantity_by_month_out', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='month', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='group', ctx=Load()),
                                                slice=Constant(value='date:month', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='replenishment_history', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='uom_name', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='month', ctx=Load()),
                                                            BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='group', ctx=Load()),
                                                                    slice=Constant(value='product_qty', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='quantity_by_month_returned', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Name(id='month', ctx=Load()),
                                                                        Constant(value=0, kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='replenishment_report', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='display_name',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='replenishment_report', ctx=Load()),
                                            attr='json_replenishment_history',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='dumps', ctx=Load()),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='template', kind=None),
                                                    Constant(value='replenishment_history', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='stock.replenishmentHistory', kind=None),
                                                    Name(id='replenishment_history', ctx=Load()),
                                                ],
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
                            args=[Constant(value='orderpoint_id', kind=None)],
                            keywords=[],
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
