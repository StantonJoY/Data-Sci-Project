Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tests', asname=None)],
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
        ClassDef(
            name='TestMenusAdmin',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_click_everywhere_as_admin',
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
                            targets=[Name(id='menus', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='load_menus',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='app_id', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='menus', ctx=Load()),
                                    slice=Constant(value='root', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='children', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='subTest',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='app',
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='menus', ctx=Load()),
                                                                slice=Name(id='app_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
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
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='runbot',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Testing %s', kind=None),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='menus', ctx=Load()),
                                                            slice=Name(id='app_id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='name', kind=None),
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
                                                    attr='browser_js',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/web', kind=None),
                                                    BinOp(
                                                        left=Constant(value="odoo.__DEBUG__.services['web.clickEverywhere']('%s');", kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='menus', ctx=Load()),
                                                                slice=Name(id='app_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='xmlid', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='odoo.isReady === true', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='login',
                                                        value=Constant(value='admin', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='timeout',
                                                        value=Constant(value=300, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='terminate_browser',
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='click_all', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='-standard', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMenusDemo',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_click_everywhere_as_demo',
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
                            targets=[Name(id='user_demo', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='menus', ctx=Store())],
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
                                                slice=Constant(value='ir.ui.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='user_demo', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='load_menus',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='app_id', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='menus', ctx=Load()),
                                    slice=Constant(value='root', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='children', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='subTest',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='app',
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='menus', ctx=Load()),
                                                                slice=Name(id='app_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
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
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='runbot',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Testing %s', kind=None),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='menus', ctx=Load()),
                                                            slice=Name(id='app_id', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='name', kind=None),
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
                                                    attr='browser_js',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/web', kind=None),
                                                    BinOp(
                                                        left=Constant(value="odoo.__DEBUG__.services['web.clickEverywhere']('%s');", kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='menus', ctx=Load()),
                                                                slice=Name(id='app_id', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='xmlid', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Constant(value='odoo.isReady === true', kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='login',
                                                        value=Constant(value='demo', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='timeout',
                                                        value=Constant(value=300, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='terminate_browser',
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='click_all', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='-standard', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMenusAdminLight',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_click_apps_menus_as_admin',
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
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value="odoo.__DEBUG__.services['web.clickEverywhere'](undefined, true);", kind=None),
                                    Constant(value='odoo.isReady === true', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=120, kind=None),
                                    ),
                                ],
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
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestMenusDemoLight',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_click_apps_menus_as_demo',
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
                                    attr='browser_js',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/web', kind=None),
                                    Constant(value="odoo.__DEBUG__.services['web.clickEverywhere'](undefined, true);", kind=None),
                                    Constant(value='odoo.isReady === true', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='demo', kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=120, kind=None),
                                    ),
                                ],
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
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
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
