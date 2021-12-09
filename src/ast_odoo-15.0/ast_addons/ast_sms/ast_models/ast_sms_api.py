Module(
    body=[
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
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='DEFAULT_ENDPOINT', ctx=Store())],
            value=Constant(value='https://iap-sms.odoo.com', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='SmsApi',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='sms.api', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='SMS API', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_contact_iap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_endpoint', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='sms', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='params', ctx=Load()),
                                    slice=Constant(value='account_token', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='account', ctx=Load()),
                                attr='account_token',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sms.endpoint', kind=None),
                                    Name(id='DEFAULT_ENDPOINT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iap_tools', ctx=Load()),
                                    attr='iap_jsonrpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='endpoint', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='local_endpoint', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='params', ctx=Load()),
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
                FunctionDef(
                    name='_send_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='numbers', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Send a single message to several numbers\n\n        :param numbers: list of E164 formatted phone numbers\n        :param message: content to send\n\n        :raises ? TDE FIXME\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='numbers', kind=None),
                                    Constant(value='message', kind=None),
                                ],
                                values=[
                                    Name(id='numbers', ctx=Load()),
                                    Name(id='message', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_contact_iap',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/iap/message_send', kind=None),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
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
                    name='_send_sms_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='messages', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Send SMS using IAP in batch mode\n\n        :param messages: list of SMS to send, structured as dict [{\n            'res_id':  integer: ID of sms.sms,\n            'number':  string: E164 formatted phone number,\n            'content': string: content to send\n        }]\n\n        :return: return of /iap/sms/1/send controller which is a list of dict [{\n            'res_id': integer: ID of sms.sms,\n            'state':  string: 'insufficient_credit' or 'wrong_number_format' or 'success',\n            'credit': integer: number of credits spent to send this SMS,\n        }]\n\n        :raises: normally none\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='messages', kind=None)],
                                values=[Name(id='messages', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_contact_iap',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/iap/sms/2/send', kind=None),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
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
                    name='_get_sms_api_error_messages',
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
                            value=Constant(value=" Returns a dict containing the error message to display for every known error 'state'\n        resulting from the '_send_sms_batch' method.\n        We prefer a dict instead of a message-per-error-state based method so we only call\n        the 'get_credits_url' once, to avoid extra RPC calls. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='buy_credits_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_credits_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='service_name',
                                        value=Constant(value='sms', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='buy_credits', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<a href="%s" target="_blank">%s</a>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='buy_credits_url', ctx=Load()),
                                        Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Buy credits.', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='unregistered', kind=None),
                                    Constant(value='insufficient_credit', kind=None),
                                    Constant(value='wrong_number_format', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="You don't have an eligible IAP account.", kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="You don't have enough credits on your IAP account.", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='buy_credits', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="The number you're trying to reach is not correctly formatted.", kind=None)],
                                        keywords=[],
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
