Module(
    body=[
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.utils', asname=None)],
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='BadRequest', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='http', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='registry', asname='registry_get')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.auth_signup.controllers.main',
            names=[alias(name='AuthSignupHome', asname='Home')],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web.controllers.main',
            names=[
                alias(name='db_monodb', asname=None),
                alias(name='ensure_db', asname=None),
                alias(name='set_cookie_and_redirect', asname=None),
                alias(name='login_and_redirect', asname=None),
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
        FunctionDef(
            name='fragment_to_query_string',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='func', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='wrapper',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='a', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='debug', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='kw', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value="<html><head><script>\n                var l = window.location;\n                var q = l.hash.substring(1);\n                var r = l.pathname + l.search;\n                if(q.length !== 0) {\n                    var s = l.search ? (l.search === '?' ? '' : '&') : '?';\n                    r = l.pathname + l.search + s + q;\n                }\n                if (r == l.pathname) {\n                    r = '/';\n                }\n                window.location = r;\n            </script></head><body></body></html>", kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='func', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Starred(
                                        value=Name(id='a', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='functools', ctx=Load()),
                                attr='wraps',
                                ctx=Load(),
                            ),
                            args=[Name(id='func', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapper', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='OAuthLogin',
            bases=[Name(id='Home', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='list_providers',
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
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='providers', ctx=Store())],
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
                                                        slice=Constant(value='auth.oauth.provider', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='enabled', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
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
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='providers', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        For(
                            target=Name(id='provider', ctx=Store()),
                            iter=Name(id='providers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='return_url', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='url_root',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value='auth_oauth/signin', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_state',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='provider', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='response_type',
                                                value=Constant(value='token', kind=None),
                                            ),
                                            keyword(
                                                arg='client_id',
                                                value=Subscript(
                                                    value=Name(id='provider', ctx=Load()),
                                                    slice=Constant(value='client_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='redirect_uri',
                                                value=Name(id='return_url', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='scope',
                                                value=Subscript(
                                                    value=Name(id='provider', ctx=Load()),
                                                    slice=Constant(value='scope', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='state',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='state', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='provider', ctx=Load()),
                                            slice=Constant(value='auth_link', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s?%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='provider', ctx=Load()),
                                                    slice=Constant(value='auth_endpoint', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='urls',
                                                            ctx=Load(),
                                                        ),
                                                        attr='url_encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='params', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='providers', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_state',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='provider', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='redirect', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='redirect', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='web', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='redirect', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Tuple(
                                            elts=[
                                                Constant(value='//', kind=None),
                                                Constant(value='http://', kind=None),
                                                Constant(value='https://', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='redirect', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='url_root',
                                                    ctx=Load(),
                                                ),
                                                IfExp(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='redirect', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='/', kind=None)],
                                                    ),
                                                    body=Subscript(
                                                        value=Name(id='redirect', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=1, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    orelse=Name(id='redirect', ctx=Load()),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='d',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='db',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='p',
                                        value=Subscript(
                                            value=Name(id='provider', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='r',
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='urls',
                                                    ctx=Load(),
                                                ),
                                                attr='url_quote_plus',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='redirect', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='token', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='state', ctx=Load()),
                                            slice=Constant(value='t', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='token', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='state', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='web_login',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='ensure_db', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='GET', kind=None)],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='redirect', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='params',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='redirect', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='providers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='list_providers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='OAuthLogin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='web_login',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='response', ctx=Load()),
                                attr='is_qweb',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='error', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='oauth_error', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='error', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='1', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Sign up is not allowed on this database.', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='2', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='error', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Access Denied', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='error', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='3', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='error', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='You do not have access to this database or your invitation has expired. Please ask for an invitation and be sure to follow the link in your invitation email.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='error', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='qcontext',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='providers', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='providers', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='error', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='response', ctx=Load()),
                                                        attr='qcontext',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='error', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='error', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_auth_signup_qcontext',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='OAuthLogin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_auth_signup_qcontext',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='providers', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='list_providers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='OAuthController',
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
                    name='signin',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='kw', ctx=Load()),
                                        slice=Constant(value='state', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=Subscript(
                                value=Name(id='state', ctx=Load()),
                                slice=Constant(value='d', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='db_filter',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[Name(id='dbname', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='provider', ctx=Store())],
                            value=Subscript(
                                value=Name(id='state', ctx=Load()),
                                slice=Constant(value='p', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='state', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='c', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Name(id='registry_get', ctx=Load()),
                                args=[Name(id='dbname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
                                                    attr='Environment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='SUPERUSER_ID', ctx=Load()),
                                                    Name(id='context', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='credentials', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.users', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='auth_oauth',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='provider', ctx=Load()),
                                                    Name(id='kw', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='commit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='action', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='state', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='a', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='menu', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='state', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='m', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='redirect', ctx=Store())],
                                            value=IfExp(
                                                test=Call(
                                                    func=Attribute(
                                                        value=Name(id='state', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='r', kind=None)],
                                                    keywords=[],
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='urls',
                                                            ctx=Load(),
                                                        ),
                                                        attr='url_unquote_plus',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='state', ctx=Load()),
                                                            slice=Constant(value='r', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=Constant(value='/web', kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='redirect', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Name(id='redirect', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='action', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='url', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='/web#action=%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='action', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Name(id='menu', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='url', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Constant(value='/web#menu_id=%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='menu', ctx=Load()),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='resp', ctx=Store())],
                                            value=Call(
                                                func=Name(id='login_and_redirect', ctx=Load()),
                                                args=[
                                                    Starred(
                                                        value=Name(id='credentials', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='redirect_url',
                                                        value=Name(id='url', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='werkzeug', ctx=Load()),
                                                                        attr='urls',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='url_parse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='resp', ctx=Load()),
                                                                        attr='location',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='/web', kind=None)],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='has_group',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='base.group_user', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='resp', ctx=Load()),
                                                            attr='location',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='/', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Name(id='resp', ctx=Load()),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AttributeError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='auth_signup not installed on database %s: oauth sign up cancelled.', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[Name(id='dbname', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Constant(value='/web/login?oauth_error=1', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='AccessDenied', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='OAuth2: access denied, redirect to main page in case a valid session exists, without setting cookies', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Constant(value='/web/login?oauth_error=3', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='redirect', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='url', ctx=Load()),
                                                            Constant(value=303, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='redirect', ctx=Load()),
                                                            attr='autocorrect_location_header',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Name(id='redirect', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='OAuth2: %s', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Constant(value='/web/login?oauth_error=2', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='set_cookie_and_redirect', ctx=Load()),
                                args=[Name(id='url', ctx=Load())],
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
                            args=[Constant(value='/auth_oauth/signin', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                            ],
                        ),
                        Name(id='fragment_to_query_string', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='oea',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='login user via Odoo Account provider', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='db', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dbname', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dbname', ctx=Store())],
                                    value=Call(
                                        func=Name(id='db_monodb', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dbname', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='db_filter',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[Name(id='dbname', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Name(id='registry_get', ctx=Load()),
                                args=[Name(id='dbname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
                                                    attr='Environment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='SUPERUSER_ID', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='provider', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='env', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='auth_oauth.provider_openerp', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='set_cookie_and_redirect', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='/web?db=%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='dbname', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='provider', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='auth.oauth.provider', kind=None)],
                                    ),
                                    msg=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='d', kind=None),
                                    Constant(value='p', kind=None),
                                    Constant(value='c', kind=None),
                                ],
                                values=[
                                    Name(id='dbname', ctx=Load()),
                                    Attribute(
                                        value=Name(id='provider', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='no_user_creation', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kw', ctx=Load()),
                                    slice=Constant(value='state', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='state', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='signin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
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
                            args=[Constant(value='/auth_oauth/oea', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
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
