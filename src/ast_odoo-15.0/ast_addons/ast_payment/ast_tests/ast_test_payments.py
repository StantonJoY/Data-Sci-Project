Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment.tests.common',
            names=[alias(name='PaymentCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPayments',
            bases=[Name(id='PaymentCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_no_amount_available_for_refund_when_not_supported',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='support_refund',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
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
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount_available_for_refund',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The value of `amount_available_for_refund` should be 0 when the acquirer doesn't support refunds.", kind=None),
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
                    name='test_full_amount_available_for_refund_when_not_yet_refunded',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='support_refund',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='full_only', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount_available_for_refund',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='places',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The value of `amount_available_for_refund` should be that of `total` when there are no linked refunds.', kind=None),
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
                    name='test_full_amount_available_for_refund_when_refunds_are_pending',
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
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='support_refund', kind=None),
                                            Constant(value='support_authorization', kind=None),
                                        ],
                                        values=[
                                            Constant(value='full_only', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='reference_index', ctx=Store()),
                                    Name(id='state', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='pending', kind=None),
                                            Constant(value='authorized', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_transaction',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='dummy', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='amount',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='reference',
                                                value=JoinedStr(
                                                    values=[
                                                        Constant(value='R-', kind=None),
                                                        FormattedValue(
                                                            value=Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='reference',
                                                                ctx=Load(),
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='-', kind=None),
                                                        FormattedValue(
                                                            value=BinOp(
                                                                left=Name(id='reference_index', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='state',
                                                value=Name(id='state', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='operation',
                                                value=Constant(value='refund', kind=None),
                                            ),
                                            keyword(
                                                arg='source_transaction_id',
                                                value=Attribute(
                                                    value=Name(id='tx', ctx=Load()),
                                                    attr='id',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount_available_for_refund',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='places',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The value of `amount_available_for_refund` should be that of `total` when all the linked refunds are pending (not in the state 'done').", kind=None),
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
                    name='test_no_amount_available_for_refund_when_fully_refunded',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='support_refund',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='full_only', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_transaction',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='dummy', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='amount',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='reference',
                                                value=JoinedStr(
                                                    values=[
                                                        Constant(value='R-', kind=None),
                                                        FormattedValue(
                                                            value=Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='reference',
                                                                ctx=Load(),
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='state',
                                                value=Constant(value='done', kind=None),
                                            ),
                                            keyword(
                                                arg='operation',
                                                value=Constant(value='refund', kind=None),
                                            ),
                                            keyword(
                                                arg='source_transaction_id',
                                                value=Attribute(
                                                    value=Name(id='tx', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='_reconcile_after_done',
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
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount_available_for_refund',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The value of `amount_available_for_refund` should be 0 when there is a linked refund of the full amount that is confirmed (state 'done').", kind=None),
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
                    name='test_no_full_amount_available_for_refund_when_partially_refunded',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='support_refund',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='partial', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_transaction',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='dummy', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='amount',
                                                value=UnaryOp(
                                                    op=USub(),
                                                    operand=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='tx', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Constant(value=10, kind=None),
                                                    ),
                                                ),
                                            ),
                                            keyword(
                                                arg='reference',
                                                value=JoinedStr(
                                                    values=[
                                                        Constant(value='R-', kind=None),
                                                        FormattedValue(
                                                            value=Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='reference',
                                                                ctx=Load(),
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='state',
                                                value=Constant(value='done', kind=None),
                                            ),
                                            keyword(
                                                arg='operation',
                                                value=Constant(value='refund', kind=None),
                                            ),
                                            keyword(
                                                arg='source_transaction_id',
                                                value=Attribute(
                                                    value=Name(id='tx', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='_reconcile_after_done',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='amount_available_for_refund',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='tx', ctx=Load()),
                                                attr='payment_id',
                                                ctx=Load(),
                                            ),
                                            attr='amount',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=BinOp(
                                            left=Attribute(
                                                value=Name(id='tx', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            op=Div(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='places',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The value of `amount_available_for_refund` should be equal to the total amount minus the sum of the absolute amount of the refunds that are confirmed (state 'done').", kind=None),
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
                    name='test_refunds_count',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer',
                                        ctx=Load(),
                                    ),
                                    attr='support_refund',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='full_only', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='redirect', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='state',
                                        value=Constant(value='done', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_reconcile_after_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='reference_index', ctx=Store()),
                                    Name(id='operation', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='online_redirect', kind=None),
                                            Constant(value='online_direct', kind=None),
                                            Constant(value='online_token', kind=None),
                                            Constant(value='validation', kind=None),
                                            Constant(value='refund', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='create_transaction',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='dummy', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='reference',
                                                        value=JoinedStr(
                                                            values=[
                                                                Constant(value='R-', kind=None),
                                                                FormattedValue(
                                                                    value=Attribute(
                                                                        value=Name(id='tx', ctx=Load()),
                                                                        attr='reference',
                                                                        ctx=Load(),
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value='-', kind=None),
                                                                FormattedValue(
                                                                    value=BinOp(
                                                                        left=Name(id='reference_index', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='state',
                                                        value=Constant(value='done', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='operation',
                                                        value=Name(id='operation', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='source_transaction_id',
                                                        value=Attribute(
                                                            value=Name(id='tx', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='_reconcile_after_done',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='payment_id',
                                            ctx=Load(),
                                        ),
                                        attr='refunds_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The refunds count should only consider transactions with operation 'refund'.", kind=None),
                                    ),
                                ],
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
