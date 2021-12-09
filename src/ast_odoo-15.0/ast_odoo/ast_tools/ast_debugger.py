Module(
    body=[
        Import(
            names=[alias(name='importlib', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='types', asname=None)],
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
            targets=[Name(id='SUPPORTED_DEBUGGER', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value='pdb', kind=None),
                    Constant(value='ipdb', kind=None),
                    Constant(value='wdb', kind=None),
                    Constant(value='pudb', kind=None),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='post_mortem',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='config', annotation=None, type_comment=None),
                    arg(arg='info', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Subscript(
                                value=Name(id='config', ctx=Load()),
                                slice=Constant(value='dev_mode', kind=None),
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='types', ctx=Load()),
                                        attr='TracebackType',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='debug', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='opt', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='opt', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='config', ctx=Load()),
                                                    slice=Constant(value='dev_mode', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='opt', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='SUPPORTED_DEBUGGER', ctx=Load())],
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
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='debug', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='importlib', ctx=Load()),
                                                            attr='import_module',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='debug', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='post_mortem',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ImportError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Error while importing %s.', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='debug', ctx=Load()),
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
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
