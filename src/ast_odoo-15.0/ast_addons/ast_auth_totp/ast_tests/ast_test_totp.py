Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='xmlrpc.client',
            names=[alias(name='Fault', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='passlib.totp',
            names=[alias(name='TOTP', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.service',
            names=[
                alias(name='common', asname='auth'),
                alias(name='model', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='tagged', asname=None),
                alias(name='HttpCase', asname=None),
                alias(name='get_db_name', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='controllers.home',
            names=[alias(name='Home', asname=None)],
            level=2,
        ),
        ClassDef(
            name='TestTOTP',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='totp', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='totp_hook',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='secret', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Nonlocal(names=['totp']),
                                If(
                                    test=Compare(
                                        left=Name(id='totp', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='totp', ctx=Store())],
                                            value=Call(
                                                func=Name(id='TOTP', ctx=Load()),
                                                args=[Name(id='secret', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='secret', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='totp', ctx=Load()),
                                                        attr='generate',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='token',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='totp', ctx=Load()),
                                                        attr='generate',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='time',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=30, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='token',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='totp_hook', ctx=Load()),
                                    attr='routing_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='json', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_clear_routing_map',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='Home', ctx=Load()),
                                    attr='totp_hook',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Call(
                                    func=Attribute(
                                        value=Name(id='http', ctx=Load()),
                                        attr='route',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='/totphook', kind=None)],
                                    keywords=[
                                        keyword(
                                            arg='type',
                                            value=Constant(value='json', kind=None),
                                        ),
                                        keyword(
                                            arg='auth',
                                            value=Constant(value='none', kind=None),
                                        ),
                                    ],
                                ),
                                args=[Name(id='totp_hook', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_cleanup',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Delete(
                                    targets=[
                                        Attribute(
                                            value=Name(id='Home', ctx=Load()),
                                            attr='totp_hook',
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_clear_routing_map',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='addCleanup',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_totp',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value='totp_tour_setup', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='demo', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='xmlrpc_common',
                                                ctx=Load(),
                                            ),
                                            attr='authenticate',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='get_db_name', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='demo', kind=None),
                                            Constant(value='demo', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Should not have returned a uid', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='xmlrpc_common',
                                                ctx=Load(),
                                            ),
                                            attr='authenticate',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='get_db_name', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='demo', kind=None),
                                            Constant(value='demo', kind=None),
                                            Dict(
                                                keys=[Constant(value='interactive', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Trying to fake the auth type should not work', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.user_demo', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaisesRegex',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='Fault', ctx=Load()),
                                            Constant(value='Access Denied', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='xmlrpc_object',
                                                ctx=Load(),
                                            ),
                                            attr='execute_kw',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='get_db_name', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='uid', ctx=Load()),
                                            Constant(value='demo', kind=None),
                                            Constant(value='res.users', kind=None),
                                            Constant(value='read', kind=None),
                                            List(
                                                elts=[
                                                    Name(id='uid', ctx=Load()),
                                                    List(
                                                        elts=[Constant(value='login', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='totp_login_enabled', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='totp_login_device', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='totp_login_disabled', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='xmlrpc_common',
                                        ctx=Load(),
                                    ),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_db_name', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='demo', kind=None),
                                    Constant(value='demo', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='uid', ctx=Load()),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.user_demo', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='r', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='xmlrpc_object',
                                        ctx=Load(),
                                    ),
                                    attr='execute_kw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_db_name', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='uid', ctx=Load()),
                                    Constant(value='demo', kind=None),
                                    Constant(value='res.users', kind=None),
                                    Constant(value='read', kind=None),
                                    List(
                                        elts=[
                                            Name(id='uid', ctx=Load()),
                                            List(
                                                elts=[Constant(value='login', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='login', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='demo', kind=None),
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
                    name='test_totp_administration',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value='totp_tour_setup', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='demo', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value='totp_admin_disables', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='totp_login_disabled', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value=None, kind=None),
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
                    name='test_totp_authenticate',
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
                            value=Constant(value="\n        Ensure that JSON-RPC authentication works and don't return the user id\n        without TOTP check\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value='totp_tour_setup', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='demo', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/session/logout', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Content-Type', kind=None)],
                                values=[Constant(value='application/json', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payload', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='method', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value='2.0', kind=None),
                                    Constant(value='call', kind=None),
                                    Constant(value=0, kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='db', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='password', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='get_db_name', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='demo', kind=None),
                                            Constant(value='demo', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
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
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/session/authenticate', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='payload', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=Name(id='headers', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='json',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='result', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='uid', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
