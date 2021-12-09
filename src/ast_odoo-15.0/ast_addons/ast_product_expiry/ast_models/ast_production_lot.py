Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
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
        ClassDef(
            name='StockProductionLot',
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
                    value=Constant(value='stock.production.lot', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_expiration_date', ctx=Store())],
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
                                value=Constant(value='Use Expiration Date', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.use_expiration_date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expiration_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Expiration Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Best before Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This is the date on which the goods with this Serial Number start deteriorating, without being dangerous yet.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='removal_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Removal Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This is the date on which the goods with this Serial Number should be removed from the stock. This date will be used in FEFO removal strategy.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alert_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Alert Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date to determine the expired lots and serial numbers using the filter "Expiration Alerts".', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_expiry_alert', ctx=Store())],
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
                                value=Constant(value='_compute_product_expiry_alert', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The Expiration Date has been reached.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_expiry_reminded', ctx=Store())],
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
                                value=Constant(value='Expiry has been reminded', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_product_expiry_alert',
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
                            targets=[Name(id='current_date', ctx=Store())],
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
                        For(
                            target=Name(id='lot', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='lot', ctx=Load()),
                                        attr='expiration_date',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='lot', ctx=Load()),
                                                    attr='product_expiry_alert',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Compare(
                                                left=Attribute(
                                                    value=Name(id='lot', ctx=Load()),
                                                    attr='expiration_date',
                                                    ctx=Load(),
                                                ),
                                                ops=[LtE()],
                                                comparators=[Name(id='current_date', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='lot', ctx=Load()),
                                                    attr='product_expiry_alert',
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
                            args=[Constant(value='expiration_date', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_dates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Returns dates based on number of days configured in current lot's product.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mapped_fields', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='expiration_date', kind=None),
                                    Constant(value='use_date', kind=None),
                                    Constant(value='removal_date', kind=None),
                                    Constant(value='alert_date', kind=None),
                                ],
                                values=[
                                    Constant(value='expiration_time', kind=None),
                                    Constant(value='use_time', kind=None),
                                    Constant(value='removal_time', kind=None),
                                    Constant(value='alert_time', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mapped_fields', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='product', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='mapped_fields', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='duration', ctx=Store())],
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='product', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='mapped_fields', ctx=Load()),
                                                        slice=Name(id='field', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='duration', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='datetime',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='now',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='datetime', ctx=Load()),
                                                                attr='timedelta',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Name(id='duration', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
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
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='date', ctx=Load())],
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
                    decorator_list=[],
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
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='dates', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_dates',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='product_id', kind=None)],
                                                        keywords=[],
                                                    ),
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
                                                        args=[Constant(value='default_product_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='d', ctx=Store()),
                                    iter=Name(id='dates', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='d', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Name(id='d', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='dates', ctx=Load()),
                                                        slice=Name(id='d', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
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
                    name='_onchange_expiration_date',
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
                                            attr='_origin',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='expiration_date',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                    attr='expiration_date',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='time_delta', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='expiration_date',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_origin',
                                        ctx=Load(),
                                    ),
                                    attr='expiration_date',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_origin',
                                        ctx=Load(),
                                    ),
                                    attr='_get_date_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='time_delta', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='expiration_date',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='expiration_date', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_product',
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
                            targets=[Name(id='dates_dict', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_dates',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='field', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='dates_dict', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='setattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='field', ctx=Load()),
                                            Name(id='value', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_alert_date_exceeded',
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
                            value=Constant(value='Log an activity on internally stored lots whose alert_date has been reached.\n\n        No further activity will be generated on lots whose alert_date\n        has already been reached (even if the alert_date is changed).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='alert_lots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.production.lot', kind=None),
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
                                                    Constant(value='alert_date', kind=None),
                                                    Constant(value='<=', kind=None),
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
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_expiry_reminded', kind=None),
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
                        Assign(
                            targets=[Name(id='lot_stock_quants', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.quant', kind=None),
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
                                                    Constant(value='lot_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='alert_lots', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='location_id.usage', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='internal', kind=None),
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
                            targets=[Name(id='alert_lots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lot_stock_quants', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lot_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='lot', ctx=Store()),
                            iter=Name(id='alert_lots', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lot', ctx=Load()),
                                            attr='activity_schedule',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='product_expiry.mail_activity_type_alert_date_reached', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='user_id',
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='lot', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='responsible_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='SUPERUSER_ID', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='note',
                                                value=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The alert date has been reached for this lot/serial number', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='alert_lots', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='product_expiry_reminded', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                FunctionDef(
                    name='_update_date_values',
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
                        If(
                            test=Name(id='new_date', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='time_delta', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='new_date', ctx=Load()),
                                        op=Sub(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='expiration_date',
                                                    ctx=Load(),
                                                ),
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
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_date_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='time_delta', ctx=Load()),
                                            Name(id='new_date', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='expiration_date', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='new_date', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
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
                    name='_get_date_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='time_delta', annotation=None, type_comment=None),
                            arg(arg='new_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a dict with different date values updated depending of the\n        time_delta. Used in the onchange of `expiration_date` and when user\n        defines a date at the receipt. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='use_date', kind=None),
                                    Constant(value='removal_date', kind=None),
                                    Constant(value='alert_date', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='use_date',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='use_date',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='time_delta', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Name(id='new_date', ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='removal_date',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='removal_date',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='time_delta', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Name(id='new_date', ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='alert_date',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='alert_date',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='time_delta', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Name(id='new_date', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ProcurementGroup',
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
                    value=Constant(value='procurement.group', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_scheduler_tasks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='use_new_cursor', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProcurementGroup', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_run_scheduler_tasks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='use_new_cursor',
                                        value=Name(id='use_new_cursor', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Name(id='company_id', ctx=Load()),
                                    ),
                                ],
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
                                        slice=Constant(value='stock.production.lot', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_alert_date_exceeded',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='use_new_cursor', ctx=Load()),
                            body=[
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
                                            attr='commit',
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
