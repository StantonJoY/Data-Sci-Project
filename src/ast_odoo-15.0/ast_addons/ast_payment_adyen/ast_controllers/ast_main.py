Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='binascii', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='hmac', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
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
        ImportFrom(
            module='odoo.tools.pycompat',
            names=[alias(name='to_text', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment_adyen.const',
            names=[alias(name='CURRENCY_DECIMALS', asname=None)],
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
            name='AdyenController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='adyen_acquirer_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return public information on the acquirer.\n\n        :param int acquirer_id: The acquirer handling the transaction, as a `payment.acquirer` id\n        :return: Public information on the acquirer, namely: the state and client key\n        :rtype: str\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='payment.acquirer', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='acquirer_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='state', kind=None),
                                    Constant(value='client_key', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                        attr='adyen_client_key',
                                        ctx=Load(),
                                    ),
                                ],
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
                            args=[Constant(value='/payment/adyen/acquirer_info', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='adyen_payment_methods',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer_id', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Query the available payment methods based on the transaction context.\n\n        :param int acquirer_id: The acquirer handling the transaction, as a `payment.acquirer` id\n        :param float amount: The transaction amount\n        :param int currency_id: The transaction currency, as a `res.currency` id\n        :param int partner_id: The partner making the transaction, as a `res.partner` id\n        :return: The JSON-formatted content of the response\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
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
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='acquirer_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.currency', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='currency_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currency_code', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='currency_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='currency', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converted_amount', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='amount', ctx=Load()),
                                    Name(id='currency_code', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='to_minor_currency_units',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='amount', ctx=Load()),
                                            Name(id='currency', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='CURRENCY_DECIMALS', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='currency_code', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_sudo', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='partner_id', ctx=Load()),
                                    Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partner_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lang', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='en-US', kind=None),
                                        ],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_', kind=None),
                                    Constant(value='-', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='shopper_reference', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='partner_sudo', ctx=Load()),
                                    JoinedStr(
                                        values=[
                                            Constant(value='ODOO_PARTNER_', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='partner_sudo', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='merchantAccount', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='countryCode', kind=None),
                                    Constant(value='shopperLocale', kind=None),
                                    Constant(value='shopperReference', kind=None),
                                    Constant(value='channel', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                        attr='adyen_merchant_account',
                                        ctx=Load(),
                                    ),
                                    Name(id='converted_amount', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner_sudo', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                    Name(id='lang_code', ctx=Load()),
                                    Name(id='shopper_reference', ctx=Load()),
                                    Constant(value='Web', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                    attr='_adyen_make_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url_field_name',
                                        value=Constant(value='adyen_checkout_api_url', kind=None),
                                    ),
                                    keyword(
                                        arg='endpoint',
                                        value=Constant(value='/paymentMethods', kind=None),
                                    ),
                                    keyword(
                                        arg='payload',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='method',
                                        value=Constant(value='POST', kind=None),
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
                                    Constant(value='paymentMethods request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='response_content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/adyen/payment_methods', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='adyen_payments',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer_id', annotation=None, type_comment=None),
                            arg(arg='reference', annotation=None, type_comment=None),
                            arg(arg='converted_amount', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='payment_method', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='browser_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Make a payment request and process the feedback data.\n\n        :param int acquirer_id: The acquirer handling the transaction, as a `payment.acquirer` id\n        :param str reference: The reference of the transaction\n        :param int converted_amount: The amount of the transaction in minor units of the currency\n        :param int currency_id: The currency of the transaction, as a `res.currency` id\n        :param int partner_id: The partner making the transaction, as a `res.partner` id\n        :param dict payment_method: The details of the payment method used for the transaction\n        :param str access_token: The access token used to verify the provided values\n        :param dict browser_info: The browser info to pass to Adyen\n        :return: The JSON-formatted content of the response\n        :rtype: dict\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='payment_utils', ctx=Load()),
                                        attr='check_access_token',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='access_token', ctx=Load()),
                                        Name(id='reference', ctx=Load()),
                                        Name(id='converted_amount', ctx=Load()),
                                        Name(id='partner_id', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Adyen: ', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Received tampered payment request data.', kind=None)],
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
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='payment.acquirer', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='acquirer_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='merchantAccount', kind=None),
                                    Constant(value='amount', kind=None),
                                    Constant(value='reference', kind=None),
                                    Constant(value='paymentMethod', kind=None),
                                    Constant(value='shopperReference', kind=None),
                                    Constant(value='recurringProcessingModel', kind=None),
                                    Constant(value='shopperIP', kind=None),
                                    Constant(value='shopperInteraction', kind=None),
                                    Constant(value='storePaymentMethod', kind=None),
                                    Constant(value='additionalData', kind=None),
                                    Constant(value='channel', kind=None),
                                    Constant(value='origin', kind=None),
                                    Constant(value='browserInfo', kind=None),
                                    Constant(value='returnUrl', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='acquirer_sudo', ctx=Load()),
                                        attr='adyen_merchant_account',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='currency', kind=None),
                                        ],
                                        values=[
                                            Name(id='converted_amount', ctx=Load()),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='currency_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Name(id='reference', ctx=Load()),
                                    Name(id='payment_method', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                            attr='_adyen_compute_shopper_reference',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value='CardOnFile', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='get_customer_ip_address',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='Ecommerce', kind=None),
                                    Attribute(
                                        value=Name(id='tx_sudo', ctx=Load()),
                                        attr='tokenize',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='allow3DS2', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Constant(value='web', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='browser_info', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='url_join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                                    attr='get_base_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    Constant(value='/payment/adyen/return?merchantReference=', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='reference', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                    attr='_adyen_make_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url_field_name',
                                        value=Constant(value='adyen_checkout_api_url', kind=None),
                                    ),
                                    keyword(
                                        arg='endpoint',
                                        value=Constant(value='/payments', kind=None),
                                    ),
                                    keyword(
                                        arg='payload',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='method',
                                        value=Constant(value='POST', kind=None),
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
                                    Constant(value='payment request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
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
                                    Constant(value='adyen', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='merchantReference',
                                                value=Name(id='reference', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='response_content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/adyen/payments', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='adyen_payment_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer_id', annotation=None, type_comment=None),
                            arg(arg='reference', annotation=None, type_comment=None),
                            arg(arg='payment_details', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Submit the details of the additional actions and process the feedback data.\n\n         The additional actions can have been performed both from the inline form or during a\n         redirection.\n\n        :param int acquirer_id: The acquirer handling the transaction, as a `payment.acquirer` id\n        :param str reference: The reference of the transaction\n        :param dict payment_details: The details of the additional actions performed for the payment\n        :return: The JSON-formatted content of the response\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='acquirer_sudo', ctx=Store())],
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
                                                slice=Constant(value='payment.acquirer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='acquirer_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                    attr='_adyen_make_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url_field_name',
                                        value=Constant(value='adyen_checkout_api_url', kind=None),
                                    ),
                                    keyword(
                                        arg='endpoint',
                                        value=Constant(value='/payments/details', kind=None),
                                    ),
                                    keyword(
                                        arg='payload',
                                        value=Name(id='payment_details', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='method',
                                        value=Constant(value='POST', kind=None),
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
                                    Constant(value='payment details request response:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
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
                                    Constant(value='adyen', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='response_content', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='merchantReference',
                                                value=Name(id='reference', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='response_content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/adyen/payment_details', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='adyen_return_from_redirect',
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
                            value=Constant(value=" Process the data returned by Adyen after redirection.\n\n        The route is flagged with `save_session=False` to prevent Odoo from assigning a new session\n        to the user if they are redirected to this route with a POST request. Indeed, as the session\n        cookie is created without a `SameSite` attribute, some browsers that don't implement the\n        recommended default `SameSite=Lax` behavior will not include the cookie in the redirection\n        request from the payment provider to Odoo. As the redirection to the '/payment/status' page\n        will satisfy any specification of the `SameSite` attribute, the session of the user will be\n        retrieved and with it the transaction which will be immediately post-processed.\n\n        :param dict data: Feedback data. May include custom params sent to Adyen in the request to\n                          allow matching the transaction when redirected here.\n        ", kind=None),
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
                                    Constant(value='adyen', kind=None),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='tx_sudo', ctx=Load()),
                                    attr='operation',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='online_redirect', kind=None),
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
                                    Constant(value='handling redirection from Adyen with data:\n%s', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='adyen_payment_details',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='tx_sudo', ctx=Load()),
                                            attr='acquirer_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='merchantReference', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='details', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[Constant(value='redirectResult', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='redirectResult', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                            args=[Constant(value='/payment/adyen/return', kind=None)],
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
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='adyen_notification',
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
                            value=Constant(value=" Process the data sent by Adyen to the webhook based on the event code.\n\n        See https://docs.adyen.com/development-resources/webhooks/understand-notifications for the\n        exhaustive list of event codes.\n\n        :return: The '[accepted]' string to acknowledge the notification\n        :rtype: str\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='notification_item', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='notificationItems', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='notification_data', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='notification_item', ctx=Load()),
                                        slice=Constant(value='NotificationRequestItem', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='received_signature', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='notification_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='additionalData', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='hmacSignature', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='PaymentTransaction', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='payment.transaction', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='acquirer_sudo', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='PaymentTransaction', ctx=Load()),
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
                                                        Constant(value='adyen', kind=None),
                                                        Name(id='notification_data', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='acquirer_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_verify_notification_signature',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='received_signature', ctx=Load()),
                                                        Name(id='notification_data', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='acquirer_sudo', ctx=Load()),
                                                            attr='adyen_hmac_key',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='notification received:\n%s', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pprint', ctx=Load()),
                                                            attr='pformat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='notification_data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='success', ctx=Store())],
                                            value=Compare(
                                                left=Subscript(
                                                    value=Name(id='notification_data', ctx=Load()),
                                                    slice=Constant(value='success', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='true', kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='event_code', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='notification_data', ctx=Load()),
                                                slice=Constant(value='eventCode', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='event_code', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='AUTHORISATION', kind=None)],
                                                    ),
                                                    Name(id='success', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='notification_data', ctx=Load()),
                                                            slice=Constant(value='resultCode', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='Authorised', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='event_code', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='CANCELLATION', kind=None)],
                                                            ),
                                                            Name(id='success', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='notification_data', ctx=Load()),
                                                                    slice=Constant(value='resultCode', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='Cancelled', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='event_code', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='REFUND', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='notification_data', ctx=Load()),
                                                                            slice=Constant(value='resultCode', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=IfExp(
                                                                        test=Name(id='success', ctx=Load()),
                                                                        body=Constant(value='Authorised', kind=None),
                                                                        orelse=Constant(value='Error', kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[Continue()],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='PaymentTransaction', ctx=Load()),
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
                                                    Constant(value='adyen', kind=None),
                                                    Name(id='notification_data', ctx=Load()),
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
                                                        args=[Constant(value='unable to handle the notification data; skipping to acknowledge', kind=None)],
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
                        Return(
                            value=Constant(value='[accepted]', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/payment/adyen/notification', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_verify_notification_signature',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='received_signature', annotation=None, type_comment=None),
                            arg(arg='payload', annotation=None, type_comment=None),
                            arg(arg='hmac_key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check that the signature computed from the payload matches the received one.\n\n        See https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures\n\n        :param str received_signature: The signature sent with the notification\n        :param dict payload: The notification payload\n        :param str hmac_key: The HMAC key of the acquirer handling the transaction\n        :return: Whether the signatures match\n        :rtype: str\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='_flatten_dict',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='_value', annotation=None, type_comment=None),
                                    arg(arg='_path_base', annotation=None, type_comment=None),
                                    arg(arg='_separator', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value='', kind=None),
                                    Constant(value='.', kind=None),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Recursively generate a flat representation of a dict.\n\n            :param Object _value: The value to flatten. A dict or an already flat value\n            :param str _path_base: They base path for keys of _value, including preceding separators\n            :param str _separator: The string to use as a separator in the key path\n            ', kind=None),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='_value', ctx=Load()),
                                            Name(id='dict', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='_path_base', ctx=Store())],
                                            value=IfExp(
                                                test=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='_path_base', ctx=Load()),
                                                ),
                                                body=Name(id='_path_base', ctx=Load()),
                                                orelse=BinOp(
                                                    left=Name(id='_path_base', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='_separator', ctx=Load()),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='_key', ctx=Store()),
                                            iter=Name(id='_value', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=YieldFrom(
                                                        value=Call(
                                                            func=Name(id='_flatten_dict', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='_value', ctx=Load()),
                                                                    slice=Name(id='_key', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                BinOp(
                                                                    left=Name(id='_path_base', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='_key', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Yield(
                                                value=Tuple(
                                                    elts=[
                                                        Name(id='_path_base', ctx=Load()),
                                                        Name(id='_value', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                            name='_to_escaped_string',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='_value', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Escape payload values that are using illegal symbols and cast them to string.\n\n            String values containing `\\` or `:` are prefixed with `\\`.\n            Empty values (`None`) are replaced by an empty string.\n\n            :param Object _value: The value to escape\n            :return: The escaped value\n            :rtype: string\n            ', kind=None),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='_value', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_value', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='\\', kind=None),
                                                            Constant(value='\\\\', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=':', kind=None),
                                                    Constant(value='\\:', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='_value', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value='', kind=None),
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='_value', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='received_signature', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ignored notification with missing signature', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='signature_keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='pspReference', kind=None),
                                    Constant(value='originalReference', kind=None),
                                    Constant(value='merchantAccountCode', kind=None),
                                    Constant(value='merchantReference', kind=None),
                                    Constant(value='amount.value', kind=None),
                                    Constant(value='amount.currency', kind=None),
                                    Constant(value='eventCode', kind=None),
                                    Constant(value='success', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='flattened_payload', ctx=Store())],
                            value=DictComp(
                                key=Name(id='k', ctx=Load()),
                                value=Name(id='v', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='_flatten_dict', ctx=Load()),
                                            args=[Name(id='payload', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='signature_values', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='flattened_payload', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='key', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='key', ctx=Store()),
                                        iter=Name(id='signature_keys', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='escaped_values', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='_to_escaped_string', ctx=Load()),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='value', ctx=Store()),
                                        iter=Name(id='signature_values', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='signing_string', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=':', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='escaped_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='binary_hmac_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='binascii', ctx=Load()),
                                    attr='a2b_hex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='hmac_key', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ascii', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='binary_hmac', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='hmac', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='binary_hmac_key', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='signing_string', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='hashlib', ctx=Load()),
                                        attr='sha256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_signature', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='binary_hmac', ctx=Load()),
                                            attr='digest',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='received_signature', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='to_text', ctx=Load()),
                                        args=[Name(id='expected_signature', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ignored event with invalid signature', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
