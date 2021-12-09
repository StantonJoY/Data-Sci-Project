Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
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
            targets=[Name(id='_flanker_lib_warning', ctx=Store())],
            value=Constant(value=False, kind=None),
            type_comment=None,
        ),
        Try(
            body=[
                ImportFrom(
                    module='flanker.addresslib',
                    names=[alias(name='address', asname=None)],
                    level=0,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='flanker.addresslib.validate', kind=None)],
                                keywords=[],
                            ),
                            attr='setLevel',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='ERROR',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                FunctionDef(
                    name='mail_validate',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='email', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='address', ctx=Load()),
                                            attr='validate_address',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='email', ctx=Load())],
                                        keywords=[],
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
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        FunctionDef(
                            name='mail_validate',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='email', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Global(names=['_flanker_lib_warning']),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='_flanker_lib_warning', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='_flanker_lib_warning', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="The `flanker` Python module is not installed,so email validation fallback to email_normalize. Use 'pip install flanker' to install it", kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_normalize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='email', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
    ],
    type_ignores=[],
)
