Module(
    body=[
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='registry', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Users',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_login',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='user_agent_env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Users', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_login',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='db', ctx=Load()),
                                            Name(id='login', ctx=Load()),
                                            Name(id='password', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='user_agent_env',
                                                value=Name(id='user_agent_env', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name='e',
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='registry', ctx=Load()),
                                                                args=[Name(id='db', ctx=Load())],
                                                                keywords=[],
                                                            ),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cr', ctx=Load()),
                                                            attr='execute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='SELECT id FROM res_users WHERE lower(login)=%s', kind=None),
                                                            Tuple(
                                                                elts=[Name(id='login', ctx=Load())],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cr', ctx=Load()),
                                                            attr='fetchone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='res', ctx=Load()),
                                                    body=[
                                                        Raise(
                                                            exc=Name(id='e', ctx=Load()),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
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
                                                    targets=[Name(id='Ldap', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='res.company.ldap', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='conf', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='Ldap', ctx=Load()),
                                                            attr='_get_ldap_dicts',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='entry', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Ldap', ctx=Load()),
                                                                    attr='_authenticate',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='conf', ctx=Load()),
                                                                    Name(id='login', ctx=Load()),
                                                                    Name(id='password', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='entry', ctx=Load()),
                                                            body=[
                                                                Return(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Ldap', ctx=Load()),
                                                                            attr='_get_or_create_user',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='conf', ctx=Load()),
                                                                            Name(id='login', ctx=Load()),
                                                                            Name(id='entry', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_credentials',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Users', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_check_credentials',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='password', ctx=Load()),
                                            Name(id='env', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='passwd_allowed', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='interactive', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_rpc_api_keys_only',
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
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='passwd_allowed', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='active',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='Ldap', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.company.ldap', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='conf', ctx=Store()),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='Ldap', ctx=Load()),
                                                            attr='_get_ldap_dicts',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Ldap', ctx=Load()),
                                                                    attr='_authenticate',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='conf', ctx=Load()),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='user',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='login',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='password', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[Return(value=None)],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Raise(exc=None, cause=None),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='change_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='old_passwd', annotation=None, type_comment=None),
                            arg(arg='new_passwd', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='new_passwd', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='Ldap', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company.ldap', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='conf', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='Ldap', ctx=Load()),
                                            attr='_get_ldap_dicts',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='changed', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Ldap', ctx=Load()),
                                                    attr='_change_password',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='conf', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='login',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='old_passwd', ctx=Load()),
                                                    Name(id='new_passwd', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='changed', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='uid', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_set_empty_password',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='uid', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='invalidate_cache',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='password', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[Name(id='uid', ctx=Load())],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='change_password',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='old_passwd', ctx=Load()),
                                    Name(id='new_passwd', ctx=Load()),
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
                    name='_set_empty_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='UPDATE res_users SET password=NULL WHERE id=%s', kind=None),
                                    Tuple(
                                        elts=[Name(id='uid', ctx=Load())],
                                        ctx=Load(),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
