Module(
    body=[
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='common', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestError',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
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
                                            Name(id='TestError', ctx=Load()),
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
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.user_admin', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rpc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='partial', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='xmlrpc_object',
                                            ctx=Load(),
                                        ),
                                        attr='execute',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='common', ctx=Load()),
                                            attr='get_db_name',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='uid', ctx=Load()),
                                    Constant(value='admin', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.users', kind=None),
                                    Constant(value='write', kind=None),
                                    List(
                                        elts=[Name(id='uid', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value=False, kind=None)],
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
                    name='test_01_create',
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
                            value=Constant(value=' Create: mandatory field not provided ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='test_rpc.model_b', kind=None),
                                    Constant(value='create', kind=None),
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='B1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
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
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='rpc',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='test_rpc.model_b', kind=None),
                                                    Constant(value='create', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Raise(exc=None, cause=None),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='The operation cannot be completed:', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Create/update: a mandatory field is not set.', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Delete: another model requires the record being deleted. If possible, archive it instead.', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Model: Model B (test_rpc.model_b), Field: Name (name)', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
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
                    name='test_02_delete',
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
                            value=Constant(value=' Delete: NOT NULL and ON DELETE RESTRICT constraints ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='b1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='test_rpc.model_b', kind=None),
                                    Constant(value='create', kind=None),
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='B1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='b2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='test_rpc.model_b', kind=None),
                                    Constant(value='create', kind=None),
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='B2', kind=None)],
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
                                    attr='rpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='test_rpc.model_a', kind=None),
                                    Constant(value='create', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='field_b1', kind=None),
                                            Constant(value='field_b2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='A1', kind=None),
                                            Name(id='b1', ctx=Load()),
                                            Name(id='b2', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
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
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='rpc',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='test_rpc.model_b', kind=None),
                                                    Constant(value='unlink', kind=None),
                                                    Name(id='b1', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Raise(exc=None, cause=None),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='The operation cannot be completed:', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='another model requires the record being deleted. If possible, archive it instead.', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Model: Model A (test_rpc.model_a), Constraint: test_rpc_model_a_field_b1_fkey', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
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
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='rpc',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='test_rpc.model_b', kind=None),
                                                    Constant(value='unlink', kind=None),
                                                    Name(id='b2', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Raise(exc=None, cause=None),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='The operation cannot be completed:', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=' another model requires the record being deleted. If possible, archive it instead.', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
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
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Model: Model A (test_rpc.model_a), Constraint: test_rpc_model_a_field_b2_fkey', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='faultString',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
