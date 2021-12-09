Module(
    body=[
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='astroid', asname=None)],
        ),
        ImportFrom(
            module='pylint',
            names=[
                alias(name='checkers', asname=None),
                alias(name='interfaces', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='OdooBaseChecker',
            bases=[
                Attribute(
                    value=Name(id='checkers', ctx=Load()),
                    attr='BaseChecker',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='__implements__', ctx=Store())],
                    value=Attribute(
                        value=Name(id='interfaces', ctx=Load()),
                        attr='IAstroidChecker',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value='odoo', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='msgs', ctx=Store())],
                    value=Dict(
                        keys=[Constant(value='E8502', kind=None)],
                        values=[
                            Tuple(
                                elts=[
                                    Constant(value='Bad usage of _, _lt function.', kind=None),
                                    Constant(value='gettext-variable', kind=None),
                                    Constant(value='See https://www.odoo.com/documentation/15.0/developer/misc/i18n/translations.html#variables', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='visit_call',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='node', annotation=None, type_comment=None),
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
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='func',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='Name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='func',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='_', kind=None),
                                                    Constant(value='_lt', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='first_arg', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='first_arg', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='astroid', ctx=Load()),
                                                            attr='Const',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='first_arg', ctx=Load()),
                                                            attr='value',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='str', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_message',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='gettext-variable', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='node',
                                                        value=Name(id='node', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Attribute(
                                    value=Name(id='checkers', ctx=Load()),
                                    attr='utils',
                                    ctx=Load(),
                                ),
                                attr='check_messages',
                                ctx=Load(),
                            ),
                            args=[Constant(value='gettext-variable', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='register',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='linter', annotation=None, type_comment=None)],
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
                            value=Name(id='linter', ctx=Load()),
                            attr='register_checker',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='OdooBaseChecker', ctx=Load()),
                                args=[Name(id='linter', ctx=Load())],
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
    type_ignores=[],
)
