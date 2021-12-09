Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
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
        Assign(
            targets=[Name(id='logger', ctx=Store())],
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
            name='Http',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='session_info',
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
                            targets=[Name(id='session_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_public_key_to_session_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='session_info', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_frontend_session_info',
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
                            targets=[Name(id='frontend_session_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_frontend_session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_public_key_to_session_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='frontend_session_info', ctx=Load())],
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
                    name='_add_public_key_to_session_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Add the ReCaptcha public key to the given session_info object', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='public_key', ctx=Store())],
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
                                args=[Constant(value='recaptcha_public_key', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='public_key', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='session_info', ctx=Load()),
                                            slice=Constant(value='recaptcha_public_key', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='public_key', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
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
                    name='_verify_request_recaptcha_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Verify the recaptcha token for the current request.\n            If no recaptcha private key is set the recaptcha verification\n            is considered inactive and this method will return True.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ip_addr', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='remote_addr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='recaptcha_token_response', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recaptcha_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_verify_recaptcha_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ip_addr', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                    Name(id='action', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='recaptcha_result', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='is_human', kind=None),
                                            Constant(value='no_secret', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='recaptcha_result', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='wrong_secret', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The reCaptcha private key is invalid.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='recaptcha_result', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='wrong_token', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The reCaptcha token is invalid.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='recaptcha_result', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='timeout', kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Your request has timed out, please retry.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='recaptcha_result', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='bad_request', kind=None)],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The request is invalid or malformed.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Return(
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
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
                    name='_verify_recaptcha_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ip_addr', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Verify a recaptchaV3 token and returns the result as a string.\n            RecaptchaV3 verify DOC: https://developers.google.com/recaptcha/docs/verify\n\n            :return: The result of the call to the google API:\n                     is_human: The token is valid and the user trustworthy.\n                     is_bot: The user is not trustworthy and most likely a bot.\n                     no_secret: No reCaptcha secret set in settings.\n                     wrong_action: the action performed to obtain the token does not match the one we are verifying.\n                     wrong_token: The token provided is invalid or empty.\n                     wrong_secret: The private key provided in settings is invalid.\n                     timeout: The request has timout or the token provided is too old.\n                     bad_request: The request is invalid or malformed.\n            :rtype: str\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='private_key', ctx=Store())],
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
                                args=[Constant(value='recaptcha_private_key', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='private_key', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='no_secret', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='min_score', ctx=Store())],
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
                                args=[Constant(value='recaptcha_min_score', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='post',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='https://www.recaptcha.net/recaptcha/api/siteverify', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='secret', kind=None),
                                                    Constant(value='response', kind=None),
                                                    Constant(value='remoteip', kind=None),
                                                ],
                                                values=[
                                                    Name(id='private_key', ctx=Load()),
                                                    Name(id='token', ctx=Load()),
                                                    Name(id='ip_addr', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res_success', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='success', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res_action', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='res_success', ctx=Load()),
                                            Name(id='action', ctx=Load()),
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='action', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='Timeout',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Trial captcha verification timeout for ip address %s', kind=None),
                                                    Name(id='ip_addr', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='timeout', kind=None),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Trial captcha verification bad request response', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='bad_request', kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Name(id='res_success', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='score', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='score', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='score', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[Name(id='min_score', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Trial captcha verification for ip address %s failed with score %f.', kind=None),
                                                    Name(id='ip_addr', ctx=Load()),
                                                    Name(id='score', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='is_bot', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='res_action', ctx=Load()),
                                            Compare(
                                                left=Name(id='res_action', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='action', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Trial captcha verification for ip address %s failed with action %f, expected: %s.', kind=None),
                                                    Name(id='ip_addr', ctx=Load()),
                                                    Name(id='score', ctx=Load()),
                                                    Name(id='action', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='wrong_action', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Trial captcha verification for ip address %s succeeded with score %f.', kind=None),
                                            Name(id='ip_addr', ctx=Load()),
                                            Name(id='score', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='is_human', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='error-codes', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Trial captcha verification for ip address %s failed error codes %r. token was: [%s]', kind=None),
                                    Name(id='ip_addr', ctx=Load()),
                                    Name(id='errors', ctx=Load()),
                                    Name(id='token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='error', ctx=Store()),
                            iter=Name(id='errors', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='error', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='missing-input-secret', kind=None),
                                                    Constant(value='invalid-input-secret', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='wrong_secret', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='missing-input-response', kind=None),
                                                    Constant(value='invalid-input-response', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='wrong_token', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='timeout-or-duplicate', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='timeout', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='bad-request', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='bad_request', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value='is_bot', kind=None),
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
