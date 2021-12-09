Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.release', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tools', asname=None)],
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
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
        Assign(
            targets=[Name(id='RPC_VERSION_1', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='server_version', kind=None),
                    Constant(value='server_version_info', kind=None),
                    Constant(value='server_serie', kind=None),
                    Constant(value='protocol_version', kind=None),
                ],
                values=[
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='release',
                            ctx=Load(),
                        ),
                        attr='version',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='release',
                            ctx=Load(),
                        ),
                        attr='version_info',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='release',
                            ctx=Load(),
                        ),
                        attr='serie',
                        ctx=Load(),
                    ),
                    Constant(value=1, kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='exp_login',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db', annotation=None, type_comment=None),
                    arg(arg='login', annotation=None, type_comment=None),
                    arg(arg='password', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Name(id='exp_authenticate', ctx=Load()),
                        args=[
                            Name(id='db', ctx=Load()),
                            Name(id='login', ctx=Load()),
                            Name(id='password', ctx=Load()),
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
        FunctionDef(
            name='exp_authenticate',
            args=arguments(
                posonlyargs=[],
                args=[
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
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='user_agent_env', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_agent_env', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='res_users', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            args=[Name(id='db', ctx=Load())],
                            keywords=[],
                        ),
                        slice=Constant(value='res.users', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res_users', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='db', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                    Name(id='password', ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='interactive', kind=None),
                                        ],
                                        values=[
                                            Name(id='user_agent_env', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
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
                                Return(
                                    value=Constant(value=False, kind=None),
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
            name='exp_version',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Name(id='RPC_VERSION_1', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_about',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='extended', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Return information about the OpenERP Server.\n\n    @param extended: if True then return version info\n    @return string if extended is False else tuple\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='info', ctx=Store())],
                    value=Call(
                        func=Name(id='_', ctx=Load()),
                        args=[Constant(value='See http://openerp.com', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='extended', ctx=Load()),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='info', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='release',
                                            ctx=Load(),
                                        ),
                                        attr='version',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='info', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_set_loglevel',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='loglevel', annotation=None, type_comment=None),
                    arg(arg='logger', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='dispatch',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='params', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='g', ctx=Store())],
                    value=Call(
                        func=Name(id='globals', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='exp_method_name', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='exp_', kind=None),
                        op=Add(),
                        right=Name(id='method', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='exp_method_name', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='g', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Subscript(
                                    value=Name(id='g', ctx=Load()),
                                    slice=Name(id='exp_method_name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='params', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Method not found: %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='method', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
