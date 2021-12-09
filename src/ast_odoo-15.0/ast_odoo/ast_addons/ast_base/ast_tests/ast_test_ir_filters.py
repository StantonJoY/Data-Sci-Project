Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='exceptions', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='TransactionCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='ADMIN_USER_ID', asname=None),
                alias(name='tagged', asname=None),
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
            name='noid',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='seq', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Removes values that are not relevant for the test comparisons ', kind=None),
                ),
                For(
                    target=Name(id='d', ctx=Store()),
                    iter=Name(id='seq', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='d', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='d', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='action_id', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='seq', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='FiltersCase',
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
                                            Name(id='FiltersCase', ctx=Load()),
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
                                    attr='USER_NG',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
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
                                        attr='name_search',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='demo', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='USER_ID',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='USER_NG',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='build',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ADMIN_USER_ID', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='args', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Model', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestGetFilters',
            bases=[Name(id='FiltersCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_own_filters',
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
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='c', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='d', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
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
                                                slice=Constant(value='ir.filters', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='d', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_global_filters',
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
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='c', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='d', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
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
                                                slice=Constant(value='ir.filters', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='d', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_no_third_party_filters',
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
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Name(id='ADMIN_USER_ID', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='c', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='d', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Name(id='ADMIN_USER_ID', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
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
                                                slice=Constant(value='ir.filters', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestOwnDefaults',
            bases=[Name(id='FiltersCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_new_no_filter',
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
                            value=Constant(value='\n        When creating a @is_default filter with no existing filter, that new\n        filter gets the default flag\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='a', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_new_filter_not_default',
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
                            value=Constant(value='\n        When creating a @is_default filter with existing non-default filters,\n        the new filter gets the flag\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='c', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_new_filter_existing_default',
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
                            value=Constant(value='\n        When creating a @is_default filter where an existing filter is already\n        @is_default, the flag should be *moved* from the old to the new filter\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='is_default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='c', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_update_filter_set_default',
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
                            value=Constant(value='\n        When updating an existing filter to @is_default, if an other filter\n        already has the flag the flag should be moved\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='is_default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='USER_ID',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='a', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='USER_ID',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='USER_NG',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestGlobalDefaults',
            bases=[Name(id='FiltersCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_new_filter_not_default',
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
                            value=Constant(value='\n        When creating a @is_default filter with existing non-default filters,\n        the new filter gets the flag\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='c', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='c', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_new_filter_existing_default',
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
                            value=Constant(value='\n        When creating a @is_default filter where an existing filter is already\n        @is_default, an error should be generated\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='is_default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='UserError',
                                                ctx=Load(),
                                            ),
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
                                            value=Name(id='Filters', ctx=Load()),
                                            attr='create_or_replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='model_id', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='is_default', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='c', kind=None),
                                                    Constant(value='ir.filters', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=True, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_update_filter_set_default',
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
                            value=Constant(value='\n        When updating an existing filter to @is_default, if an other filter\n        already has the flag an error should be generated\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='is_default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
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
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='UserError',
                                                ctx=Load(),
                                            ),
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
                                            value=Name(id='Filters', ctx=Load()),
                                            attr='create_or_replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='model_id', kind=None),
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='is_default', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='ir.filters', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=True, kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_update_default_filter',
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
                            value=Constant(value='\n        Replacing the current default global filter should not generate any error\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.filters', kind=None),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='a', kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='is_default',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='USER_ID',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context_value', ctx=Store())],
                            value=Constant(value="{'some_key': True}", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create_or_replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='context', kind=None),
                                            Constant(value='is_default', kind=None),
                                        ],
                                        values=[
                                            Constant(value='b', kind=None),
                                            Constant(value='ir.filters', kind=None),
                                            Constant(value=False, kind=None),
                                            Name(id='context_value', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='get_filters',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ir.filters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='noid', ctx=Load()),
                                        args=[Name(id='filters', ctx=Load())],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Constant(value='{}', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Constant(value='b', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='user_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='is_default',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Constant(value='[]', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Name(id='context_value', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='sort',
                                                        value=Constant(value='[]', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestReadGroup',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Test function read_group with groupby on a many2one field to a model\n    (in test, "user_id" to "res.users") which is ordered by an inherited not stored field (in\n    test, "name" inherited from "res.partners").\n    ', kind=None),
                ),
                FunctionDef(
                    name='test_read_group_1',
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
                            targets=[Name(id='Users', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
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
                                        value=Name(id='Users', ctx=Load()),
                                        attr='_order',
                                        ctx=Load(),
                                    ),
                                    Constant(value='name, login', kind=None),
                                    Constant(value='Model res.users must be ordered by name, login', kind=None),
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
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='Users', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='store',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Field name is not stored in res.users', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Filters', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.filters', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filter_a', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='Filter_A', kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filter_b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='Filter_B', kind=None),
                                            ),
                                            keyword(
                                                arg='model_id',
                                                value=Constant(value='ir.filters', kind=None),
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
                                    value=Name(id='filter_b', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Filters', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='user_id', kind=None)],
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Subscript(
                                                        value=Name(id='val', ctx=Load()),
                                                        slice=Constant(value='user_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=False, kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='val', ctx=Store()),
                                                        iter=Name(id='res', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value="At least one group must contain val['user_id'] == False.", kind=None),
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
        ClassDef(
            name='TestAllFilters',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='check_filter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='groupby', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
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
                                                                slice=Name(id='model', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='context', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='read_group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='domain', ctx=Load()),
                                                    Name(id='fields', ctx=Load()),
                                                    Name(id='groupby', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='orderby',
                                                        value=Name(id='order', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='failureException',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Test filter '%s' failed: %s", kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='name', ctx=Load()),
                                                                        Name(id='e', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='failureException',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Test filter '%s' failed: field or aggregate %s does not exist", kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='name', ctx=Load()),
                                                                        Name(id='e', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='domain', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
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
                                                                        slice=Name(id='model', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='context', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='domain', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='order',
                                                                value=Name(id='order', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ValueError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='failureException',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value="Test filter '%s' failed: %s", kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Name(id='name', ctx=Load()),
                                                                                Name(id='e', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=Constant(value=None, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='No domain or group by in filter %s with model %s and context %s', kind=None),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='context', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_filters',
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
                        For(
                            target=Name(id='filter_', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.filters', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
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
                                                        arg='name',
                                                        value=Attribute(
                                                            value=Name(id='filter_', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='context', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ast', ctx=Load()),
                                                    attr='literal_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='filter_', ctx=Load()),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='groupby', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='context', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='group_by', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='check_filter',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Attribute(
                                                            value=Name(id='filter_', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='model',
                                                        value=Attribute(
                                                            value=Name(id='filter_', ctx=Load()),
                                                            attr='model_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='domain',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='filter_', ctx=Load()),
                                                                attr='_get_eval_domain',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='fields',
                                                        value=ListComp(
                                                            elt=Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='field', ctx=Load()),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=':', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='field', ctx=Store()),
                                                                    iter=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Name(id='groupby', ctx=Load()),
                                                                            List(elts=[], ctx=Load()),
                                                                        ],
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='groupby',
                                                        value=Name(id='groupby', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='order',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value=',', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='ast', ctx=Load()),
                                                                        attr='literal_eval',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='filter_', ctx=Load()),
                                                                            attr='sort',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='context',
                                                        value=Name(id='context', ctx=Load()),
                                                    ),
                                                ],
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
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='migration', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
