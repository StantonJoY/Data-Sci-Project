Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='HttpCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='LoadMenusTests',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='menu',
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
                                        slice=Constant(value='ir.ui.menu', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='parent_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_menu', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='search',
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
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='menu',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
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
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='search', kind=None),
                                    Name(id='search', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='admin', kind=None),
                                    Constant(value='admin', kind=None),
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
                    name='test_load_menus',
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
                            targets=[Name(id='menu_loaded', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/webclient/load_menus/1234', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='menu',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='root', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='actionID', kind=None),
                                            Constant(value='actionModel', kind=None),
                                            Constant(value='appID', kind=None),
                                            Constant(value='children', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='webIcon', kind=None),
                                            Constant(value='webIconData', kind=None),
                                            Constant(value='xmlid', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='menu',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='menu',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='test_menu', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='actionID', kind=None),
                                            Constant(value='actionModel', kind=None),
                                            Constant(value='appID', kind=None),
                                            Constant(value='children', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='webIcon', kind=None),
                                            Constant(value='webIconData', kind=None),
                                            Constant(value='xmlid', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='menu',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='root', kind=None),
                                            Constant(value='root', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertDictEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='menu_loaded', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='expected', ctx=Load()),
                                    Constant(value="load_menus didn't return the expected value", kind=None),
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
