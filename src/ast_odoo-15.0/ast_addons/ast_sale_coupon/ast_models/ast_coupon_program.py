Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='babel.dates',
            names=[alias(name='format_datetime', asname=None)],
            level=0,
        ),
        ClassDef(
            name='CouponProgram',
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
                    value=Constant(value='coupon.program', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='order_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_order_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_order_count',
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
                            target=Name(id='program', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='program', ctx=Load()),
                                            attr='order_count',
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
                                                slice=Constant(value='sale.order.line', kind=None),
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
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='program', ctx=Load()),
                                                                    attr='discount_line_product_id',
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
                    name='action_view_sales_orders',
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
                            targets=[Name(id='orders', ctx=Store())],
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
                                                slice=Constant(value='sale.order.line', kind=None),
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
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='discount_line_product_id',
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
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='order_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='search_view_id', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Sales Orders', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree,form', kind=None),
                                    Constant(value='sale.order', kind=None),
                                    List(
                                        elts=[
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
                                                    args=[Constant(value='sale.sale_order_view_search_inherit_quotation', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='orders', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='create',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
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
                    name='_check_promo_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='coupon_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='maximum_use_number',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='total_order_count',
                                            ctx=Load(),
                                        ),
                                        ops=[GtE()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='maximum_use_number',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Promo code %s has been expired.', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Name(id='coupon_code', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_filter_on_mimimum_amount',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='order', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='A minimum of %(amount)s %(currency)s should be purchased to get the reward', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='amount',
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='rule_minimum_amount',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='currency',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='currency_id',
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
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='promo_code',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='promo_code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='promo_code',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Dict(
                                                        keys=[Constant(value='error', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The promo code is already applied on this order', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='self', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='order', ctx=Load()),
                                                                attr='no_code_promo_program_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='message', ctx=Store())],
                                                            value=Dict(
                                                                keys=[Constant(value='error', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The promotional offer is already applied on this order', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
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
                                                                    attr='active',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=Dict(
                                                                        keys=[Constant(value='error', kind=None)],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='Promo code is invalid', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='rule_date_from',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='rule_date_from',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Gt()],
                                                                                comparators=[
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
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='tzinfo', ctx=Store())],
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
                                                                                        args=[Constant(value='tz', kind=None)],
                                                                                        keywords=[],
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
                                                                                        attr='tz',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value='UTC', kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='locale', ctx=Store())],
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
                                                                                        args=[Constant(value='lang', kind=None)],
                                                                                        keywords=[],
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
                                                                                    Constant(value='en_US', kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='message', ctx=Store())],
                                                                            value=Dict(
                                                                                keys=[Constant(value='error', kind=None)],
                                                                                values=[
                                                                                    BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value='This coupon is not yet usable. It will be starting from %s', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Mod(),
                                                                                        right=Call(
                                                                                            func=Name(id='format_datetime', ctx=Load()),
                                                                                            args=[
                                                                                                Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='rule_date_from',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[
                                                                                                keyword(
                                                                                                    arg='format',
                                                                                                    value=Constant(value='short', kind=None),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='tzinfo',
                                                                                                    value=Name(id='tzinfo', ctx=Load()),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='locale',
                                                                                                    value=Name(id='locale', ctx=Load()),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='rule_date_to',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Call(
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
                                                                                        ops=[Gt()],
                                                                                        comparators=[
                                                                                            Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='rule_date_to',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='message', ctx=Store())],
                                                                                    value=Dict(
                                                                                        keys=[Constant(value='error', kind=None)],
                                                                                        values=[
                                                                                            Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[Constant(value='Promo code is expired', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Name(id='order', ctx=Load()),
                                                                                                attr='promo_code',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='promo_code_usage',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='code_needed', kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='message', ctx=Store())],
                                                                                            value=Dict(
                                                                                                keys=[Constant(value='error', kind=None)],
                                                                                                values=[
                                                                                                    Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='Promotionals codes are not cumulative.', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='_is_global_discount_program',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='order', ctx=Load()),
                                                                                                            attr='_is_global_discount_already_applied',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='message', ctx=Store())],
                                                                                                    value=Dict(
                                                                                                        keys=[Constant(value='error', kind=None)],
                                                                                                        values=[
                                                                                                            Call(
                                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                                args=[Constant(value='Global discounts are not cumulative.', kind=None)],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
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
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='promo_applicability',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='on_current_order', kind=None)],
                                                                                                            ),
                                                                                                            Compare(
                                                                                                                left=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='reward_type',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='product', kind=None)],
                                                                                                            ),
                                                                                                            UnaryOp(
                                                                                                                op=Not(),
                                                                                                                operand=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(id='order', ctx=Load()),
                                                                                                                        attr='_is_reward_in_order_lines',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[Name(id='self', ctx=Load())],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Assign(
                                                                                                            targets=[Name(id='message', ctx=Store())],
                                                                                                            value=Dict(
                                                                                                                keys=[Constant(value='error', kind=None)],
                                                                                                                values=[
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='The reward products should be in the sales order lines to apply the discount.', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        If(
                                                                                                            test=UnaryOp(
                                                                                                                op=Not(),
                                                                                                                operand=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                        attr='_is_valid_partner',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[
                                                                                                                        Attribute(
                                                                                                                            value=Name(id='order', ctx=Load()),
                                                                                                                            attr='partner_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[Name(id='message', ctx=Store())],
                                                                                                                    value=Dict(
                                                                                                                        keys=[Constant(value='error', kind=None)],
                                                                                                                        values=[
                                                                                                                            Call(
                                                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                                                args=[Constant(value="The customer doesn't have access to this reward.", kind=None)],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                If(
                                                                                                                    test=UnaryOp(
                                                                                                                        op=Not(),
                                                                                                                        operand=Call(
                                                                                                                            func=Attribute(
                                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                                attr='_filter_programs_on_products',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            args=[Name(id='order', ctx=Load())],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Assign(
                                                                                                                            targets=[Name(id='message', ctx=Store())],
                                                                                                                            value=Dict(
                                                                                                                                keys=[Constant(value='error', kind=None)],
                                                                                                                                values=[
                                                                                                                                    Call(
                                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                                        args=[Constant(value="You don't have the required product quantities on your sales order. If the reward is same product quantity, please make sure that all the products are recorded on the sales order (Example: You need to have 3 T-shirts on your sales order if the promotion is 'Buy 2, Get 1 Free'.", kind=None)],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                ],
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
                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                            attr='promo_applicability',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        ops=[Eq()],
                                                                                                                                        comparators=[Constant(value='on_current_order', kind=None)],
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
                                                                                                                                                    attr='context',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                attr='get',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            args=[Constant(value='applicable_coupon', kind=None)],
                                                                                                                                            keywords=[],
                                                                                                                                        ),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            body=[
                                                                                                                                Assign(
                                                                                                                                    targets=[Name(id='applicable_programs', ctx=Store())],
                                                                                                                                    value=Call(
                                                                                                                                        func=Attribute(
                                                                                                                                            value=Name(id='order', ctx=Load()),
                                                                                                                                            attr='_get_applicable_programs',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        args=[],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                    type_comment=None,
                                                                                                                                ),
                                                                                                                                If(
                                                                                                                                    test=Compare(
                                                                                                                                        left=Name(id='self', ctx=Load()),
                                                                                                                                        ops=[NotIn()],
                                                                                                                                        comparators=[Name(id='applicable_programs', ctx=Load())],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Assign(
                                                                                                                                            targets=[Name(id='message', ctx=Store())],
                                                                                                                                            value=Dict(
                                                                                                                                                keys=[Constant(value='error', kind=None)],
                                                                                                                                                values=[
                                                                                                                                                    Call(
                                                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                                                        args=[Constant(value='At least one of the required conditions is not met to get the reward!', kind=None)],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                            type_comment=None,
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
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='message', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_on_mimimum_amount',
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
                        Assign(
                            targets=[Name(id='no_effect_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='_get_no_effect_on_threshold_lines',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='order_amount', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='amount_untaxed', kind=None),
                                    Constant(value='amount_tax', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='amount_untaxed',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='price_subtotal',
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='line', ctx=Store()),
                                                            iter=Name(id='no_effect_lines', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='amount_tax',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='price_tax',
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='line', ctx=Store()),
                                                            iter=Name(id='no_effect_lines', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='program_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='program', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='program', ctx=Load()),
                                            attr='reward_type',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='discount', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lines', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sale.order.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='lines', ctx=Store())],
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
                                                            op=Or(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='program', ctx=Load()),
                                                                            attr='discount_line_product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='program', ctx=Load()),
                                                                                attr='reward_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='discount_line_product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='program', ctx=Load()),
                                                                                attr='program_type',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='promotion_program', kind=None)],
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='is_reward_line',
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
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='untaxed_amount', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='order_amount', ctx=Load()),
                                            slice=Constant(value='amount_untaxed', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='price_subtotal',
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
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tax_amount', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='order_amount', ctx=Load()),
                                            slice=Constant(value='amount_tax', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='price_tax',
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
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='program_amount', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='program', ctx=Load()),
                                            attr='_compute_program_amount',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='rule_minimum_amount', kind=None),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
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
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='program', ctx=Load()),
                                                            attr='rule_minimum_amount_tax_inclusion',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='tax_included', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='program_amount', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[
                                                            BinOp(
                                                                left=Name(id='untaxed_amount', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='tax_amount', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='program_amount', ctx=Load()),
                                                ops=[LtE()],
                                                comparators=[Name(id='untaxed_amount', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='program_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='id',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='program_ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_on_validity_dates',
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
                                            args=[arg(arg='program', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='program', ctx=Load()),
                                                                attr='rule_date_from',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='program', ctx=Load()),
                                                                attr='rule_date_from',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[LtE()],
                                                            comparators=[
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
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='program', ctx=Load()),
                                                                attr='rule_date_to',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='program', ctx=Load()),
                                                                attr='rule_date_to',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[GtE()],
                                                            comparators=[
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
                    name='_filter_promo_programs_with_code',
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
                            value=Constant(value='Filter Promo program with code with a different promo_code if a promo_code is already ordered', kind=None),
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
                                            args=[arg(arg='program', annotation=None, type_comment=None)],
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
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='promo_code_usage',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='code_needed', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='promo_code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='promo_code',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_unexpired_programs',
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
                                            args=[arg(arg='program', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='maximum_use_number',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='total_order_count',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[LtE()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='program', ctx=Load()),
                                                            attr='maximum_use_number',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_programs_on_partners',
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
                                            args=[arg(arg='program', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='program', ctx=Load()),
                                                attr='_is_valid_partner',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
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
                    name='_filter_programs_on_products',
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
                            value=Constant(value='\n        To get valid programs according to product list.\n        i.e Buy 1 imac + get 1 ipad mini free then check 1 imac is on cart or not\n        or  Buy 1 coke + get 1 coke free then check 2 cokes are on cart or not\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='order_lines', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='order', ctx=Load()),
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
                                                args=[arg(arg='line', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='_get_reward_lines',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='order_lines', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products_qties', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='products', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='order_lines', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='products_qties', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='product_uom_qty',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='valid_program_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='program', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='program', ctx=Load()),
                                            attr='rule_products_domain',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='valid_program_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='valid_products', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='program', ctx=Load()),
                                            attr='_get_valid_products',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='products', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='valid_products', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='ordered_rule_products_qty', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='products_qties', ctx=Load()),
                                                    slice=Name(id='product', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='product', ctx=Store()),
                                                        iter=Name(id='valid_products', ctx=Load()),
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
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='program', ctx=Load()),
                                                    attr='promo_applicability',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='on_current_order', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='program', ctx=Load()),
                                                    attr='reward_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='product', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='program', ctx=Load()),
                                                    attr='_get_valid_products',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='reward_product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='ordered_rule_products_qty', ctx=Store()),
                                            op=Sub(),
                                            value=Attribute(
                                                value=Name(id='program', ctx=Load()),
                                                attr='reward_product_quantity',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ordered_rule_products_qty', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='program', ctx=Load()),
                                                attr='rule_min_quantity',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='valid_program_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='program', ctx=Load()),
                                                        attr='id',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='valid_program_ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_not_ordered_reward_programs',
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
                            value=Constant(value='\n        Returns the programs when the reward is actually in the order lines\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='coupon.program', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='program', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='program', ctx=Load()),
                                                    attr='reward_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='product', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
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
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='program', ctx=Load()),
                                                                        attr='reward_product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='program', ctx=Load()),
                                                            attr='reward_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='discount', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='program', ctx=Load()),
                                                            attr='discount_apply_on',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='specific_products', kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='order', ctx=Load()),
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
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='program', ctx=Load()),
                                                                                attr='discount_specific_product_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='programs', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='program', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='programs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_programs_from_common_rules',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='next_order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the programs if every conditions is met\n            :param bool next_order: is the reward given from a previous order\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='next_order', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='programs', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='programs', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='programs', ctx=Load()),
                                                    attr='_filter_on_mimimum_amount',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='order', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
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
                                    args=[Constant(value='no_outdated_coupons', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='programs', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='programs', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='programs', ctx=Load()),
                                                    attr='_filter_on_validity_dates',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='order', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='programs', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='programs', ctx=Load()),
                                            attr='_filter_unexpired_programs',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='order', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='programs', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='programs', ctx=Load()),
                                            attr='_filter_programs_on_partners',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='order', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='next_order', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='programs', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='programs', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='programs', ctx=Load()),
                                                    attr='_filter_programs_on_products',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='order', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='programs_curr_order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='programs', ctx=Load()),
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
                                                attr='promo_applicability',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='on_current_order', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='programs', ctx=Load()),
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
                                                attr='promo_applicability',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='on_next_order', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='programs_curr_order', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='programs', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='programs_curr_order', ctx=Load()),
                                            attr='_filter_not_ordered_reward_programs',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='order', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='programs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_discount_product_values',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_discount_product_values',
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
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='invoice_policy', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='order', kind=None),
                            type_comment=None,
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
                    name='_is_global_discount_program',
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
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='promo_applicability',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='on_current_order', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='reward_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='discount', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='discount_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='percentage', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='discount_apply_on',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='on_order', kind=None)],
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
                    name='_keep_only_most_interesting_auto_applied_global_discount_program',
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
                            value=Constant(value='Given a record set of programs, remove the less interesting auto\n        applied global discount to keep only the most interesting one.\n        We should not take promo code programs into account as a 10% auto\n        applied is considered better than a 50% promo code, as the user might\n        not know about the promo code.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='programs', ctx=Store())],
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='_is_global_discount_program',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='promo_code_usage',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='no_code_needed', kind=None)],
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
                                operand=Name(id='programs', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='self', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='most_interesting_program', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[Name(id='programs', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='p', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='discount_percentage',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=BinOp(
                                    left=Name(id='programs', ctx=Load()),
                                    op=Sub(),
                                    right=Name(id='most_interesting_program', ctx=Load()),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_total_order_count',
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
                                            Name(id='CouponProgram', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_total_order_count',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='program', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='program', ctx=Load()),
                                        attr='total_order_count',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='program', ctx=Load()),
                                        attr='order_count',
                                        ctx=Load(),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
