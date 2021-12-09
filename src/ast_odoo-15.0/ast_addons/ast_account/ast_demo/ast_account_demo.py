Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
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
                alias(name='Command', asname=None),
            ],
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
            module='odoo.tools.misc',
            names=[alias(name='file_open', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='AccountChartTemplate',
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
                    value=Constant(value='account.chart.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_demo_data',
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
                            value=Constant(value='Generate the demo data related to accounting.', kind=None),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_move',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_statement',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_reconcile_model',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_attachment',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_mail_message',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_demo_data_mail_activity',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
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
                    name='_get_demo_data_move',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='account.move', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_2', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_3', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_followup', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_5', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_extract', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_invoice_equipment_purchase', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_payment_term_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_12', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.account_payment_term_end_following_month', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-01', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_02', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_03', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_2', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-08', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_03', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_01', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=20, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_2', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-08', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_01', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_03', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_payment_term_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_2', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.account_payment_term_immediate', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Call(
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
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='timedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=15, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-%d', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_02', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='product.consu_delivery_03', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_payment_term_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='in_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_12', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.account_payment_term_end_following_month', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-01', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='ref', ctx=Load()),
                                                                                args=[Constant(value='product.product_delivery_01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=10.0, kind=None),
                                                                            Constant(value=1, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='ref', ctx=Load()),
                                                                                args=[Constant(value='product.product_order_01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=4.0, kind=None),
                                                                            Constant(value=5, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='in_invoice', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='ref', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_user_id', kind=None),
                                                    Constant(value='invoice_date', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='in_invoice', kind=None),
                                                    Constant(value='INV/2018/0057', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.res_partner_12', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='2018-09-17', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Redeem Reference Number: PO02529', kind=None),
                                                                            Constant(value=1, kind=None),
                                                                            Constant(value=541.1, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_get_demo_data_statement',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='account.bank.statement', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_demo_bank_statement_1', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='journal_id', kind=None),
                                                    Constant(value='date', kind=None),
                                                    Constant(value='balance_end_real', kind=None),
                                                    Constant(value='balance_start', kind=None),
                                                    Constant(value='line_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='account.journal', kind=None),
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
                                                                                Constant(value='type', kind=None),
                                                                                Constant(value='=', kind=None),
                                                                                Constant(value='bank', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='company_id', kind=None),
                                                                                Constant(value='=', kind=None),
                                                                                Name(id='cid', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='limit',
                                                                    value=Constant(value=1, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='time', ctx=Load()),
                                                                attr='strftime',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='%Y', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='-01-01', kind=None),
                                                    ),
                                                    Constant(value=9944.87, kind=None),
                                                    Constant(value=5103.0, kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='INV/%Y/00002 and INV/%Y/00003', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=1275.0, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='base.res_partner_12', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Bank Fees', kind=None),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=32.58, kind=None),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Prepayment', kind=None),
                                                                            Constant(value=650, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='base.res_partner_12', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='First 2000 $ of invoice %Y/00001', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=2000, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='base.res_partner_12', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Last Year Interests', kind=None),
                                                                            Constant(value=102.78, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='INV/%Y/00002', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=750, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='base.res_partner_2', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='payment_ref', kind=None),
                                                                            Constant(value='amount', kind=None),
                                                                            Constant(value='date', kind=None),
                                                                            Constant(value='partner_id', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='R:9772938  10/07 AX 9415116318 T:5 BRT: 100,00€ C/ croip', kind=None),
                                                                            Constant(value=96.67, kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='time', ctx=Load()),
                                                                                    attr='strftime',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[Constant(value='base.res_partner_2', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_get_demo_data_reconcile_model',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='account.reconcile.model', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_reconcile_from_label', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='rule_type', kind=None),
                                                    Constant(value='match_label', kind=None),
                                                    Constant(value='match_label_param', kind=None),
                                                    Constant(value='decimal_separator', kind=None),
                                                    Constant(value='line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Line with Bank Fees', kind=None),
                                                    Constant(value='writeoff_suggestion', kind=None),
                                                    Constant(value='contains', kind=None),
                                                    Constant(value='BRT', kind=None),
                                                    Constant(value=',', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='label', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='amount_type', kind=None),
                                                                            Constant(value='amount_string', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Due amount', kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_get_demo_account',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Constant(value='income', kind=None),
                                                                                        Constant(value='account.data_account_type_revenue', kind=None),
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
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='regex', kind=None),
                                                                            Constant(value='BRT: ([\\d,]+)', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='label', kind=None),
                                                                            Constant(value='account_id', kind=None),
                                                                            Constant(value='amount_type', kind=None),
                                                                            Constant(value='amount_string', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='Bank Fees', kind=None),
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_get_demo_account',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Constant(value='cost_of_goods_sold', kind=None),
                                                                                        Constant(value='account.data_account_type_direct_costs', kind=None),
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
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='percentage', kind=None),
                                                                            Constant(value='100', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_get_demo_data_attachment',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='ir.attachment', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_ir_attachment_bank_statement_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_ir_attachment_in_invoice_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_ir_attachment_in_invoice_2', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='raw', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='binary', kind=None),
                                                    Constant(value='bank_statement_yourcompany_demo.pdf', kind=None),
                                                    Constant(value='account.bank.statement', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_bank_statement_1', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='file_open', ctx=Load()),
                                                                args=[
                                                                    Constant(value='account/static/demo/bank_statement_yourcompany_1.pdf', kind=None),
                                                                    Constant(value='rb', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='raw', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='binary', kind=None),
                                                    Constant(value='in_invoice_yourcompany_demo.pdf', kind=None),
                                                    Constant(value='account.move', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_extract', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='file_open', ctx=Load()),
                                                                args=[
                                                                    Constant(value='account/static/demo/in_invoice_yourcompany_demo_1.pdf', kind=None),
                                                                    Constant(value='rb', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='raw', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='binary', kind=None),
                                                    Constant(value='in_invoice_yourcompany_demo.pdf', kind=None),
                                                    Constant(value='account.move', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_equipment_purchase', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='file_open', ctx=Load()),
                                                                args=[
                                                                    Constant(value='account/static/demo/in_invoice_yourcompany_demo_2.pdf', kind=None),
                                                                    Constant(value='rb', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='read',
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
                    name='_get_demo_data_mail_message',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='mail.message', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_mail_message_bank_statement_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_mail_message_in_invoice_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_mail_message_in_invoice_2', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='author_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='account.bank.statement', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_bank_statement_1', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='Bank statement attachment', kind=None),
                                                    Constant(value='comment', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.partner_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[
                                                                                        JoinedStr(
                                                                                            values=[
                                                                                                Constant(value='account.', kind=None),
                                                                                                FormattedValue(
                                                                                                    value=Name(id='cid', ctx=Load()),
                                                                                                    conversion=-1,
                                                                                                    format_spec=None,
                                                                                                ),
                                                                                                Constant(value='_ir_attachment_bank_statement_1', kind=None),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
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
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='author_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='account.move', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_extract', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='Vendor Bill attachment', kind=None),
                                                    Constant(value='comment', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.partner_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[
                                                                                        JoinedStr(
                                                                                            values=[
                                                                                                Constant(value='account.', kind=None),
                                                                                                FormattedValue(
                                                                                                    value=Name(id='cid', ctx=Load()),
                                                                                                    conversion=-1,
                                                                                                    format_spec=None,
                                                                                                ),
                                                                                                Constant(value='_ir_attachment_in_invoice_1', kind=None),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
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
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='author_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='account.move', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_equipment_purchase', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='Vendor Bill attachment', kind=None),
                                                    Constant(value='comment', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.partner_demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Name(id='ref', ctx=Load()),
                                                                                    args=[
                                                                                        JoinedStr(
                                                                                            values=[
                                                                                                Constant(value='account.', kind=None),
                                                                                                FormattedValue(
                                                                                                    value=Name(id='cid', ctx=Load()),
                                                                                                    conversion=-1,
                                                                                                    format_spec=None,
                                                                                                ),
                                                                                                Constant(value='_ir_attachment_in_invoice_2', kind=None),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
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
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_get_demo_data_mail_activity',
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
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='ref',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='mail.activity', kind=None),
                                    Dict(
                                        keys=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_invoice_activity_1', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_invoice_activity_2', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_invoice_activity_3', kind=None),
                                                ],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='cid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='_invoice_activity_4', kind=None),
                                                ],
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model_id', kind=None),
                                                    Constant(value='activity_type_id', kind=None),
                                                    Constant(value='date_deadline', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_3', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.model_account_move', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='mail.mail_activity_data_todo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='fields', ctx=Load()),
                                                                            attr='Datetime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='today',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=Constant(value=5, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-%d %H:%M', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Follow-up on payment', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model_id', kind=None),
                                                    Constant(value='activity_type_id', kind=None),
                                                    Constant(value='date_deadline', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_2', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.model_account_move', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='mail.mail_activity_data_call', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-%d %H:%M', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model_id', kind=None),
                                                    Constant(value='activity_type_id', kind=None),
                                                    Constant(value='date_deadline', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_1', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.model_account_move', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='mail.mail_activity_data_todo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='fields', ctx=Load()),
                                                                            attr='Datetime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='today',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=Constant(value=5, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-%d %H:%M', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Include upsell', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model_id', kind=None),
                                                    Constant(value='activity_type_id', kind=None),
                                                    Constant(value='date_deadline', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[
                                                                JoinedStr(
                                                                    values=[
                                                                        Constant(value='account.', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='cid', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='_demo_invoice_extract', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='account.model_account_move', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='mail.mail_activity_data_todo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='fields', ctx=Load()),
                                                                            attr='Datetime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='today',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='days',
                                                                            value=Constant(value=5, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%Y-%m-%d %H:%M', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Update address', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Name(id='ref', ctx=Load()),
                                                            args=[Constant(value='base.user_admin', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
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
                    name='_post_create_demo_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='created', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cid', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='created', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='account.move', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='created', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='created', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='check_move_validity',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Name(id='created', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='_onchange_partner_id',
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
                                                value=Name(id='created', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='_onchange_product_id',
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
                                                value=Name(id='created', ctx=Load()),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='_onchange_account_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='created', ctx=Load()),
                                            attr='_recompute_dynamic_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='recompute_all_taxes',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='recompute_tax_base_amount',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=BinOp(
                                        left=Name(id='created', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
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
                                                JoinedStr(
                                                    values=[
                                                        Constant(value='account.', kind=None),
                                                        FormattedValue(
                                                            value=Name(id='cid', ctx=Load()),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='_demo_invoice_extract', kind=None),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='action_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='UserError', ctx=Load()),
                                                            Name(id='ValidationError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Error while posting demo data', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='created', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='account.bank.statement', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='created', ctx=Load()),
                                                    attr='button_post',
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
                    name='_get_demo_account',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml_id', annotation=None, type_comment=None),
                            arg(arg='user_type_id', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Find the most appropriate account possible for demo data creation.\n\n        :param xml_id (str): the xml_id of the account template in the generic coa\n        :param user_type_id (str): the full xml_id of the account type wanted\n        :param company (Model<res.company>): the company for which we search the account\n        :return (Model<account.account>): the most appropriate record found\n        ', kind=None),
                        ),
                        Return(
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
                                                slice=Constant(value='account.account', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
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
                                                                    slice=Constant(value='ir.model.data', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
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
                                                                        Constant(value='=', kind=None),
                                                                        BinOp(
                                                                            left=Constant(value='%d_%s', kind=None),
                                                                            op=Mod(),
                                                                            right=Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='company', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='xml_id', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='model', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Constant(value='account.account', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='module', kind=None),
                                                                        Constant(value='=like', kind=None),
                                                                        Constant(value='l10n%', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='limit',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='res_id',
                                                ctx=Load(),
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
                                                slice=Constant(value='account.account', kind=None),
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
                                                            Constant(value='user_type_id', kind=None),
                                                            Constant(value='=', kind=None),
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
                                                                    args=[Name(id='user_type_id', ctx=Load())],
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
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
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
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.account', kind=None),
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
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company', ctx=Load()),
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
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
