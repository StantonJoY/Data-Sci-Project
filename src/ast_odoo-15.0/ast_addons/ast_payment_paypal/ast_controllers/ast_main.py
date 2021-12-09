Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='http', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
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
            name='PaypalController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_return_url', ctx=Store())],
                    value=Constant(value='/payment/paypal/dpn/', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_notify_url', ctx=Store())],
                    value=Constant(value='/payment/paypal/ipn/', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='paypal_dpn',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='data', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Route used by the PDT notification.\n\n        The "PDT notification" is actually POST data sent along the user redirection.\n        The route also allows the GET method in case the user clicks on "go back to merchant site".\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='beginning DPN with post data:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_validate_data_authenticity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='data', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='payment.transaction', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='_handle_feedback_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='paypal', kind=None),
                                                    Name(id='data', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[Pass()],
                                ),
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/payment/status', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Name(id='_return_url', ctx=Load())],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[
                                            Constant(value='GET', kind=None),
                                            Constant(value='POST', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='paypal_ipn',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='data', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Route used by the IPN. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='beginning IPN with post data:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_validate_data_authenticity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='payment.transaction', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_handle_feedback_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='paypal', kind=None),
                                            Name(id='data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='unable to handle the IPN data; skipping to acknowledge the notif', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Name(id='_notify_url', ctx=Load())],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[
                                            Constant(value='GET', kind=None),
                                            Constant(value='POST', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_validate_data_authenticity',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='data', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Validate the authenticity of data received through DPN or IPN\n\n        The verification is done in three steps:\n          - 1: POST the complete, unaltered, message back to Paypal (preceded by\n               `cmd=_notify-validate`), in the same encoding.\n          - 2: PayPal sends back either 'VERIFIED' or 'INVALID'.\n          - 3: Return an empty HTTP 200 response (done at the end of the route method).\n        See https://developer.paypal.com/docs/api-basics/notifications/ipn/IPNIntro\n\n        As per https://developer.paypal.com/docs/api-basics/notifications/payment-data-transfer/,\n        PDT notifications should be verified in a similar but different manner:\n          - The transaction ID should be retrieved from the GET param `tx`.\n          - The POST should use `_notify-synch` (as per previous versions of this method) as `cmd`,\n            and only have as params the transaction ID and the PDT Identity Token (under the key\n            `at`, as per previous versions of this method).\n          - The payment data should be parsed from the response of the check request.\n        In practice, however, the transaction ID is never given by PayPal and the documentation\n        has no mention of `_notify_synch` nor `at`. Because of this, PDT cannot be verified as\n        prescribed by the documentation.\n        Nevertheless, previous versions of this method used a bad heuristic (assessing the presence\n        of the optional, PDT-specific, param `amt`) to determine whether the notification was a PDT.\n        Since PDT notifications have in practice always been successfully authenticated by using the\n        IPN protocol, this method does explicitly that for both PDT and IPN.\n\n        :param dict data: The data whose authenticity to check\n        :return: None\n        :raise: ValidationError if the authenticity could not be verified\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='payment.transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_tx_from_feedback_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='paypal', kind=None),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                            value=Attribute(
                                value=Name(id='tx_sudo', ctx=Load()),
                                attr='acquirer_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='cmd', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='_notify-validate', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                            attr='_paypal_get_api_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=60, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='raise_for_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response_code', ctx=Store())],
                            value=Attribute(
                                value=Name(id='response', ctx=Load()),
                                attr='text',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='response_code', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='VERIFIED', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='authenticity of notification data verified', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='response_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='INVALID', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_message', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='PayPal: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Notification data were not acknowledged.', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='error_message', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='PayPal: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='Received unrecognized authentication check response code: received %s, expected VERIFIED or INVALID.', kind=None),
                                                        Name(id='response_code', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='_set_error',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='error_message', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[Name(id='error_message', ctx=Load())],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
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
