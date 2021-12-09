Module(
    body=[
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='PaymentLinkWizard',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='payment.link.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Generate Sales Payment Link', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
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
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='res_model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale.order', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='res_id', kind=None),
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
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='description', kind=None),
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='amount_max', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='amount_total',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='sum', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    attr='invoice_ids',
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
                                                                                        ops=[NotEq()],
                                                                                        comparators=[Constant(value='cancel', kind=None)],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='mapped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='amount_total', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='currency_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='amount_total',
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
                    name='_compute_available_acquirer_ids',
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
                            targets=[Name(id='sale_links', ctx=Store())],
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
                                            args=[arg(arg='link', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='link', ctx=Load()),
                                                attr='res_model',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='sale.order', kind=None)],
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
                                            Name(id='PaymentLinkWizard', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='sale_links', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_available_acquirer_ids',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='link', ctx=Store()),
                            iter=Name(id='sale_links', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='link', ctx=Load()),
                                            attr='available_acquirer_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='link', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_compatible_acquirers',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='company_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='link', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='link', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='currency_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='link', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sale_order_id',
                                                value=Attribute(
                                                    value=Name(id='link', ctx=Load()),
                                                    attr='res_id',
                                                    ctx=Load(),
                                                ),
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
                            args=[
                                Constant(value='company_id', kind=None),
                                Constant(value='partner_id', kind=None),
                                Constant(value='currency_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_link',
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
                            value=Constant(value=' Override of payment to add the sale_order_id in the link. ', kind=None),
                        ),
                        For(
                            target=Name(id='payment_link', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='payment_link', ctx=Load()),
                                            attr='res_model',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale.order', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='related_document', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='payment_link', ctx=Load()),
                                                            attr='res_model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='payment_link', ctx=Load()),
                                                        attr='res_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='base_url', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='related_document', ctx=Load()),
                                                    attr='get_base_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='payment_link', ctx=Load()),
                                                    attr='link',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='base_url', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='/payment/pay?reference=', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='urls', ctx=Load()),
                                                                attr='url_quote',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='payment_link', ctx=Load()),
                                                                    attr='description',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='&amount=', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='payment_link', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='&sale_order_id=', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='payment_link', ctx=Load()),
                                                            attr='res_id',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    FormattedValue(
                                                        value=IfExp(
                                                            test=Attribute(
                                                                value=Name(id='payment_link', ctx=Load()),
                                                                attr='acquirer_id',
                                                                ctx=Load(),
                                                            ),
                                                            body=BinOp(
                                                                left=Constant(value='&acquirer_id=', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='payment_link', ctx=Load()),
                                                                                attr='acquirer_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            orelse=Constant(value='', kind=None),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='&access_token=', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='payment_link', ctx=Load()),
                                                            attr='access_token',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='super', ctx=Load()),
                                                        args=[
                                                            Name(id='PaymentLinkWizard', ctx=Load()),
                                                            Name(id='payment_link', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='_generate_link',
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
