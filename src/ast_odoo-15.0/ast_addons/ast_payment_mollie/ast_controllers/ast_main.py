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
            names=[alias(name='http', asname=None)],
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
            name='MollieController',
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
                    value=Constant(value='/payment/mollie/return', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_notify_url', ctx=Store())],
                    value=Constant(value='/payment/mollie/notify', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='mollie_return',
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
                            value=Constant(value=" Process the data returned by Mollie after redirection.\n\n        The route is flagged with `save_session=False` to prevent Odoo from assigning a new session\n        to the user if they are redirected to this route with a POST request. Indeed, as the session\n        cookie is created without a `SameSite` attribute, some browsers that don't implement the\n        recommended default `SameSite=Lax` behavior will not include the cookie in the redirection\n        request from the payment provider to Odoo. As the redirection to the '/payment/status' page\n        will satisfy any specification of the `SameSite` attribute, the session of the user will be\n        retrieved and with it the transaction which will be immediately post-processed.\n\n        :param dict data: The feedback data (only `id`) and the transaction reference (`ref`)\n                          embedded in the return URL\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Received Mollie return data:\n%s', kind=None),
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
                                    Constant(value='mollie', kind=None),
                                    Name(id='data', ctx=Load()),
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
                    name='mollie_notify',
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
                            value=Constant(value=' Process the data sent by Mollie to the webhook.\n\n        :param dict data: The feedback data (only `id`) and the transaction reference (`ref`)\n                          embedded in the return URL\n        :return: An empty string to acknowledge the notification\n        :rtype: str\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Received Mollie notify data:\n%s', kind=None),
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
                                            Constant(value='mollie', kind=None),
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
                                        elts=[Constant(value='POST', kind=None)],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
