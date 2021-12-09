Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.addons.web.controllers.main', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
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
        Assign(
            targets=[Name(id='TRUSTED_DEVICE_COOKIE', ctx=Store())],
            value=Constant(value='td_id', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TRUSTED_DEVICE_AGE', ctx=Store())],
            value=BinOp(
                left=Constant(value=90, kind=None),
                op=Mult(),
                right=Constant(value=86400, kind=None),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Home',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='addons',
                                    ctx=Load(),
                                ),
                                attr='web',
                                ctx=Load(),
                            ),
                            attr='controllers',
                            ctx=Load(),
                        ),
                        attr='main',
                        ctx=Load(),
                    ),
                    attr='Home',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='web_totp',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='redirect', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
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
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_login_redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='redirect',
                                                        value=Name(id='redirect', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='pre_uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/web/login', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='pre_uid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='user', ctx=Load()),
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
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cookies', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='cookies',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cookies', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TRUSTED_DEVICE_COOKIE', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='key', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='checked_credentials', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='auth_totp.device', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_check_credentials',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='scope',
                                                        value=Constant(value='browser', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='key',
                                                        value=Name(id='key', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='checked_credentials', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='finalize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_login_redirect',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='session',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uid',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='redirect',
                                                                        value=Name(id='redirect', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='user', ctx=Load()),
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
                                                comparators=[Constant(value='POST', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='_assert_can_auth',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=None,
                                                        ),
                                                    ],
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='_totp_check',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='re', ctx=Load()),
                                                                                    attr='sub',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Constant(value='\\s', kind=None),
                                                                                    Constant(value='', kind=None),
                                                                                    Subscript(
                                                                                        value=Name(id='kwargs', ctx=Load()),
                                                                                        slice=Constant(value='totp_token', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AccessDenied', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='error', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Verification failed, please double-check the 6-digit code', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                ExceptHandler(
                                                    type=Name(id='ValueError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='error', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Invalid authentication code format.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='finalize',
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
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_login_redirect',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='session',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uid',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='redirect',
                                                                        value=Name(id='redirect', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='kwargs', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='remember', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='name', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='%(browser)s on %(platform)s', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='browser',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='request', ctx=Load()),
                                                                                            attr='httprequest',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='user_agent',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='browser',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='capitalize',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='platform',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='request', ctx=Load()),
                                                                                            attr='httprequest',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='user_agent',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='platform',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='capitalize',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='geoip', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='session',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='geoip',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='geoip', ctx=Load()),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='name', ctx=Store()),
                                                                    op=Add(),
                                                                    value=BinOp(
                                                                        left=Constant(value=' (%s, %s)', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Subscript(
                                                                                    value=Name(id='geoip', ctx=Load()),
                                                                                    slice=Constant(value='city', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Subscript(
                                                                                    value=Name(id='geoip', ctx=Load()),
                                                                                    slice=Constant(value='country_name', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='key', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='auth_totp.device', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_generate',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='browser', kind=None),
                                                                    Name(id='name', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='response', ctx=Load()),
                                                                    attr='set_cookie',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='key',
                                                                        value=Name(id='TRUSTED_DEVICE_COOKIE', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='value',
                                                                        value=Name(id='key', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='max_age',
                                                                        value=Name(id='TRUSTED_DEVICE_AGE', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='httponly',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='samesite',
                                                                        value=Constant(value='Lax', kind=None),
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
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='auth_totp.auth_totp_form', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='redirect', kind=None),
                                        ],
                                        values=[
                                            Name(id='error', ctx=Load()),
                                            Name(id='redirect', ctx=Load()),
                                        ],
                                    ),
                                ],
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
                            args=[Constant(value='/web/login/totp', kind=None)],
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
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
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
