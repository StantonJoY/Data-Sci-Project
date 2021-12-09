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
            name='OnchangeChecker',
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
                    name='matches_onchange',
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
                                                comparators=[Constant(value='onchange', kind=None)],
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
                                                comparators=[Constant(value='onchange', kind=None)],
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
                    name='visit_FunctionDef',
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
                            targets=[Name(id='walker', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='map', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='matches_onchange',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='decorator_list',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='ast', ctx=Load()),
                                        attr='walk',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='node', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='islice',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='n', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Name(id='walker', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='n', ctx=Load()),
                                                                            Call(
                                                                                func=Name(id='getattr', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='ast', ctx=Load()),
                                                                                    Constant(value='Str', kind=None),
                                                                                    Call(
                                                                                        func=Name(id='type', ctx=Load()),
                                                                                        args=[Constant(value=None, kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            attr='s',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='domain', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='n', ctx=Load()),
                                                                            Call(
                                                                                func=Name(id='getattr', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='ast', ctx=Load()),
                                                                                    Constant(value='Constant', kind=None),
                                                                                    Call(
                                                                                        func=Name(id='type', ctx=Load()),
                                                                                        args=[Constant(value=None, kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            attr='value',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='domain', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=1, kind=None),
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
        ClassDef(
            name='TestOnchangeDomains',
            bases=[
                Attribute(
                    value=Name(id='lint_case', ctx=Load()),
                    attr='LintCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Would ideally have been a pylint module but that's slow as molasses\n    (takes minutes to run, and can blow up entirely depending on the pylint\n    version)\n    ", kind=None),
                ),
                FunctionDef(
                    name='test_forbid_domains_in_onchanges',
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
                            value=Constant(value=' Dynamic domains (returning a domain from an onchange) are deprecated\n        and should not be used in "standard" Odoo anymore\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='checker', ctx=Store())],
                            value=Call(
                                func=Name(id='OnchangeChecker', ctx=Load()),
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
                                args=[Constant(value='*.py', kind=None)],
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
                                left=Constant(value='probable domains in onchanges at\n', kind=None),
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
