Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        ImportFrom(
            module='uuid',
            names=[alias(name='uuid4', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.payment',
            names=[alias(name='utils', asname='payment_utils')],
            level=0,
        ),
        Import(
            names=[alias(name='requests', asname=None)],
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
            name='AuthorizeAPI',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Authorize.net Gateway API integration.\n\n    This class allows contacting the Authorize.net API with simple operation\n    requests. It implements a *very limited* subset of the complete API\n    (http://developer.authorize.net/api/reference); namely:\n        - Customer Profile/Payment Profile creation\n        - Transaction authorization/capture/voiding\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='AUTH_ERROR_STATUS', ctx=Store())],
                    value=Constant(value='3', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='acquirer', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Initiate the environment with the acquirer data.\n\n        :param recordset acquirer: payment.acquirer account that will be contacted\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='acquirer', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='enabled', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='https://api.authorize.net/xml/v1/request.api', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='https://apitest.authorize.net/xml/v1/request.api', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='acquirer', ctx=Load()),
                                attr='state',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='acquirer', ctx=Load()),
                                attr='authorize_login',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='transaction_key',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='acquirer', ctx=Load()),
                                attr='authorize_transaction_key',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='payment_method_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='acquirer', ctx=Load()),
                                attr='authorize_payment_method_type',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_make_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operation', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='request', ctx=Store())],
                            value=Dict(
                                keys=[Name(id='operation', ctx=Load())],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='merchantAuthentication', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='transactionKey', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='transaction_key',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='data', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
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
                                    Constant(value='sending request to %s:\n%s', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='request', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='request', ctx=Load())],
                                        keywords=[],
                                    ),
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
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='content',
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
                                    Constant(value='response received:\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='messages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='messages', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='messages', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='messages', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='resultCode', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='Error', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='err_code', kind=None),
                                            Constant(value='err_msg', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='messages', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='message', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='code', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='messages', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='message', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='text', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_format_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                            arg(arg='operation', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='response', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='err_code', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='x_response_code', kind=None),
                                            Constant(value='x_response_reason_text', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='AUTH_ERROR_STATUS',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='err_msg', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='x_response_code', kind=None),
                                            Constant(value='x_trans_id', kind=None),
                                            Constant(value='x_type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='transactionResponse', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='responseCode', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='transactionResponse', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='transId', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='operation', ctx=Load()),
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
                    name='create_customer_profile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                            arg(arg='transaction_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create an Auth.net payment/customer profile from an existing transaction.\n\n        Creates a customer profile for the partner/credit card combination and links\n        a corresponding payment profile to it. Note that a single partner in the Odoo\n        database can have multiple customer profiles in Authorize.net (i.e. a customer\n        profile is created for every res.partner/payment.token couple).\n\n        Note that this function makes 2 calls to the authorize api, since we need to\n        obtain a partial card number to generate a meaningful payment.token name.\n\n        :param record partner: the res.partner record of the customer\n        :param str transaction_id: id of the authorized transaction in the\n                                   Authorize.net backend\n\n        :return: a dict containing the profile_id and payment_profile_id of the\n                 newly created customer profile and payment profile as well as the\n                 last digits of the card number\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createCustomerProfileFromTransactionRequest', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='transId', kind=None),
                                            Constant(value='customer', kind=None),
                                        ],
                                        values=[
                                            Name(id='transaction_id', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='merchantCustomerId', kind=None),
                                                    Constant(value='email', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=BinOp(
                                                            left=Constant(value='ODOO-%s-%s', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Call(
                                                                                func=Name(id='uuid4', ctx=Load()),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='hex',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=Constant(value=8, kind=None),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=20, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='customerProfileId', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Unable to create customer payment profile, data missing from transaction. Transaction_id: %s - Partner_id: %s', kind=None),
                                            Name(id='transaction_id', ctx=Load()),
                                            Name(id='partner', ctx=Load()),
                                        ],
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='profile_id', kind=None),
                                    Constant(value='payment_profile_id', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='customerProfileId', kind=None)],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='customerPaymentProfileIdList', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='getCustomerPaymentProfileRequest', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='customerProfileId', kind=None),
                                            Constant(value='customerPaymentProfileId', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='profile_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='payment_profile_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='paymentProfile', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='payment', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='payment_method_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='credit_card', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='payment', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='creditCard', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='cardNumber', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='payment', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='bankAccount', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='accountNumber', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                    name='delete_customer_profile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='profile_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Delete a customer profile\n\n        :param str profile_id: the id of the customer profile in the Authorize.net backend\n\n        :return: a dict containing the response code\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='deleteCustomerProfileRequest', kind=None),
                                    Dict(
                                        keys=[Constant(value='customerProfileId', kind=None)],
                                        values=[Name(id='profile_id', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='deleteCustomerProfile', kind=None),
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
                    name='_prepare_authorization_transaction_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='transaction_type', annotation=None, type_comment=None),
                            arg(arg='tx_data', annotation=None, type_comment=None),
                            arg(arg='tx', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='bill_to', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='profile', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='tx_data', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='split_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='payment_utils', ctx=Load()),
                                            attr='split_partner_name',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tx', ctx=Load()),
                                                attr='partner_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bill_to', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='billTo', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='firstName', kind=None),
                                                    Constant(value='lastName', kind=None),
                                                    Constant(value='company', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='city', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='zip', kind=None),
                                                    Constant(value='country', kind=None),
                                                ],
                                                values=[
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='is_company',
                                                            ctx=Load(),
                                                        ),
                                                        body=Constant(value='', kind=None),
                                                        orelse=Subscript(
                                                            value=Name(id='split_name', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='split_name', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='is_company',
                                                            ctx=Load(),
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='tx', ctx=Load()),
                                                            attr='partner_name',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value='', kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='partner_address',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='partner_city',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='tx', ctx=Load()),
                                                                    attr='partner_state_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='partner_zip',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='tx', ctx=Load()),
                                                                    attr='partner_country_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='transactionRequest', kind=None)],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='transactionType', kind=None),
                                            Constant(value='amount', kind=None),
                                            None,
                                            Constant(value='order', kind=None),
                                            Constant(value='customer', kind=None),
                                            None,
                                            Constant(value='customerIP', kind=None),
                                        ],
                                        values=[
                                            Name(id='transaction_type', ctx=Load()),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='tx_data', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='invoiceNumber', kind=None),
                                                    Constant(value='description', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tx', ctx=Load()),
                                                            attr='reference',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=20, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tx', ctx=Load()),
                                                            attr='reference',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=255, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='email', kind=None)],
                                                values=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='tx', ctx=Load()),
                                                                attr='partner_email',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Name(id='bill_to', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='payment_utils', ctx=Load()),
                                                    attr='get_customer_ip_address',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                    name='authorize',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tx', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='opaque_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Authorize (without capture) a payment for the given amount.\n\n        :param recordset tx: The transaction of the payment, as a `payment.transaction` record\n        :param recordset token: The token of the payment method to charge, as a `payment.token`\n                                record\n        :param dict opaque_data: The payment details obfuscated by Authorize.Net\n        :return: a dict containing the response code, transaction id and transaction type\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_tx_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='token',
                                        value=Name(id='token', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='opaque_data',
                                        value=Name(id='opaque_data', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createTransactionRequest', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_authorization_transaction_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='authOnlyTransaction', kind=None),
                                            Name(id='tx_data', ctx=Load()),
                                            Name(id='tx', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='auth_only', kind=None),
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
                    name='auth_and_capture',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tx', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='opaque_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Authorize and capture a payment for the given amount.\n\n        Authorize and immediately capture a payment for the given payment.token\n        record for the specified amount with reference as communication.\n\n        :param recordset tx: The transaction of the payment, as a `payment.transaction` record\n        :param record token: the payment.token record that must be charged\n        :param str opaque_data: the transaction opaque_data obtained from Authorize.net\n\n        :return: a dict containing the response code, transaction id and transaction type\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_tx_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='token',
                                        value=Name(id='token', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='opaque_data',
                                        value=Name(id='opaque_data', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createTransactionRequest', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_authorization_transaction_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='authCaptureTransaction', kind=None),
                                            Name(id='tx_data', ctx=Load()),
                                            Name(id='tx', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='auth_capture', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='transactionResponse', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='errors', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='errors', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='x_response_reason_text', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='errorText', kind=None)],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='e', ctx=Store()),
                                                        iter=Name(id='errors', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_tx_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='opaque_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param token: The token of the payment method to charge, as a `payment.token` record\n        :param dict opaque_data: The payment details obfuscated by Authorize.Net\n        ', kind=None),
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='token', ctx=Load()),
                                            Name(id='opaque_data', ctx=Load()),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='token', ctx=Load()),
                                                Name(id='opaque_data', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Exactly one of token or opaque_data must be specified', kind=None),
                        ),
                        If(
                            test=Name(id='token', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='token', ctx=Load()),
                                            attr='ensure_one',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='profile', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='customerProfileId', kind=None),
                                                    Constant(value='paymentProfile', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='authorize_profile',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='paymentProfileId', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='acquirer_ref',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='payment', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[Constant(value='opaqueData', kind=None)],
                                                values=[Name(id='opaque_data', ctx=Load())],
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
                    name='_get_transaction_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='transaction_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return detailed information about a specific transaction. Useful to issue refunds.\n\n        :param str transaction_id: transaction id\n        :return: a dict containing the transaction details\n        :rtype: dict\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='getTransactionDetailsRequest', kind=None),
                                    Dict(
                                        keys=[Constant(value='transId', kind=None)],
                                        values=[Name(id='transaction_id', ctx=Load())],
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
                    name='capture',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='transaction_id', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Capture a previously authorized payment for the given amount.\n\n        Capture a previsouly authorized payment. Note that the amount is required\n        even though we do not support partial capture.\n\n        :param str transaction_id: id of the authorized transaction in the\n                                   Authorize.net backend\n        :param str amount: transaction amount (up to 15 digits with decimal point)\n\n        :return: a dict containing the response code, transaction id and transaction type\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createTransactionRequest', kind=None),
                                    Dict(
                                        keys=[Constant(value='transactionRequest', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='transactionType', kind=None),
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='refTransId', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='priorAuthCaptureTransaction', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='amount', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='transaction_id', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='prior_auth_capture', kind=None),
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
                    name='void',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='transaction_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Void a previously authorized payment.\n\n        :param str transaction_id: the id of the authorized transaction in the\n                                   Authorize.net backend\n        :return: a dict containing the response code, transaction id and transaction type\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createTransactionRequest', kind=None),
                                    Dict(
                                        keys=[Constant(value='transactionRequest', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='transactionType', kind=None),
                                                    Constant(value='refTransId', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='voidTransaction', kind=None),
                                                    Name(id='transaction_id', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='void', kind=None),
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
                    name='refund',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='transaction_id', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Refund a previously authorized payment. If the transaction is not settled\n            yet, it will be voided.\n\n        :param str transaction_id: the id of the authorized transaction in the\n                                   Authorize.net backend\n        :param float amount: transaction amount to refund\n        :return: a dict containing the response code, transaction id and transaction type\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tx_details', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_transaction_details',
                                    ctx=Load(),
                                ),
                                args=[Name(id='transaction_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='tx_details', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tx_details', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='err_code', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='x_response_code', kind=None),
                                            Constant(value='x_response_reason_text', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='AUTH_ERROR_STATUS',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tx_details', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='err_msg', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='tx_details', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='transaction', kind=None),
                                                Dict(keys=[], values=[]),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='transactionStatus', kind=None)],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='authorizedPendingCapture', kind=None),
                                            Constant(value='capturedPendingSettlement', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='void',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='transaction_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='card', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tx_details', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='transaction', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='payment', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='creditCard', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='cardNumber', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createTransactionRequest', kind=None),
                                    Dict(
                                        keys=[Constant(value='transactionRequest', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='transactionType', kind=None),
                                                    Constant(value='amount', kind=None),
                                                    Constant(value='payment', kind=None),
                                                    Constant(value='refTransId', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='refundTransaction', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='amount', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='creditCard', kind=None)],
                                                        values=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='cardNumber', kind=None),
                                                                    Constant(value='expirationDate', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='card', ctx=Load()),
                                                                    Constant(value='XXXX', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='transaction_id', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_format_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='refund', kind=None),
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
                    name='merchant_details',
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
                            value=Constant(value=' Retrieves the merchant details and generate a new public client key if none exists.\n\n        :return: Dictionary containing the merchant details\n        :rtype: dict', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='getMerchantDetailsRequest', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_authenticate',
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
                            value=Constant(value=' Test Authorize.net communication with a simple credentials check.\n\n        :return: The authentication results\n        :rtype: dict\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='authenticateTestRequest', kind=None)],
                                keywords=[],
                            ),
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
