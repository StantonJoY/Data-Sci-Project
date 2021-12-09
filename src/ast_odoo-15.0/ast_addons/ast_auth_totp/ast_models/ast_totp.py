Module(
    body=[
        Import(
            names=[alias(name='hmac', asname=None)],
        ),
        Import(
            names=[alias(name='struct', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Assign(
            targets=[Name(id='TOTP_SECRET_SIZE', ctx=Store())],
            value=Constant(value=160, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ALGORITHM', ctx=Store())],
            value=Constant(value='sha1', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DIGITS', ctx=Store())],
            value=Constant(value=6, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TIMESTEP', ctx=Store())],
            value=Constant(value=30, kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='TOTP',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_key',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='key', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='match',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='t', annotation=None, type_comment=None),
                            arg(arg='window', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Name(id='TIMESTEP', ctx=Load()),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param code: authenticator code to check against this key\n        :param int t: current timestamp (seconds)\n        :param int window: fuzz window to account for slow fingers, network\n                           latency, desynchronised clocks, ..., every code\n                           valid between t-window an t+window is considered\n                           valid\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='t', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='low', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='t', ctx=Load()),
                                            op=Sub(),
                                            right=Name(id='window', ctx=Load()),
                                        ),
                                        op=Div(),
                                        right=Name(id='TIMESTEP', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='high', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Name(id='t', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='window', ctx=Load()),
                                            ),
                                            op=Div(),
                                            right=Name(id='TIMESTEP', ctx=Load()),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='counter', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='counter', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[
                                                        Name(id='low', ctx=Load()),
                                                        Name(id='high', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='hotp', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_key',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='counter', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='code', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
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
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='hotp',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='secret', annotation=None, type_comment=None),
                    arg(arg='counter', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='C', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='struct', ctx=Load()),
                            attr='pack',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='>Q', kind=None),
                            Name(id='counter', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mac', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='hmac', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='secret', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Name(id='C', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='digestmod',
                                        value=Name(id='ALGORITHM', ctx=Load()),
                                    ),
                                ],
                            ),
                            attr='digest',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='offset', ctx=Store())],
                    value=BinOp(
                        left=Subscript(
                            value=Name(id='mac', ctx=Load()),
                            slice=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            ctx=Load(),
                        ),
                        op=BitAnd(),
                        right=Constant(value=15, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='code', ctx=Store())],
                    value=BinOp(
                        left=Subscript(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='struct', ctx=Load()),
                                    attr='unpack_from',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='>I', kind=None),
                                    Name(id='mac', ctx=Load()),
                                    Name(id='offset', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                        op=BitAnd(),
                        right=Constant(value=2147483647, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=BinOp(
                        left=Name(id='code', ctx=Load()),
                        op=Mod(),
                        right=BinOp(
                            left=Constant(value=10, kind=None),
                            op=Pow(),
                            right=Name(id='DIGITS', ctx=Load()),
                        ),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='r', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
