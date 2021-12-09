Module(
    body=[
        ImportFrom(
            module='psycopg2',
            names=[alias(name='IntegrityError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.service.model',
            names=[alias(name='check', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWebsiteResUsers',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                            targets=[Name(id='websites', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Test Website', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Test Website 2', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='website_1',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='website_2',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='websites', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_no_website',
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
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='new_test_user', ctx=Load()),
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
                                                value=Constant(value='Pou', kind=None),
                                            ),
                                            keyword(
                                                arg='website_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_websites_set_null',
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
                            targets=[Name(id='user_1', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_1',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_2', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_2',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='user_1', ctx=Load()),
                                                op=BitOr(),
                                                right=Name(id='user_2', ctx=Load()),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='website_id', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_null_and_website',
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
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_1',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Constant(value=False, kind=None),
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
                    name='test_change_login',
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
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_1',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_belle', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Belle', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_1',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='IntegrityError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user_belle', ctx=Load()),
                                            attr='login',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Pou', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_change_login_no_website',
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
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_belle', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Belle', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='user_belle', ctx=Load()),
                                            attr='login',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Pou', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_same_website_message',
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
                        FunctionDef(
                            name='check_new_test_user',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='dbname', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='new_test_user', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='context',
                                                        value=Dict(
                                                            keys=[Constant(value='land', kind=None)],
                                                            values=[Constant(value='en_US', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='login',
                                                value=Constant(value='Pou', kind=None),
                                            ),
                                            keyword(
                                                arg='website_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='website_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[Name(id='check', ctx=Load())],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
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
                                        value=Constant(value='Pou', kind=None),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_1',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='check_new_test_user', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='registry',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_db',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
