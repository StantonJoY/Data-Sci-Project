Module(
    body=[
        Expr(
            value=Constant(value='\nStore database-specific configuration parameters\n', kind=None),
        ),
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='ormcache', asname=None),
                alias(name='mute_logger', asname=None),
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
        Expr(
            value=Constant(value='\nA dictionary holding some configuration parameters to be initialized when the database is created.\n', kind=None),
        ),
        Assign(
            targets=[Name(id='_default_parameters', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='database.secret', kind=None),
                    Constant(value='database.uuid', kind=None),
                    Constant(value='database.create_date', kind=None),
                    Constant(value='web.base.url', kind=None),
                    Constant(value='base.login_cooldown_after', kind=None),
                    Constant(value='base.login_cooldown_duration', kind=None),
                ],
                values=[
                    Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='uuid', ctx=Load()),
                                        attr='uuid4',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='uuid', ctx=Load()),
                                        attr='uuid1',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    Attribute(
                        value=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        attr='now',
                        ctx=Load(),
                    ),
                    Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=BinOp(
                            left=Constant(value='http://localhost:%s', kind=None),
                            op=Mod(),
                            right=Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='http_port', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ),
                    Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=Constant(value=10, kind=None),
                    ),
                    Lambda(
                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=Constant(value=60, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrConfigParameter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Per-database storage of configuration key-value pairs.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.config_parameter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='System Parameter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='key', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='key', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='key_uniq', kind=None),
                                    Constant(value='unique (key)', kind=None),
                                    Constant(value='Key must be unique.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Initializes the parameters listed in _default_parameters.\n        It overrides existing parameters if force is ``True``.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prefetch_fields',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='func', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='_default_parameters', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='key', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='key', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='force', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='params', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='params', ctx=Load()),
                                                    attr='set_param',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='key', ctx=Load()),
                                                    Call(
                                                        func=Name(id='func', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.base.models.ir_config_parameter', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_param',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Retrieve the value for a given key.\n\n        :param string key: The key of the parameter value to retrieve.\n        :param string default: default value if parameter is missing.\n        :return: The value of the parameter, or ``default`` if it does not exist.\n        :rtype: string\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='key', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='default', ctx=Load()),
                                ],
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
                    name='_get_param',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='key', kind=None),
                                            Constant(value='value', kind=None),
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
                                    Constant(value='SELECT value FROM ir_config_parameter WHERE key = %s', kind=None),
                                    List(
                                        elts=[Name(id='key', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
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
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='result', ctx=Load()),
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Name(id='ormcache', ctx=Load()),
                            args=[Constant(value='key', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_param',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Sets the value of a parameter.\n\n        :param string key: The key of the parameter value to set.\n        :param string value: The value to set.\n        :return: the previous value of the parameter or False if it did\n                 not exist.\n        :rtype: string\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='param', ctx=Store())],
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
                                                    Constant(value='key', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='key', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='param', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='old', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='param', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='value', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='old', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='param', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='value', kind=None)],
                                                                values=[Name(id='value', ctx=Load())],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='param', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Name(id='old', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='key', kind=None),
                                                            Constant(value='value', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='key', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrConfigParameter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrConfigParameter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrConfigParameter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
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
