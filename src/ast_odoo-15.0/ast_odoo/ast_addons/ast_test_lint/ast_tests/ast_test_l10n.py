Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='lint_case', asname=None)],
            level=1,
        ),
        ClassDef(
            name='L10nChecker',
            bases=[
                Attribute(
                    value=Name(id='lint_case', ctx=Load()),
                    attr='NodeVisitor',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='matches_tagged',
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
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load()),
                                    Attribute(
                                        value=Name(id='ast', ctx=Load()),
                                        attr='Call',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='func',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Attribute',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='func',
                                                        ctx=Load(),
                                                    ),
                                                    attr='attr',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='tagged', kind=None)],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='func',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='func',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='tagged', kind=None)],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='visit_ClassDef',
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
                            targets=[Name(id='tags', ctx=Store())],
                            value=SetComp(
                                elt=Attribute(
                                    value=Name(id='arg', ctx=Load()),
                                    attr='value',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='deco', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='decorator_list',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Name(id='arg', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='deco', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='matches_tagged',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='deco', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Set(
                                                        elts=[
                                                            Constant(value='post_install_l10n', kind=None),
                                                            Constant(value='external_l10n', kind=None),
                                                        ],
                                                    ),
                                                    op=BitAnd(),
                                                    right=Name(id='tags', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='post_install_l10n', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='post_install', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='external_l10n', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='external', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='external_l10n', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='external', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='tags', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[Name(id='node', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
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
            name='L10nLinter',
            bases=[
                Attribute(
                    value=Name(id='lint_case', ctx=Load()),
                    attr='LintCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_l10n_test_tags',
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
                            targets=[Name(id='checker', ctx=Store())],
                            value=Call(
                                func=Name(id='L10nChecker', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rs', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_module_files',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='**/l10n_*/tests/*.py', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='t', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ast', ctx=Load()),
                                                    attr='parse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='f', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Name(id='path', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rs', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='itertools', ctx=Load()),
                                                            attr='repeat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='relpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='checker', ctx=Load()),
                                                            attr='visit',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='t', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rs', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='t', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='t', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='rs', ctx=Load()),
                            ),
                            msg=BinOp(
                                left=Constant(value='missing `post_install_l10n` tag at\n', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value='\n', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        GeneratorExp(
                                            elt=BinOp(
                                                left=Constant(value='- %s:%d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='path', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='lineno',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='path', ctx=Store()),
                                                            Name(id='node', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Name(id='rs', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
