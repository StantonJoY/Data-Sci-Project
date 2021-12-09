Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='mail_new_test_user', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMailPluginControllerCommon',
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
                                        args=[
                                            Name(id='TestMailPluginControllerCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_test',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='employee', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user,base.group_partner_manager', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mock_plugin_partner_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                            arg(arg='patched_iap_enrich', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Simulate a HTTP call to /partner/get with the given email and name.\n\n        The authentication process is patched to allow all queries.\n        The third argument "patched_iap_enrich" allow you to mock the IAP request and\n        to return the response you want.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='patched_auth_method_outlook',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='uid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_test',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='method', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value=0, kind=None),
                                    Constant(value='2.0', kind=None),
                                    Constant(value='call', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='email', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.mail_plugin.models.ir_http.IrHttp._auth_method_outlook', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='patched_auth_method_outlook', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.mail_plugin.controllers.mail_plugin.MailPluginController._iap_enrich', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='patched_iap_enrich', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url_open',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/mail_plugin/partner/get', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='json', ctx=Load()),
                                                                attr='dumps',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='data', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Dict(
                                                    keys=[Constant(value='Content-Type', kind=None)],
                                                    values=[Constant(value='application/json', kind=None)],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='ok',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='result', kind=None),
                                    Dict(keys=[], values=[]),
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
                    name='mock_enrich_and_create_company',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='patched_iap_enrich', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Simulate a HTTP call to /partner/enrich_and_create_company on the given partner.\n\n        The third argument "patched_iap_enrich" allow you to mock the IAP request and\n        to return the response you want.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='patched_auth_method_outlook',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='uid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_test',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='jsonrpc', kind=None),
                                    Constant(value='method', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value=0, kind=None),
                                    Constant(value='2.0', kind=None),
                                    Constant(value='call', kind=None),
                                    Dict(
                                        keys=[Constant(value='partner_id', kind=None)],
                                        values=[Name(id='partner_id', ctx=Load())],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.mail_plugin.models.ir_http.IrHttp._auth_method_outlook', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='patched_auth_method_outlook', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.mail_plugin.controllers.mail_plugin.MailPluginController._iap_enrich', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='patched_iap_enrich', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url_open',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/mail_plugin/partner/enrich_and_create_company', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='json', ctx=Load()),
                                                                attr='dumps',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='data', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Dict(
                                                    keys=[Constant(value='Content-Type', kind=None)],
                                                    values=[Constant(value='application/json', kind=None)],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='ok',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='result', kind=None),
                                    Dict(keys=[], values=[]),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
