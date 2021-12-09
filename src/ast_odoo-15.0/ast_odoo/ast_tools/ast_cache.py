Module(
    body=[
        ImportFrom(
            module='collections',
            names=[
                alias(name='Counter', asname=None),
                alias(name='defaultdict', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='decorator',
            names=[alias(name='decorator', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='inspect',
            names=[alias(name='signature', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Assign(
            targets=[Name(id='unsafe_eval', ctx=Store())],
            value=Name(id='eval', ctx=Load()),
            type_comment=None,
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
            name='ormcache_counter',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Statistic counters for cache entries. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='hit', kind=None),
                            Constant(value='miss', kind=None),
                            Constant(value='err', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
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
                                    attr='hit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='miss',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='err',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ratio',
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
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=100.0, kind=None),
                                    op=Mult(),
                                    right=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hit',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Div(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='hit',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='miss',
                                                ctx=Load(),
                                            ),
                                        ),
                                        Constant(value=1, kind=None),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='STAT', ctx=Store())],
            value=Call(
                func=Name(id='defaultdict', ctx=Load()),
                args=[Name(id='ormcache_counter', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ormcache',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' LRU cache decorator for model methods.\n    The parameters are strings that represent expressions referring to the\n    signature of the decorated method, and are used to compute a cache key::\n\n        @ormcache(\'model_name\', \'mode\')\n        def _compute_domain(self, model_name, mode="read"):\n            ...\n\n    For the sake of backward compatibility, the decorator supports the named\n    parameter `skiparg`::\n\n        @ormcache(skiparg=1)\n        def _compute_domain(self, model_name, mode="read"):\n            ...\n\n    Methods implementing this decorator should never return a Recordset,\n    because the underlying cursor will eventually be closed and raise a\n    `psycopg2.OperationalError`.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='skiparg',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='skiparg', kind=None)],
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
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
                        ],
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
                                    attr='method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='method', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='determine_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lookup', ctx=Store())],
                            value=Call(
                                func=Name(id='decorator', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lookup',
                                        ctx=Load(),
                                    ),
                                    Name(id='method', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lookup', ctx=Load()),
                                    attr='clear_cache',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='clear',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='lookup', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='determine_key',
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
                            value=Constant(value=' Determine the function that computes a cache key from arguments. ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='skiparg',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='signature', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='method',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='code', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='lambda %s: (%s,)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='args', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Constant(value=', ', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='code', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='lambda %s: ()', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='args', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='key',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='unsafe_eval', ctx=Load()),
                                        args=[Name(id='code', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='key',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[],
                                            vararg=arg(arg='args', annotation=None, type_comment=None),
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                            defaults=[],
                                        ),
                                        body=Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Slice(
                                                lower=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='skiparg',
                                                    ctx=Load(),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='lru',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Subscript(
                                value=Name(id='STAT', ctx=Load()),
                                slice=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='pool',
                                                ctx=Load(),
                                            ),
                                            attr='db_name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='pool',
                                            ctx=Load(),
                                        ),
                                        attr='_Registry__cache',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='method',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='counter', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='lookup',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='d', ctx=Store()),
                                        Name(id='key0', ctx=Store()),
                                        Name(id='counter', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lru',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=BinOp(
                                left=Name(id='key0', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Starred(
                                            value=Name(id='args', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg=None,
                                            value=Name(id='kwargs', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='d', ctx=Load()),
                                        slice=Name(id='key', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='counter', ctx=Load()),
                                        attr='hit',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Return(
                                    value=Name(id='r', ctx=Load()),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='counter', ctx=Load()),
                                                attr='miss',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                        Assign(
                                            targets=[
                                                Name(id='value', ctx=Store()),
                                                Subscript(
                                                    value=Name(id='d', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='method',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='value', ctx=Load()),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='TypeError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='cache lookup error on %r', kind=None),
                                                    Name(id='key', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='exc_info',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='counter', ctx=Load()),
                                                attr='err',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='method',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
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
                    name='clear',
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
                        Expr(
                            value=Constant(value=' Clear the registry cache ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='pool',
                                        ctx=Load(),
                                    ),
                                    attr='_clear_cache',
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
        ClassDef(
            name='ormcache_context',
            bases=[Name(id='ormcache', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' This LRU cache decorator is a variant of :class:`ormcache`, with an\n    extra parameter ``keys`` that defines a sequence of dictionary keys. Those\n    keys are looked up in the ``context`` parameter and combined to the cache\n    key made by :class:`ormcache`.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ormcache_context', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='keys',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='kwargs', ctx=Load()),
                                slice=Constant(value='keys', kind=None),
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
                    name='determine_key',
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
                            value=Constant(value=' Determine the function that computes a cache key from arguments. ', kind=None),
                        ),
                        Assert(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='skiparg',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            msg=Constant(value='ormcache_context() no longer supports skiparg', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=Call(
                                func=Name(id='signature', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='method',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='sign', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cont_expr', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='context', kind=None),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='sign', ctx=Load()),
                                            attr='parameters',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Constant(value='(context or {})', kind=None),
                                orelse=Constant(value='self._context', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keys_expr', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='tuple(%s.get(k) for k in %r)', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='cont_expr', ctx=Load()),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='args',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='lambda %s: (%s, %s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='args', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value=', ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Name(id='keys_expr', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='lambda %s: (%s,)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='args', ctx=Load()),
                                                Name(id='keys_expr', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='key',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='unsafe_eval', ctx=Load()),
                                args=[Name(id='code', ctx=Load())],
                                keywords=[],
                            ),
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
            name='ormcache_multi',
            bases=[Name(id='ormcache', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' This LRU cache decorator is a variant of :class:`ormcache`, with an\n    extra parameter ``multi`` that gives the name of a parameter. Upon call, the\n    corresponding argument is iterated on, and every value leads to a cache\n    entry under its own key.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ormcache_multi', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='multi',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='kwargs', ctx=Load()),
                                slice=Constant(value='multi', kind=None),
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
                    name='determine_key',
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
                            value=Constant(value=' Determine the function that computes a cache key from arguments. ', kind=None),
                        ),
                        Assert(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='skiparg',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            msg=Constant(value='ormcache_multi() no longer supports skiparg', kind=None),
                        ),
                        Assert(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='multi',
                                        ctx=Load(),
                                    ),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            msg=Constant(value='ormcache_multi() parameter multi must be an argument name', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ormcache_multi', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='determine_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=Call(
                                func=Name(id='signature', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='method',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='sign', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code_multi', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='lambda %s: %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='args', ctx=Load()),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='multi',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='key_multi',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='unsafe_eval', ctx=Load()),
                                args=[Name(id='code_multi', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='multi_pos',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='sign', ctx=Load()),
                                                attr='parameters',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='index',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='multi',
                                        ctx=Load(),
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
                    name='lookup',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='method', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='d', ctx=Store()),
                                        Name(id='key0', ctx=Store()),
                                        Name(id='counter', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lru',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_key', ctx=Store())],
                            value=BinOp(
                                left=Name(id='key0', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Starred(
                                            value=Name(id='args', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg=None,
                                            value=Name(id='kwargs', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='key_multi',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='missed', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Name(id='ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='base_key', ctx=Load()),
                                        op=Add(),
                                        right=Tuple(
                                            elts=[Name(id='i', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='d', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='counter', ctx=Load()),
                                                attr='hit',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Name(id='counter', ctx=Load()),
                                                        attr='miss',
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='missed', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='i', ctx=Load())],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='missed', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='args', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='args', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='multi_pos',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='missed', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='method', ctx=Load()),
                                                args=[
                                                    Starred(
                                                        value=Name(id='args', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Name(id='missed', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='key', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='base_key', ctx=Load()),
                                                op=Add(),
                                                right=Tuple(
                                                    elts=[Name(id='i', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='d', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
            name='dummy_cache',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Cache decorator replacement to actually do no caching. ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='l', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fn', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='fn', ctx=Load()),
                                    attr='clear_cache',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='clear',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='fn', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='l', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='log_ormcache_stats',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='sig', annotation=None, type_comment=None),
                    arg(arg='frame', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Log statistics of ormcache usage by database, model, and method. ', kind=None),
                ),
                ImportFrom(
                    module='odoo.modules.registry',
                    names=[alias(name='Registry', asname=None)],
                    level=0,
                ),
                Import(
                    names=[alias(name='threading', asname=None)],
                ),
                Assign(
                    targets=[Name(id='me', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='threading', ctx=Load()),
                            attr='currentThread',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='me_dbname', ctx=Store())],
                    value=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='me', ctx=Load()),
                            Constant(value='dbname', kind=None),
                            Constant(value='n/a', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='dbname', ctx=Store()),
                            Name(id='reg', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='Registry', ctx=Load()),
                                            attr='registries',
                                            ctx=Load(),
                                        ),
                                        attr='d',
                                        ctx=Load(),
                                    ),
                                    attr='items',
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
                                    value=Name(id='me', ctx=Load()),
                                    attr='dbname',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='dbname', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='entries', ctx=Store())],
                            value=Call(
                                func=Name(id='Counter', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='k', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='k', ctx=Store()),
                                                iter=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='reg', ctx=Load()),
                                                        attr='_Registry__cache',
                                                        ctx=Load(),
                                                    ),
                                                    attr='d',
                                                    ctx=Load(),
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
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='entries', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='key', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='key', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='key', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='__name__',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='model', ctx=Store()),
                                                Name(id='method', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='key', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='stat', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='STAT', ctx=Load()),
                                        slice=Tuple(
                                            elts=[
                                                Name(id='dbname', ctx=Load()),
                                                Name(id='model', ctx=Load()),
                                                Name(id='method', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='%6d entries, %6d hit, %6d miss, %6d err, %4.1f%% ratio, for %s.%s', kind=None),
                                            Subscript(
                                                value=Name(id='entries', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='stat', ctx=Load()),
                                                attr='hit',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='stat', ctx=Load()),
                                                attr='miss',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='stat', ctx=Load()),
                                                attr='err',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='stat', ctx=Load()),
                                                attr='ratio',
                                                ctx=Load(),
                                            ),
                                            Name(id='model', ctx=Load()),
                                            Attribute(
                                                value=Name(id='method', ctx=Load()),
                                                attr='__name__',
                                                ctx=Load(),
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
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='me', ctx=Load()),
                            attr='dbname',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='me_dbname', ctx=Load()),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_cache_key_counter',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='bound_method', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the cache, key and stat counter for the given call. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='model', ctx=Store())],
                    value=Attribute(
                        value=Name(id='bound_method', ctx=Load()),
                        attr='__self__',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ormcache', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='bound_method', ctx=Load()),
                            attr='clear_cache',
                            ctx=Load(),
                        ),
                        attr='__self__',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='cache', ctx=Store()),
                                Name(id='key0', ctx=Store()),
                                Name(id='counter', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ormcache', ctx=Load()),
                            attr='lru',
                            ctx=Load(),
                        ),
                        args=[Name(id='model', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='key', ctx=Store())],
                    value=BinOp(
                        left=Name(id='key0', ctx=Load()),
                        op=Add(),
                        right=Call(
                            func=Attribute(
                                value=Name(id='ormcache', ctx=Load()),
                                attr='key',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='model', ctx=Load()),
                                Starred(
                                    value=Name(id='args', ctx=Load()),
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg=None,
                                    value=Name(id='kwargs', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='cache', ctx=Load()),
                            Name(id='key', ctx=Load()),
                            Name(id='counter', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='cache', ctx=Store())],
            value=Name(id='ormcache', ctx=Load()),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
