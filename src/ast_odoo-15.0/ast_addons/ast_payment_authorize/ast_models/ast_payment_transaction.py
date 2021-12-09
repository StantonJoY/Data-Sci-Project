Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='models', asname=None),
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
            module='authorize_request',
            names=[alias(name='AuthorizeAPI', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
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
            name='PaymentTransaction',
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
                    value=Constant(value='payment.transaction', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_specific_processing_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='processing_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to return an access token as acquirer-specific processing values.\n\n        Note: self.ensure_one() from `_get_processing_values`\n\n        :param dict processing_values: The generic processing values of the transaction\n        :return: The dict of acquirer-specific processing values\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_specific_processing_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='processing_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='access_token', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='generate_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='processing_values', ctx=Load()),
                                                slice=Constant(value='reference', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='processing_values', ctx=Load()),
                                                slice=Constant(value='partner_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                    name='_authorize_create_transaction_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='opaque_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create an Authorize.Net payment transaction request.\n\n        Note: self.ensure_one()\n\n        :param dict opaque_data: The payment details obfuscated by Authorize.Net\n        :return:\n        ', kind=None),
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
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='capture_manually',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='operation',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='validation', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='authorize_API', ctx=Load()),
                                            attr='authorize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='opaque_data',
                                                value=Name(id='opaque_data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='authorize_API', ctx=Load()),
                                            attr='auth_and_capture',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='opaque_data',
                                                value=Name(id='opaque_data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_payment_request',
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
                            value=Constant(value=' Override of payment to send a payment request to Authorize.\n\n        Note: self.ensure_one()\n\n        :return: None\n        :raise: UserError if the transaction is not linked to a token\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_payment_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='token_id',
                                        ctx=Load(),
                                    ),
                                    attr='authorize_profile',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Authorize.Net: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The transaction is not linked to a token.', kind=None)],
                                                    keywords=[],
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
                        Assign(
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='acquirer_id',
                                    ctx=Load(),
                                ),
                                attr='capture_manually',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='authorize_API', ctx=Load()),
                                            attr='authorize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='token',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='token_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='authorize request response:\n%s', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='pprint', ctx=Load()),
                                                    attr='pformat',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='res_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='authorize_API', ctx=Load()),
                                            attr='auth_and_capture',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='token',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='token_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='auth_and_capture request response:\n%s', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='pprint', ctx=Load()),
                                                    attr='pformat',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='feedback_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='reference', kind=None),
                                    Constant(value='response', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='res_content', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='authorize', kind=None),
                                    Name(id='feedback_data', ctx=Load()),
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
                    name='_send_refund_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='amount_to_refund', annotation=None, type_comment=None),
                            arg(arg='create_refund_transaction', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to send a refund request to Authorize.\n\n        Note: self.ensure_one()\n\n        :param float amount_to_refund: The amount to refund\n        :param bool create_refund_transaction: Whether a refund transaction should be created or not\n        :return: The refund transaction if any\n        :rtype: recordset of `payment.transaction`\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_send_refund_request',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='amount_to_refund',
                                                value=Name(id='amount_to_refund', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='create_refund_transaction',
                                                value=Name(id='create_refund_transaction', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='refund_tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_refund_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='amount_to_refund',
                                        value=Name(id='amount_to_refund', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='create_refund_transaction',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rounded_amount', ctx=Store())],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='authorize_API', ctx=Load()),
                                    attr='refund',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='rounded_amount', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='refund request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='feedback_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='reference', kind=None),
                                    Constant(value='response', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='res_content', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='authorize', kind=None),
                                    Name(id='feedback_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='refund_tx', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_capture_request',
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
                            value=Constant(value=' Override of payment to send a capture request to Authorize.\n\n        Note: self.ensure_one()\n\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_capture_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rounded_amount', ctx=Store())],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='amount',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        attr='decimal_places',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='authorize_API', ctx=Load()),
                                    attr='capture',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='rounded_amount', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='capture request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='feedback_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='reference', kind=None),
                                    Constant(value='response', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='res_content', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='authorize', kind=None),
                                    Name(id='feedback_data', ctx=Load()),
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
                    name='_send_void_request',
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
                            value=Constant(value=' Override of payment to send a void request to Authorize.\n\n        Note: self.ensure_one()\n\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_void_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='authorize_API', ctx=Load()),
                                    attr='void',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_reference',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='void request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='feedback_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='reference', kind=None),
                                    Constant(value='response', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
                                    ),
                                    Name(id='res_content', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='authorize', kind=None),
                                    Name(id='feedback_data', ctx=Load()),
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
                    name='_get_tx_from_feedback_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='provider', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find the transaction based on the feedback data.\n\n        :param str provider: The provider of the acquirer that handled the transaction\n        :param dict data: The feedback data sent by the acquirer\n        :return: The transaction if found\n        :rtype: recordset of `payment.transaction`\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_tx_from_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='provider', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='provider', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='tx', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='reference', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='reference', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='reference', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='reference', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='provider', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='authorize', kind=None),
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
                                operand=Name(id='tx', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Authorize.Net: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='No transaction found matching reference %s.', kind=None),
                                                        Name(id='reference', ctx=Load()),
                                                    ],
                                                    keywords=[],
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
                        Return(
                            value=Name(id='tx', ctx=Load()),
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
                    name='_process_feedback_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override of payment to process the transaction based on Authorize data.\n\n        Note: self.ensure_one()\n\n        :param dict data: The feedback data sent by the provider\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_process_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='provider',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='authorize', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='response_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='response', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='acquirer_reference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response_content', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='x_trans_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response_content', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='x_response_code', kind=None),
                                    Constant(value='3', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status_code', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='1', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='status_type', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response_content', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='x_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='status_type', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='auth_capture', kind=None),
                                                    Constant(value='prior_auth_capture', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_set_done',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tokenize',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='token_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_authorize_tokenize',
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='status_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='auth_only', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_set_authorized',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='tokenize',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='token_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_authorize_tokenize',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='operation',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='validation', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_send_refund_request',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='create_refund_transaction',
                                                                        value=Constant(value=False, kind=None),
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
                                                    test=Compare(
                                                        left=Name(id='status_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='void', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='operation',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='validation', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_set_done',
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
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_set_canceled',
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
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='status_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='2', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_set_canceled',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='status_code', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='4', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_set_pending',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='error_code', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='response_content', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='x_response_reason_text', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='received data with invalid status code %s and error code %s', kind=None),
                                                            Name(id='status_code', ctx=Load()),
                                                            Name(id='error_code', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_set_error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Authorize.Net: ', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Received data with status code "%(status)s" and error code "%(error)s"', kind=None)],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='status',
                                                                            value=Name(id='status_code', ctx=Load()),
                                                                        ),
                                                                        keyword(
                                                                            arg='error',
                                                                            value=Name(id='error_code', ctx=Load()),
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
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_authorize_tokenize',
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
                            value=Constant(value=' Create a token for the current transaction.\n\n        Note: self.ensure_one()\n\n        :return: None\n        ', kind=None),
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
                            targets=[Name(id='authorize_API', ctx=Store())],
                            value=Call(
                                func=Name(id='AuthorizeAPI', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cust_profile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='authorize_API', ctx=Load()),
                                    attr='create_customer_profile',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='acquirer_reference',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='create_customer_profile request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cust_profile', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='cust_profile', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.token', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='acquirer_id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='acquirer_ref', kind=None),
                                                    Constant(value='authorize_profile', kind=None),
                                                    Constant(value='authorize_payment_method_type', kind=None),
                                                    Constant(value='verified', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='acquirer_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cust_profile', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
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
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cust_profile', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='payment_profile_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cust_profile', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='profile_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='acquirer_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='authorize_payment_method_type',
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
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='token_id', kind=None),
                                                    Constant(value='tokenize', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='created token with id %s for partner with id %s', kind=None),
                                            Attribute(
                                                value=Name(id='token', ctx=Load()),
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
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
