Module(
    body=[
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
                        keys=[Constant(value='E8503', kind=None)],
                        values=[
                            Tuple(
                                elts=[
                                    Constant(value='Raise inside unlink override.', kind=None),
                                    Constant(value='raise-unlink-override', kind=None),
                                    Constant(value='Raising errors is not allowed inside unlink overrides, you can create a method and decorate it with @api.ondelete(at_uninstall=False), only use at_uninstall=True if you know what you are doing.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_inherits_BaseModel',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='node', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='n', ctx=Load()),
                                                    Constant(value='name', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='BaseModel', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='ancestors',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='visit_raise',
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
                        Assign(
                            targets=[Name(id='parent', ctx=Store())],
                            value=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='parent',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='parent', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='parent', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='astroid', ctx=Load()),
                                                        attr='FunctionDef',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='parent', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='unlink', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='parent', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='parent',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='parent', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='astroid', ctx=Load()),
                                                                attr='ClassDef',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_inherits_BaseModel',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='parent', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='add_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='raise-unlink-override', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='node',
                                                                value=Name(id='node', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='parent', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='parent', ctx=Load()),
                                        attr='parent',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
