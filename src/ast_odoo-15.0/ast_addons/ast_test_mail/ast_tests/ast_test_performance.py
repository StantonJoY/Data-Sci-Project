Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='TransactionCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='users', asname=None),
                alias(name='warmup', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='mute_logger', asname=None),
                alias(name='formataddr', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='BaseMailPerformance',
            bases=[Name(id='TransactionCaseWithUserDemo', ctx=Load())],
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
                                            Name(id='BaseMailPerformance', ctx=Load()),
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
                                    attr='_quick_create_ctx',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='no_reset_password', kind=None),
                                    Constant(value='mail_create_nolog', kind=None),
                                    Constant(value='mail_create_nosubscribe', kind=None),
                                    Constant(value='mail_notrack', kind=None),
                                    Constant(value='mail_channel_nosubscribe', kind=None),
                                ],
                                values=[
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_employee',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='signature', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Ernest Employee', kind=None),
                                            Constant(value='emp', kind=None),
                                            Constant(value='e.e@example.com', kind=None),
                                            Constant(value='--\nErnest', kind=None),
                                            Constant(value='inbox', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                                                            args=[Constant(value='base.group_partner_manager', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    Constant(value='ready', kind=None),
                                    Constant(value=True, kind=None),
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
                    name='_init_mail_gateway',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alias_domain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='example.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alias_catchall',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='catchall.test', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alias_bounce',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='bounce.test', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_from',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='notifications', kind=None),
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
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.bounce.alias', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_bounce',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.catchall.domain', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_domain',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.catchall.alias', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_catchall',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.default.from', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='default_from',
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_performance', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestBaseMailPerformance',
            bases=[Name(id='BaseMailPerformance', ctx=Load())],
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
                                            Name(id='TestBaseMailPerformance', ctx=Load()),
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
                                    attr='res_partner_3',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Gemini Furniture', kind=None),
                                            Constant(value='gemini.furniture39@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='res_partner_4',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Ready Mat', kind=None),
                                            Constant(value='ready.mat28@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='res_partner_10',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='The Jackson Group', kind=None),
                                            Constant(value='jackson.group82@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='res_partner_12',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Azure Interior', kind=None),
                                            Constant(value='azure.Interior24@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='mail.performance.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Object 0', kind=None),
                                                    Constant(value=0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_3',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Object 1', kind=None),
                                                    Constant(value=10, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_3',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Object 2', kind=None),
                                                    Constant(value=20, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_4',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Object 3', kind=None),
                                                    Constant(value=30, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_10',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Object 4', kind=None),
                                                    Constant(value=40, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_12',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mail_gateway',
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
                    name='test_read_mail',
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
                            value=Constant(value=" Read records inheriting from 'mail.thread'. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.performance.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='records', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='value_pc',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_write_mail',
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
                            value=Constant(value=" Write records inheriting from 'mail.thread' (no recomputation). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.performance.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='records', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='X', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_write_mail_with_recomputation',
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
                            value=Constant(value=" Write records inheriting from 'mail.thread' (with recomputation). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.performance.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='records', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='value', kind=None)],
                                                values=[Constant(value=42, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_write_mail_with_tracking',
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
                            value=Constant(value=" Write records inheriting from 'mail.thread' (with field tracking). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.performance.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='track', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Constant(value='Y', kind=None),
                                            Constant(value=40, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='res_partner_12',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=3, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='track',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='X', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_mail',
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
                            value=Constant(value=" Create records inheriting from 'mail.thread' (without field tracking). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.performance.thread', kind=None),
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='tracking_disable',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='X', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_mail_with_tracking',
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
                            value=Constant(value=" Create records inheriting from 'mail.thread' (with field tracking). ", kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=8, kind=None),
                                            ),
                                            keyword(
                                                arg='demo',
                                                value=Constant(value=8, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                slice=Constant(value='mail.performance.thread', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='X', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='demo', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_mail_simple',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=7, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                slice=Constant(value='mail.test.simple', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Test', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_write_mail_simple',
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
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test2', kind=None),
                                                    Constant(value='test@test.com', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_performance', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMailAPIPerformance',
            bases=[Name(id='BaseMailPerformance', ctx=Load())],
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
                                            Name(id='TestMailAPIPerformance', ctx=Load()),
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
                                    attr='customer',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Customer', kind=None),
                                            Constant(value='customer.test@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                func=Attribute(
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Paulette Testouille', kind=None),
                                            Constant(value='paul', kind=None),
                                            Constant(value='user.test.paulette@example.com', kind=None),
                                            Constant(value='inbox', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    attr='_init_mail_gateway',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='mail.mt_activities', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='default', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                    name='_create_test_records',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_record_full',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='mail.test.ticket', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='email_from', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestRecord', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_test',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='nopartner.test@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_template_full',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='body_html', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='partner_to', kind=None),
                                            Constant(value='email_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestTemplate', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='mail.test.ticket', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='About {{ object.name }}', kind=None),
                                            Constant(value='<p>Hello <t t-out="object.name"/></p>', kind=None),
                                            Constant(value='{{ object.user_id.email_formatted }}', kind=None),
                                            Constant(value='{{ object.customer_id.id }}', kind=None),
                                            Constant(value='{{ ("%s Customer <%s>" % (object.name, object.email_from)) }}', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_adv_activity',
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
                            targets=[Name(id='model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mail.test.activity', kind=None),
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=7, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Test', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_adv_activity_full',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.activity', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='MailActivity', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.activity', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='default_res_model', kind=None)],
                                        values=[Constant(value='mail.test.activity', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=6, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=6, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='activity', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='MailActivity', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='activity_type_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test Activity', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                                                            args=[Constant(value='mail.mail_activity_data_todo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='category', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='activity', ctx=Load()),
                                            attr='activity_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='category',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=17, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=19, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='activity', ctx=Load()),
                                            attr='action_feedback',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='feedback',
                                                value=Constant(value='Zizisse Done !', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_adv_activity_mixin',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.activity', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=8, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=8, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='activity', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='action_start',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Test Start', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='category', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='activity', ctx=Load()),
                                            attr='activity_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='category',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Dupe write', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=18, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=21, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='action_close',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Dupe feedback', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='activity_ids',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.activity', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mail_composer',
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
                                    attr='_create_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_record_full',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Load(),
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='composer', ctx=Store())],
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
                                                        slice=Constant(value='mail.compose.message', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='default_composition_mode', kind=None),
                                                            Constant(value='default_model', kind=None),
                                                            Constant(value='default_res_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='comment', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='body', kind=None),
                                                    Constant(value='partner_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='<p>Test Body</p>', kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=4, kind=None),
                                                                    Name(id='customer_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=32, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=38, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='composer', ctx=Load()),
                                            attr='_action_send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mail_composer_nodelete',
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
                                    attr='_create_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_record_full',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Load(),
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='composer', ctx=Store())],
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
                                                        slice=Constant(value='mail.compose.message', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='default_composition_mode', kind=None),
                                                            Constant(value='default_model', kind=None),
                                                            Constant(value='default_res_id', kind=None),
                                                            Constant(value='mail_auto_delete', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='comment', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='body', kind=None),
                                                    Constant(value='partner_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='<p>Test Body</p>', kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=4, kind=None),
                                                                    Name(id='customer_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=25, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=31, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='composer', ctx=Load()),
                                            attr='_action_send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mail_composer_w_template',
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
                                    attr='_create_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_record_full',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_template_full',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=11, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=12, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='composer', ctx=Store())],
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
                                                        slice=Constant(value='mail.compose.message', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='default_composition_mode', kind=None),
                                                            Constant(value='default_model', kind=None),
                                                            Constant(value='default_res_id', kind=None),
                                                            Constant(value='default_template_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='comment', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='test_record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='test_template', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Dict(keys=[], values=[])],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='composer', ctx=Load()),
                                            attr='_onchange_template_id_wrapper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=33, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=39, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='composer', ctx=Load()),
                                            attr='_action_send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='nopartner.test@example.com', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_assignation_email',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_test',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='notification_type', kind=None)],
                                        values=[Constant(value='email', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=38, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=39, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='user_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_assignation_inbox',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=17, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=19, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='user_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_log',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_message_log',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test _message_log</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_log_with_post',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=4, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test message_post as log</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_note', kind=None),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_post_no_notification',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=4, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test Post Performances basic</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=List(elts=[], ctx=Load()),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_post_one_email_notification',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=29, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=32, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test Post Performances with an email ping</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='customer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_post_one_inbox_notification',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=12, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=16, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test Post Performances with an inbox ping</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_subscribe_default',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=6, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=6, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=3, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_subscribe_subtypes',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.simple', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtype_ids', ctx=Store())],
                            value=Attribute(
                                value=BinOp(
                                    left=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_simple_external', kind=None)],
                                        keywords=[],
                                    ),
                                    op=BitOr(),
                                    right=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.mt_comment', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                attr='ids',
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=5, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=5, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='subtype_ids',
                                                value=Name(id='subtype_ids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_test',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='subtype_ids',
                                                value=Name(id='subtype_ids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_track',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.performance.tracking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Zizizatestname', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=3, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=3, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Zizizanewtestname', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=5, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=5, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            DictComp(
                                                key=BinOp(
                                                    left=Constant(value='field_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                value=BinOp(
                                                    left=Constant(value='Tracked Char Fields %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=3, kind=None)],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=6, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=6, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            DictComp(
                                                key=BinOp(
                                                    left=Constant(value='field_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                value=BinOp(
                                                    left=Constant(value='Field Without Cache %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=3, kind=None)],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            DictComp(
                                                key=BinOp(
                                                    left=Constant(value='field_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                value=BinOp(
                                                    left=Constant(value='Field With Cache %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=3, kind=None)],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_notification_reply_to_batch',
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
                            targets=[Name(id='test_records_sudo', ctx=Store())],
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
                                                slice=Constant(value='mail.test.container', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='alias_name', kind=None),
                                                Constant(value='customer_id', kind=None),
                                                Constant(value='name', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='alias.test.%s.%d', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
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
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='index', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='customer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                BinOp(
                                                    left=Constant(value='Test_%d', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='index', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='index', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=10, kind=None)],
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
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='test_records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.test.container', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='test_records_sudo', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='reply_to', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='test_records', ctx=Load()),
                                            attr='_notify_get_reply_to',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default',
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
                                                    attr='email_formatted',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='test_records', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='reply_to', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='formataddr', ctx=Load()),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            BinOp(
                                                                left=Constant(value='%s %s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
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
                                                                                attr='company_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='%s@%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='alias_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='alias_domain',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_performance', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMailComplexPerformance',
            bases=[Name(id='BaseMailPerformance', ctx=Load())],
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
                                            Name(id='TestMailComplexPerformance', ctx=Load()),
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
                                    attr='user_portal',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='signature', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Olivia Portal', kind=None),
                                            Constant(value='port', kind=None),
                                            Constant(value='p.p@example.com', kind=None),
                                            Constant(value='--\nOlivia', kind=None),
                                            Constant(value='email', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_portal', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='admin',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Customer', kind=None),
                                            Constant(value='test@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='container',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='mail.test.container', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_create_nosubscribe',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='alias_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Container', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test-alias', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_quick_create_ctx',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='partners',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='x', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Constant(value=10, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partners',
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Partners', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='email', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='Test %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='x', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='test%s@example.com', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='x', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='message_subscribe',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='subtype_ids',
                                        value=List(
                                            elts=[
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
                                                        args=[Constant(value='mail.mt_comment', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
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
                                                        args=[Constant(value='test_mail.st_mail_test_container_child_full', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mail_gateway',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='flush',
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
                    name='test_complex_mail_mail_send',
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
                            targets=[Name(id='message', ctx=Store())],
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
                                                slice=Constant(value='mail.message', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subject', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='author_id', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Constant(value='<p>Test</p>', kind=None),
                                            Attribute(
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
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            Constant(value='mail.test.container', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='container',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail', ctx=Store())],
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
                                                slice=Constant(value='mail.mail', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='body_html', kind=None),
                                            Constant(value='mail_message_id', kind=None),
                                            Constant(value='recipient_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='<p>Test</p>', kind=None),
                                            Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=4, kind=None),
                                                        Name(id='pid', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='pid', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='mail', ctx=Load()),
                                attr='ids',
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=8, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=8, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
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
                                                                slice=Constant(value='mail.mail', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mail_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='send',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mail', ctx=Load()),
                                        attr='body_html',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Test</p>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='mail', ctx=Load()),
                                        attr='reply_to',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='formataddr', ctx=Load()),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='container',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='test-alias@example.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_message_post',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='message_subscribe',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=63, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=64, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test Post Performances</p>', kind=None),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    Constant(value='<p>Test Post Performances</p>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_message_post_template',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='message_subscribe',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='container',
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template_id', ctx=Store())],
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
                                    args=[Constant(value='test_mail.mail_test_container_tpl', kind=None)],
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=72, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=73, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_post_with_template',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_id', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='composition_mode',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='<p>Adding stuff on %s</p>', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='customer',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_message_subscribe',
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
                            targets=[Name(id='pids', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='partners',
                                    ctx=Load(),
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtypes', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='mail.mt_comment', kind=None)],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subtype_ids', ctx=Store())],
                            value=Attribute(
                                value=Name(id='subtypes', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='container_id', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=7, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Subscript(
                                                    value=Name(id='pids', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=4, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='subtype_ids',
                                                value=Name(id='subtype_ids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=4, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=6, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=6, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Subscript(
                                                    value=Name(id='pids', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=6, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='subtype_ids',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=6, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=7, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=7, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='message_subscribe',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Name(id='pids', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='subtype_ids',
                                                value=Name(id='subtype_ids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_tracking_assignation',
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
                            value=Constant(value=' Assignation performance test on already-created record ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='container_id', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='container',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=38, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=39, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='user_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_portal',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.mt_note', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partners',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_tracking_subscription_create',
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
                            value=Constant(value=' Creation performance test involving auto subscription, assignation, tracking with subtype and template send. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='container_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='container',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_portal',
                                    ctx=Load(),
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=109, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=110, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='rec', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.test.ticket', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='container_id', kind=None),
                                                    Constant(value='customer_id', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test', kind=None),
                                                    Name(id='container_id', ctx=Load()),
                                                    Name(id='customer_id', ctx=Load()),
                                                    Name(id='user_id', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_tracking_subscription_subtype',
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
                            value=Constant(value=' Write performance test involving auto subscription, tracking with subtype ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='container_id', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=77, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=77, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='container_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test2', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='container',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.mt_note', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_tracking_subscription_write',
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
                            value=Constant(value=' Write performance test involving auto subscription, tracking with subtype and template send ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='container_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='container',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='container2', ctx=Store())],
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
                                                slice=Constant(value='mail.test.container', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_create_nosubscribe',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='alias_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Container 2', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='container_id', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Attribute(
                                                value=Name(id='container2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=85, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=85, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='container_id', kind=None),
                                                    Constant(value='customer_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test2', kind=None),
                                                    Name(id='container_id', ctx=Load()),
                                                    Name(id='customer_id', ctx=Load()),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_portal',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_complex_tracking_template',
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
                            value=Constant(value=' Write performance test involving assignation, tracking with template ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='customer_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='ready',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We need to simulate that registery is ready', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.test.ticket', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='container_id', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='mail_template', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='container',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_portal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='test_mail.mail_test_ticket_tracking_tpl', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='active_test',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='rec1', ctx=Load()),
                                        attr='message_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partners',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=29, kind=None),
                                            ),
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=30, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='customer_id', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test2', kind=None),
                                                    Name(id='customer_id', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.message.subtype', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subject',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Test Template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.mt_note', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='subtype_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_mail.st_mail_test_ticket_container_upd', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='notified_partner_ids',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partners',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_portal',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='rec1', ctx=Load()),
                                                attr='message_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[
                                Constant(value='__system__', kind=None),
                                Constant(value='emp', kind=None),
                            ],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_format',
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
                            value=Constant(value='Test performance of `_message_format` and of `message_format` with\n        multiple messages with multiple attachments, different authors, various\n        notifications, and different tracking values.\n        Those messages might not make sense functionally but they are crafted to\n        cover as much of the code as possible in regard to number of queries.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='name_field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='container',
                                            ctx=Load(),
                                        ),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='name', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_id_field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='container',
                                            ctx=Load(),
                                        ),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='customer_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='messages', ctx=Store())],
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
                                                slice=Constant(value='mail.message', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='author_id', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='subtype_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                    Constant(value='notification_ids', kind=None),
                                                    Constant(value='tracking_value_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test 0', kind=None),
                                                    Constant(value='<p>Test 0</p>', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='mail.test.container', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='container',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.data', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_xmlid_to_res_id',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.mt_comment', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='datas', kind=None),
                                                                    ],
                                                                    values=[
                                                                        BinOp(
                                                                            left=Constant(value='test file 0 - %d', kind=None),
                                                                            op=Mod(),
                                                                            right=Name(id='j', ctx=Load()),
                                                                        ),
                                                                        Constant(value='data', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='j', ctx=Store()),
                                                                iter=Call(
                                                                    func=Name(id='range', ctx=Load()),
                                                                    args=[Constant(value=2, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_partner_id', kind=None),
                                                                            Constant(value='notification_type', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=3, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='inbox', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_partner_id', kind=None),
                                                                            Constant(value='notification_type', kind=None),
                                                                            Constant(value='notification_status', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=4, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='exception', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_partner_id', kind=None),
                                                                            Constant(value='notification_type', kind=None),
                                                                            Constant(value='notification_status', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=6, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='exception', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='field', kind=None),
                                                                            Constant(value='field_desc', kind=None),
                                                                            Constant(value='old_value_char', kind=None),
                                                                            Constant(value='new_value_char', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='name_field', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='Name', kind=None),
                                                                            Constant(value='old 0', kind=None),
                                                                            Constant(value='new 0', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='field', kind=None),
                                                                            Constant(value='field_desc', kind=None),
                                                                            Constant(value='old_value_integer', kind=None),
                                                                            Constant(value='new_value_integer', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='customer_id_field', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='Customer', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=7, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=8, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='author_id', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='subtype_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                    Constant(value='notification_ids', kind=None),
                                                    Constant(value='tracking_value_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test 1', kind=None),
                                                    Constant(value='<p>Test 1</p>', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partners',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='mail.test.container', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='container',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.data', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_xmlid_to_res_id',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.mt_note', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='datas', kind=None),
                                                                    ],
                                                                    values=[
                                                                        BinOp(
                                                                            left=Constant(value='test file 1 - %d', kind=None),
                                                                            op=Mod(),
                                                                            right=Name(id='j', ctx=Load()),
                                                                        ),
                                                                        Constant(value='data', kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='j', ctx=Store()),
                                                                iter=Call(
                                                                    func=Name(id='range', ctx=Load()),
                                                                    args=[Constant(value=2, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_partner_id', kind=None),
                                                                            Constant(value='notification_type', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=5, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='inbox', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_partner_id', kind=None),
                                                                            Constant(value='notification_type', kind=None),
                                                                            Constant(value='notification_status', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=6, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='exception', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='field', kind=None),
                                                                            Constant(value='field_desc', kind=None),
                                                                            Constant(value='old_value_char', kind=None),
                                                                            Constant(value='new_value_char', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='name_field', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='Name', kind=None),
                                                                            Constant(value='old 1', kind=None),
                                                                            Constant(value='new 1', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='field', kind=None),
                                                                            Constant(value='field_desc', kind=None),
                                                                            Constant(value='old_value_integer', kind=None),
                                                                            Constant(value='new_value_integer', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='customer_id_field', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='Customer', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=7, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='partners',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=8, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=5, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='messages', ctx=Load()),
                                            attr='message_format',
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
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='message', ctx=Store()),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='message', ctx=Load()),
                                                                slice=Constant(value='attachment_ids', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=2, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='messages', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='messages', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=17, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='messages', ctx=Load()),
                                            attr='message_format',
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
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='message', ctx=Store()),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='message', ctx=Load()),
                                                                slice=Constant(value='attachment_ids', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=2, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='emp', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_message_format_group_thread_name_by_model',
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
                            value=Constant(value='Ensures the fetch of multiple thread names is grouped by model.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='_i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.test.simple', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='name', kind=None)],
                                                        values=[Constant(value='Test', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.test.track', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Test', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='messages', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='model', kind=None),
                                                Constant(value='res_id', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='record', ctx=Store()),
                                                iter=Name(id='records', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=4, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='messages', ctx=Load()),
                                            attr='message_format',
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
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=6, kind=None),
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
                                    value=Name(id='messages', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='messages', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=13, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='messages', ctx=Load()),
                                            attr='message_format',
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
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='res', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='emp', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_performance', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMailHeavyPerformancePost',
            bases=[Name(id='BaseMailPerformance', ctx=Load())],
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
                                            Name(id='TestMailHeavyPerformancePost', ctx=Load()),
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
                                    attr='customer',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='customer', kind=None),
                                            Constant(value='customer@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='record',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='mail.test.container', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_create_nosubscribe',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='customer_id', kind=None),
                                            Constant(value='alias_name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test record', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test-alias', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_follower_email',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='user_follower_email', kind=None),
                                            Constant(value='user_follower_email', kind=None),
                                            Constant(value='user_follower_email@example.com', kind=None),
                                            Constant(value='email', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_follower_inbox',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='user_follower_inbox', kind=None),
                                            Constant(value='user_follower_inbox', kind=None),
                                            Constant(value='user_follower_inbox@example.com', kind=None),
                                            Constant(value='inbox', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='partner_follower',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='partner_follower', kind=None),
                                            Constant(value='partner_follower@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='record',
                                        ctx=Load(),
                                    ),
                                    attr='message_subscribe',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_follower',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_follower_inbox',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_follower_email',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_inbox',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='user_inbox', kind=None),
                                            Constant(value='user_inbox', kind=None),
                                            Constant(value='user_inbox@example.com', kind=None),
                                            Constant(value='inbox', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_email',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='notification_type', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='user_email', kind=None),
                                            Constant(value='user_email', kind=None),
                                            Constant(value='user_email@example.com', kind=None),
                                            Constant(value='email', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.group_user', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='partner',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_quick_create_ctx',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='partner', kind=None),
                                            Constant(value='partner@example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='vals',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='datas', kind=None),
                                        Constant(value='name', kind=None),
                                        Constant(value='mimetype', kind=None),
                                        Constant(value='res_model', kind=None),
                                        Constant(value='res_id', kind=None),
                                    ],
                                    values=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='base64', ctx=Load()),
                                                attr='b64encode',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='bytes', ctx=Load()),
                                                    args=[
                                                        BinOp(
                                                            left=Constant(value='attachement content %s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='i', ctx=Load()),
                                                        ),
                                                        Constant(value='utf-8', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        BinOp(
                                            left=Constant(value='fileText_test%s.txt', kind=None),
                                            op=Mod(),
                                            right=Name(id='i', ctx=Load()),
                                        ),
                                        Constant(value='text/plain', kind=None),
                                        Constant(value='mail.compose.message', kind=None),
                                        Constant(value=0, kind=None),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Constant(value=3, kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mail_gateway',
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
                    name='test_complete_message_post',
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
                            targets=[Name(id='partner_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_inbox',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_email',
                                                ctx=Load(),
                                            ),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='record',
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachements', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='attach tuple 1', kind=None),
                                            Constant(value='attachement tupple content 1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='attach tuple 2', kind=None),
                                            Constant(value='attachement tupple content 2', kind=None),
                                            Dict(
                                                keys=[Constant(value='cid', kind=None)],
                                                values=[Constant(value='cid1', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='attach tuple 3', kind=None),
                                            Constant(value='attachement tupple content 3', kind=None),
                                            Dict(
                                                keys=[Constant(value='cid', kind=None)],
                                                values=[Constant(value='cid2', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='attachements',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
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
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='vals',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachement_ids', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='attachements',
                                    ctx=Load(),
                                ),
                                attr='ids',
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
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='emp',
                                                value=Constant(value=70, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='sql_log',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='warm',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='sql_log_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Dict(keys=[], values=[])],
                                                keywords=[],
                                            ),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='<p>Test body <img src="cid:cid1"> <img src="cid:cid2"></p>', kind=None),
                                            ),
                                            keyword(
                                                arg='subject',
                                                value=Constant(value='Test Subject', kind=None),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='notification', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value=None, kind=None),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=Name(id='partner_ids', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='parent_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='attachments',
                                                value=Name(id='attachements', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='attachment_ids',
                                                value=Name(id='attachement_ids', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='add_sign',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='model_description',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='mail_auto_delete',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='sql_log',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='message_ids',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='body',
                                                ctx=Load(),
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='<p>Test body <img src="/web/image/', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='attachements',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_model', kind=None)],
                                        keywords=[],
                                    ),
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=3, kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='attachements',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_id', kind=None)],
                                        keywords=[],
                                    ),
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=3, kind=None)],
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
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.tests', kind=None),
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='emp', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='mail_performance', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
