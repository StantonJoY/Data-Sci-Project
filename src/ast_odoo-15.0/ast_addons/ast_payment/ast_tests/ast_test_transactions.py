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
            name='TestTransactions',
            bases=[Name(id='PaymentCommon', ctx=Load())],
            keywords=[],
            body=[
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
                                        value=Name(id='tx', ctx=Load()),
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
                FunctionDef(
                    name='test_refund_transaction_values',
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
                        Assign(
                            targets=[Name(id='refund_tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_create_refund_transaction',
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
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    JoinedStr(
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
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The reference of the refund transaction should be the prefixed reference of the source transaction.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The amount of a refund transaction should always be negative.', kind=None),
                                    ),
                                ],
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
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='amount',
                                            ctx=Load(),
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
                                        value=Constant(value='The amount of the refund transaction should be taken from the amount of the source transaction.', kind=None),
                                    ),
                                ],
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
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The currency of the refund transaction should that of the source transaction.', kind=None),
                                    ),
                                ],
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
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='operation',
                                        ctx=Load(),
                                    ),
                                    Constant(value='refund', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value="The operation of the refund transaction should be 'refund'.", kind=None),
                                    ),
                                ],
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
                                    Name(id='tx', ctx=Load()),
                                    Attribute(
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='source_transaction_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The refund transaction should be linked to the source transaction.', kind=None),
                                    ),
                                ],
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
                                        value=Name(id='refund_tx', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The partner of the refund transaction should that of the source transaction.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='partial_refund_tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_create_refund_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='amount_to_refund',
                                        value=Constant(value=11.11, kind=None),
                                    ),
                                ],
                            ),
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
                                        value=Name(id='partial_refund_tx', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=11.11, kind=None),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='places',
                                        value=Constant(value=2, kind=None),
                                    ),
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='The amount of the refund transaction should be the negative value of the amount to refund.', kind=None),
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
                    name='test_no_payment_for_validations',
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
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='flow',
                                        value=Constant(value='dummy', kind=None),
                                    ),
                                    keyword(
                                        arg='operation',
                                        value=Constant(value='validation', kind=None),
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
                        Assign(
                            targets=[Name(id='payment_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.payment', kind=None),
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
                                                    Constant(value='payment_transaction_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='tx', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='payment_count', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='validation transactions should not create payments', kind=None),
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
