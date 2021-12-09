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
            name='SipsController',
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
                    value=Constant(value='/payment/sips/dpn/', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_notify_url', ctx=Store())],
                    value=Constant(value='/payment/sips/ipn/', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='sips_dpn',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Process the data returned by SIPS after redirection.\n\n        The route is flagged with `save_session=False` to prevent Odoo from assigning a new session\n        to the user if they are redirected to this route with a POST request. Indeed, as the session\n        cookie is created without a `SameSite` attribute, some browsers that don't implement the\n        recommended default `SameSite=Lax` behavior will not include the cookie in the redirection\n        request from the payment provider to Odoo. As the redirection to the '/payment/status' page\n        will satisfy any specification of the `SameSite` attribute, the session of the user will be\n        retrieved and with it the transaction which will be immediately post-processed.\n\n        :param dict post: The feedback data to process\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='beginning Sips DPN _handle_feedback_data with data %s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='post', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sips_validate_data',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='post', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                                    Constant(value='sips', kind=None),
                                                    Name(id='post', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
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
                                        elts=[Constant(value='POST', kind=None)],
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
                    name='sips_ipn',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Sips IPN. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='beginning Sips IPN _handle_feedback_data with data %s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='post', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='post', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='received empty notification; skip.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sips_validate_data',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='post', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                                            Constant(value='sips', kind=None),
                                                            Name(id='post', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValidationError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
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
                FunctionDef(
                    name='_sips_validate_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='post', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
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
                                    Constant(value='sips', kind=None),
                                    Name(id='post', ctx=Load()),
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
                            targets=[Name(id='security', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='acquirer_sudo', ctx=Load()),
                                    attr='_sips_generate_shasign',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='post', ctx=Load()),
                                        slice=Constant(value='Data', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='security', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Subscript(
                                        value=Name(id='post', ctx=Load()),
                                        slice=Constant(value='Seal', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='validated data', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data are tampered', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
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
