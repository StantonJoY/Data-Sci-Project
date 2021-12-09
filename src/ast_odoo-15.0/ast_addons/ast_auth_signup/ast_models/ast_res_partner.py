Module(
    body=[
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SignupError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        FunctionDef(
            name='random_token',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='chars', ctx=Store())],
                    value=Constant(value='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value='', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='SystemRandom',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='choice',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='chars', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='_', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Constant(value=20, kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
        FunctionDef(
            name='now',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='now',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        op=Add(),
                        right=Call(
                            func=Name(id='timedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg=None,
                                    value=Name(id='kwargs', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ResPartner',
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
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signup_token', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_erp_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signup_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Signup Token Type', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_erp_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signup_expiration', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_erp_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signup_valid', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_signup_valid', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Signup Token is Valid', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='signup_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_signup_url', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Signup URL', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_signup_valid',
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
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='now', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='partner', ctx=Store()),
                                    Name(id='partner_sudo', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='signup_valid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='partner_sudo', ctx=Load()),
                                                        attr='signup_token',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='partner_sudo', ctx=Load()),
                                                            attr='signup_expiration',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Name(id='dt', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='partner_sudo', ctx=Load()),
                                                                attr='signup_expiration',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='signup_token', kind=None),
                                Constant(value='signup_expiration', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_signup_url',
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
                            value=Constant(value=' proxy for function field towards actual implementation ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_signup_url_for_action',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='u', ctx=Load()),
                                                        attr='has_group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.group_user', kind=None)],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='u', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='user_ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='u', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='check_access_rights',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='write', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='signup_url',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_signup_url_for_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                            arg(arg='view_type', annotation=None, type_comment=None),
                            arg(arg='menu_id', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' generate a signup url for the given partner ids and action, possibly overriding\n            the url state components (menu_id, id, view_type) ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='base_url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='signup_valid', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='user_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='signup_prepare',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='route', ctx=Store())],
                                    value=Constant(value='login', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='db',
                                                value=Attribute(
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
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='signup_type', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='signup_force_type_in_url', kind=None),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='signup_type',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='signup_type', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='route', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Name(id='signup_type', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='reset', kind=None)],
                                                ),
                                                body=Constant(value='reset_password', kind=None),
                                                orelse=Name(id='signup_type', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='signup_token',
                                                ctx=Load(),
                                            ),
                                            Name(id='signup_type', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='query', ctx=Load()),
                                                    slice=Constant(value='token', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='signup_token',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='query', ctx=Load()),
                                                            slice=Constant(value='login', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='user_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='login',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[Continue()],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Name(id='url', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='query', ctx=Load()),
                                                    slice=Constant(value='redirect', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='url', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='fragment', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='base', ctx=Store())],
                                            value=Constant(value='/web#', kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='action', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='/mail/view', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='base', ctx=Store())],
                                                    value=Constant(value='/mail/view?', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='action', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='fragment', ctx=Load()),
                                                                    slice=Constant(value='action', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='action', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Name(id='view_type', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='fragment', ctx=Load()),
                                                            slice=Constant(value='view_type', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='view_type', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='menu_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='fragment', ctx=Load()),
                                                            slice=Constant(value='menu_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='menu_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='model', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='fragment', ctx=Load()),
                                                            slice=Constant(value='model', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='model', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='res_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='fragment', ctx=Load()),
                                                            slice=Constant(value='res_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='res_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='fragment', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='query', ctx=Load()),
                                                            slice=Constant(value='redirect', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Name(id='base', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='werkzeug', ctx=Load()),
                                                                    attr='urls',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='url_encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='fragment', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='signup_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/web/%s?%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='route', ctx=Load()),
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
                                                    args=[Name(id='query', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='relative_url', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='signup_url', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='urls',
                                                        ctx=Load(),
                                                    ),
                                                    attr='url_join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='base_url', ctx=Load()),
                                                    Name(id='signup_url', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='signup_url', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_signup_prepare',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='signup_prepare',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='signup_get_auth_param',
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
                            value=Constant(value=' Get a signup token related to the partner if signup is enabled.\n            If the partner already has a user, get the login parameter.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
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
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.group_user', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Name(id='exceptions', ctx=Load()),
                                            attr='AccessDenied',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='allow_signup', ctx=Store())],
                            value=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_get_signup_invitation_scope',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='b2c', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='allow_signup', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='user_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='signup_prepare',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='auth_signup_token', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='signup_token',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='auth_login', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='user_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='login',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='signup_cancel',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='signup_token', kind=None),
                                            Constant(value='signup_type', kind=None),
                                            Constant(value='signup_expiration', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
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
                FunctionDef(
                    name='signup_prepare',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='signup_type', annotation=None, type_comment=None),
                            arg(arg='expiration', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='signup', kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' generate a new token for the partners with the given validity, if necessary\n            :param expiration: the expiration datetime of the token (string, optional)\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='expiration', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='signup_valid',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='token', ctx=Store())],
                                            value=Call(
                                                func=Name(id='random_token', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_signup_retrieve_partner',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='token', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='token', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='random_token', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='signup_token', kind=None),
                                                            Constant(value='signup_type', kind=None),
                                                            Constant(value='signup_expiration', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='token', ctx=Load()),
                                                            Name(id='signup_type', ctx=Load()),
                                                            Name(id='expiration', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_signup_retrieve_partner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='check_validity', annotation=None, type_comment=None),
                            arg(arg='raise_exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' find the partner corresponding to a token, and possibly check its validity\n            :param token: the token to resolve\n            :param check_validity: if True, also check validity\n            :param raise_exception: if True, raise exception instead of returning False\n            :return: partner (browse record) or False (if raise_exception is False)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='signup_token', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='token', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='partner', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Name(id='raise_exception', ctx=Load()),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='exceptions', ctx=Load()),
                                                    attr='UserError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value="Signup token '%s' is not valid", kind=None),
                                                            Name(id='token', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='check_validity', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='signup_valid',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Name(id='raise_exception', ctx=Load()),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='exceptions', ctx=Load()),
                                                    attr='UserError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value="Signup token '%s' is no longer valid", kind=None),
                                                            Name(id='token', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='partner', ctx=Load()),
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
                    name='signup_retrieve_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" retrieve the user info about the token\n            :return: a dictionary with the user information:\n                - 'db': the name of the database\n                - 'token': the token, if token is valid\n                - 'name': the name of the partner, if token is valid\n                - 'login': the user login, if the user already exists\n                - 'email': the partner email, if the user does not exist\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_signup_retrieve_partner',
                                    ctx=Load(),
                                ),
                                args=[Name(id='token', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='raise_exception',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='db', kind=None)],
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
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='partner', ctx=Load()),
                                attr='signup_valid',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='token', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='partner', ctx=Load()),
                                attr='user_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='login', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='email', kind=None),
                                            ctx=Store(),
                                        ),
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='login', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
