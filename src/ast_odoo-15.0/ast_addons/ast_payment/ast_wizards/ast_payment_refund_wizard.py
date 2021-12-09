Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='PaymentRefundWizard',
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
                    value=Constant(value='payment.refund.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Payment Refund Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Payment', kind=None),
                            ),
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='account.payment', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
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
                                        args=[Constant(value='active_id', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='transaction_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Payment Transaction', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='payment_id.payment_transaction_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='payment_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Payment Amount', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='payment_id.amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='refunded_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Refunded Amount', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_refunded_amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_available_for_refund', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Maximum Refund Allowed', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='payment_id.amount_available_for_refund', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_to_refund', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Refund Amount', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_amount_to_refund', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
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
                                arg='string',
                                value=Constant(value='Currency', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='transaction_id.currency_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='support_refund', ctx=Store())],
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
                                value=Constant(value='transaction_id.acquirer_id.support_refund', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='has_pending_refund', ctx=Store())],
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
                                value=Constant(value='Has a pending refund', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_has_pending_refund', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_amount_to_refund_within_boundaries',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Constant(value=0, kind=None),
                                            ops=[
                                                Lt(),
                                                LtE(),
                                            ],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='amount_to_refund',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='amount_available_for_refund',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='The amount to be refunded must be positive and cannot be superior to %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='wizard', ctx=Load()),
                                                                attr='amount_available_for_refund',
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='amount_to_refund', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_refunded_amount',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='refunded_amount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='payment_amount',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='amount_available_for_refund',
                                            ctx=Load(),
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
                            args=[Constant(value='amount_available_for_refund', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_amount_to_refund',
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
                            value=Constant(value=' Set the default amount to refund to the amount available for refund. ', kind=None),
                        ),
                        For(
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='amount_to_refund',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='amount_available_for_refund',
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
                            args=[Constant(value='amount_available_for_refund', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_has_pending_refund',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pending_refunds_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
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
                                                            Constant(value='source_transaction_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='wizard', ctx=Load()),
                                                                        attr='payment_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='payment_transaction_id',
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
                                                            Constant(value='operation', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='refund', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='draft', kind=None),
                                                                    Constant(value='pending', kind=None),
                                                                    Constant(value='authorized', kind=None),
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='has_pending_refund',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Name(id='pending_refunds_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
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
                            args=[Constant(value='payment_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_refund',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='transaction_id',
                                                ctx=Load(),
                                            ),
                                            attr='action_refund',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='amount_to_refund',
                                                value=Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='amount_to_refund',
                                                    ctx=Load(),
                                                ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
