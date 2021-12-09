Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
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
        Assign(
            targets=[Name(id='TIMEOUT', ctx=Store())],
            value=Constant(value=20, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GOOGLE_AUTH_ENDPOINT', ctx=Store())],
            value=Constant(value='https://accounts.google.com/o/oauth2/auth', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GOOGLE_TOKEN_ENDPOINT', ctx=Store())],
            value=Constant(value='https://accounts.google.com/o/oauth2/token', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GOOGLE_API_BASE_URL', ctx=Store())],
            value=Constant(value='https://www.googleapis.com', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='GoogleService',
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
                    value=Constant(value='google.service', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Google Service', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_refresh_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                            arg(arg='authorization_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Call Google API to refresh the token, with the given authorization code\n            :param service : the name of the google service to actualize\n            :param authorization_code : the code to exchange against the new refresh token\n            :returns the new refresh token\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Parameters', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Parameters', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='google_%s_client_id', kind=None),
                                        op=Mod(),
                                        right=Name(id='service', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_secret', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Parameters', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='google_%s_client_secret', kind=None),
                                        op=Mod(),
                                        right=Name(id='service', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='redirect_uri', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Parameters', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='google_redirect_uri', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Content-type', kind=None)],
                                values=[Constant(value='application/x-www-form-urlencoded', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='code', kind=None),
                                    Constant(value='client_id', kind=None),
                                    Constant(value='client_secret', kind=None),
                                    Constant(value='redirect_uri', kind=None),
                                    Constant(value='grant_type', kind=None),
                                ],
                                values=[
                                    Name(id='authorization_code', ctx=Load()),
                                    Name(id='client_id', ctx=Load()),
                                    Name(id='client_secret', ctx=Load()),
                                    Name(id='redirect_uri', ctx=Load()),
                                    Constant(value='authorization_code', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='req', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='post',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='GOOGLE_TOKEN_ENDPOINT', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Name(id='data', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Name(id='headers', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='req', ctx=Load()),
                                            attr='raise_for_status',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='req', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Something went wrong during your token generation. Maybe your Authorization Code is invalid or already expired', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.config.settings', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_config_warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error_msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='content', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='refresh_token', kind=None)],
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
                    name='_get_google_token_uri',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                            arg(arg='scope', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='encoded_params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urls', ctx=Load()),
                                    attr='url_encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='scope', kind=None),
                                            Constant(value='redirect_uri', kind=None),
                                            Constant(value='client_id', kind=None),
                                            Constant(value='response_type', kind=None),
                                        ],
                                        values=[
                                            Name(id='scope', ctx=Load()),
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[Constant(value='google_redirect_uri', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='google_%s_client_id', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='service', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='code', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s?%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='GOOGLE_AUTH_ENDPOINT', ctx=Load()),
                                        Name(id='encoded_params', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
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
                    name='_get_authorize_uri',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_url', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                            arg(arg='scope', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method return the url needed to allow this instance of Odoo to access to the scope\n            of gmail specified as parameters\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='d', kind=None),
                                    Constant(value='s', kind=None),
                                    Constant(value='f', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                    Name(id='service', ctx=Load()),
                                    Name(id='from_url', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='web.base.url', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='http://www.odoo.com?NoBaseUrl', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_id', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='google_%s_client_id', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='service', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='encoded_params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urls', ctx=Load()),
                                    attr='url_encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='response_type', kind=None),
                                            Constant(value='client_id', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='scope', kind=None),
                                            Constant(value='redirect_uri', kind=None),
                                            Constant(value='approval_prompt', kind=None),
                                            Constant(value='access_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='code', kind=None),
                                            Name(id='client_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='state', ctx=Load())],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='scope', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='%s/auth/%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='GOOGLE_API_BASE_URL', ctx=Load()),
                                                                Name(id='service', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            BinOp(
                                                left=Name(id='base_url', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value='/google_account/authentication', kind=None),
                                            ),
                                            Constant(value='force', kind=None),
                                            Constant(value='offline', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s?%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='GOOGLE_AUTH_ENDPOINT', ctx=Load()),
                                        Name(id='encoded_params', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
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
                    name='_get_google_tokens',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='authorize_code', annotation=None, type_comment=None),
                            arg(arg='service', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Call Google API to exchange authorization code against token, with POST request, to\n            not be redirected.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[Constant(value='web.base.url', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='http://www.odoo.com?NoBaseUrl', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_id', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='google_%s_client_id', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='service', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client_secret', ctx=Store())],
                            value=Call(
                                func=Name(id='get_param', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='google_%s_client_secret', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='service', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='content-type', kind=None)],
                                values=[Constant(value='application/x-www-form-urlencoded', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='code', kind=None),
                                    Constant(value='client_id', kind=None),
                                    Constant(value='client_secret', kind=None),
                                    Constant(value='grant_type', kind=None),
                                    Constant(value='redirect_uri', kind=None),
                                ],
                                values=[
                                    Name(id='authorize_code', ctx=Load()),
                                    Name(id='client_id', ctx=Load()),
                                    Name(id='client_secret', ctx=Load()),
                                    Constant(value='authorization_code', kind=None),
                                    BinOp(
                                        left=Name(id='base_url', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value='/google_account/authentication', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='dummy', ctx=Store()),
                                                Name(id='response', ctx=Store()),
                                                Name(id='dummy', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_do_request',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='GOOGLE_TOKEN_ENDPOINT', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='params',
                                                value=Name(id='data', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Name(id='headers', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='method',
                                                value=Constant(value='POST', kind=None),
                                            ),
                                            keyword(
                                                arg='preuri',
                                                value=Constant(value='', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='access_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='access_token', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='refresh_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='refresh_token', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ttl', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='expires_in', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='access_token', ctx=Load()),
                                            Name(id='refresh_token', ctx=Load()),
                                            Name(id='ttl', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='requests', ctx=Load()),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Something went wrong during your token generation. Maybe your Authorization Code is invalid', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.config.settings', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_config_warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error_msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
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
                    name='_do_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uri', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
                            arg(arg='preuri', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='POST', kind=None),
                            Constant(value='https://www.googleapis.com', kind=None),
                            Name(id='TIMEOUT', ctx=Load()),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Execute the request to Google API. Return a tuple ('HTTP_CODE', 'HTTP_RESPONSE')\n            :param uri : the url to contact\n            :param params : dict or already encoded parameters for the request to make\n            :param headers : headers of request\n            :param method : the method to use to make the request\n            :param preuri : pre url to prepend to param uri.\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='params', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='headers', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='headers', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Uri: %s - Type : %s - Headers: %s - Params : %s !', kind=None),
                                    Name(id='uri', ctx=Load()),
                                    Name(id='method', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ask_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='method', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='GET', kind=None),
                                                    Constant(value='DELETE', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='method', ctx=Load()),
                                                            attr='lower',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Name(id='preuri', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='uri', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='params',
                                                        value=Name(id='params', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='timeout',
                                                        value=Name(id='timeout', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='method', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='POST', kind=None),
                                                            Constant(value='PATCH', kind=None),
                                                            Constant(value='PUT', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='requests', ctx=Load()),
                                                            attr='request',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='method', ctx=Load()),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            BinOp(
                                                                left=Name(id='preuri', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='uri', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='data',
                                                                value=Name(id='params', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='headers',
                                                                value=Name(id='headers', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='timeout',
                                                                value=Name(id='timeout', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='Exception', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Method not supported [%s] not in [GET, POST, PUT, PATCH or DELETE]!', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Name(id='method', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='raise_for_status',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='status', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='res', ctx=Load()),
                                        attr='status_code',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[Name(id='status', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=204, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='json',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='ask_time', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='res', ctx=Load()),
                                                                attr='headers',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='%a, %d %b %Y %H:%M:%S %Z', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='requests', ctx=Load()),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                    name='error',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='error', ctx=Load()),
                                                        attr='response',
                                                        ctx=Load(),
                                                    ),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=204, kind=None),
                                                            Constant(value=404, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='status', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='error', ctx=Load()),
                                                            attr='response',
                                                            ctx=Load(),
                                                        ),
                                                        attr='status_code',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='response', ctx=Store())],
                                                    value=Constant(value='', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Bad google request : %s !', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='error', ctx=Load()),
                                                                    attr='response',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='content',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Name(id='error', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='status', ctx=Load()),
                                    Name(id='response', ctx=Load()),
                                    Name(id='ask_time', ctx=Load()),
                                ],
                                ctx=Load(),
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
