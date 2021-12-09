Module(
    body=[
        Expr(
            value=Constant(value=' View validation code (using assertions, not the RNG schema). ', kind=None),
        ),
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
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
            targets=[Name(id='_validators', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='collections', ctx=Load()),
                    attr='defaultdict',
                    ctx=Load(),
                ),
                args=[Name(id='list', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_relaxng_cache', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='READONLY', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\\breadonly\\b', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_get_attrs_symbols',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Return a set of predefined symbols for evaluating attrs. ', kind=None),
                ),
                Return(
                    value=Set(
                        elts=[
                            Constant(value='True', kind=None),
                            Constant(value='False', kind=None),
                            Constant(value='None', kind=None),
                            Constant(value='self', kind=None),
                            Constant(value='id', kind=None),
                            Constant(value='uid', kind=None),
                            Constant(value='context', kind=None),
                            Constant(value='context_today', kind=None),
                            Constant(value='active_id', kind=None),
                            Constant(value='active_ids', kind=None),
                            Constant(value='allowed_company_ids', kind=None),
                            Constant(value='current_company_id', kind=None),
                            Constant(value='active_model', kind=None),
                            Constant(value='time', kind=None),
                            Constant(value='datetime', kind=None),
                            Constant(value='relativedelta', kind=None),
                            Constant(value='current_date', kind=None),
                            Constant(value='today', kind=None),
                            Constant(value='now', kind=None),
                            Constant(value='abs', kind=None),
                            Constant(value='len', kind=None),
                            Constant(value='bool', kind=None),
                            Constant(value='float', kind=None),
                            Constant(value='str', kind=None),
                            Constant(value='unicode', kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_variable_names',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='expr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the subexpressions of the kind "VARNAME(.ATTNAME)*" in the given\n    string or AST node.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='IGNORED', ctx=Store())],
                    value=Call(
                        func=Name(id='_get_attrs_symbols', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='names', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_name_seq',
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
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load()),
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
                                    value=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='node', ctx=Load()),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Attribute',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='left', ctx=Store())],
                                            value=Call(
                                                func=Name(id='get_name_seq', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='left', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='left', ctx=Load()),
                                                        op=Add(),
                                                        right=List(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='attr',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process',
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
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='get_name_seq', ctx=Load()),
                                args=[Name(id='node', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='seq', ctx=Load()),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='seq', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='IGNORED', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='names', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='.', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='seq', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                For(
                                    target=Name(id='child', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='ast', ctx=Load()),
                                            attr='iter_child_nodes',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='process', ctx=Load()),
                                                args=[Name(id='child', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='ast', ctx=Load()),
                                        attr='parse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='expr', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='mode',
                                            value=Constant(value='eval', kind=None),
                                        ),
                                    ],
                                ),
                                attr='body',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='process', ctx=Load()),
                        args=[Name(id='expr', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='names', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_dict_asts',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='expr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Check that the given string or AST node represents a dict expression\n    where all keys are string literals, and return it as a dict mapping string\n    keys to the AST of values.\n    ', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='ast', ctx=Load()),
                                        attr='parse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='expr', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='mode',
                                            value=Constant(value='eval', kind=None),
                                        ),
                                    ],
                                ),
                                attr='body',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='expr', ctx=Load()),
                                Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='Dict',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='Non-dict expression', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='all', ctx=Load()),
                            args=[
                                GeneratorExp(
                                    elt=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='key', ctx=Load()),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Str',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='key', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='expr', ctx=Load()),
                                                attr='keys',
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
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='Non-string literal dict key', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=DictComp(
                        key=Attribute(
                            value=Name(id='key', ctx=Load()),
                            attr='s',
                            ctx=Load(),
                        ),
                        value=Name(id='val', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='key', ctx=Store()),
                                        Name(id='val', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Name(id='zip', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='expr', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='expr', ctx=Load()),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_check',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='condition', annotation=None, type_comment=None),
                    arg(arg='explanation', annotation=None, type_comment=None),
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
                        operand=Name(id='condition', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Expression is not a valid domain: %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='explanation', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_domain_identifiers',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='expr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Check that the given string or AST node represents a domain expression,\n    and return a pair of sets ``(fields, vars)`` where ``fields`` are the field\n    names on the left-hand side of conditions, and ``vars`` are the variable\n    names on the right-hand side of conditions.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='expr', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='ast', ctx=Load()),
                                        attr='parse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='expr', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='mode',
                                            value=Constant(value='eval', kind=None),
                                        ),
                                    ],
                                ),
                                attr='body',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='fnames', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='vnames', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='expr', ctx=Load()),
                            Attribute(
                                value=Name(id='ast', ctx=Load()),
                                attr='List',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        For(
                            target=Name(id='elem', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='expr', ctx=Load()),
                                attr='elts',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='elem', ctx=Load()),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Str',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='_check', ctx=Load()),
                                                args=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='elem', ctx=Load()),
                                                            attr='s',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='&', kind=None),
                                                                    Constant(value='|', kind=None),
                                                                    Constant(value='!', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value="logical operators should be '&', '|', or '!', found ", kind=None),
                                                            FormattedValue(
                                                                value=Attribute(
                                                                    value=Name(id='elem', ctx=Load()),
                                                                    attr='s',
                                                                    ctx=Load(),
                                                                ),
                                                                conversion=114,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='elem', ctx=Load()),
                                                Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='ast', ctx=Load()),
                                                            attr='List',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='ast', ctx=Load()),
                                                            attr='Tuple',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='_check', ctx=Load()),
                                        args=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='elem', ctx=Load()),
                                                            attr='elts',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=3, kind=None)],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    Constant(value='segments should have 3 elements, found ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='elem', ctx=Load()),
                                                                    attr='elts',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='lhs', ctx=Store()),
                                                Name(id='operator', ctx=Store()),
                                                Name(id='rhs', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='elem', ctx=Load()),
                                        attr='elts',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='_check', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='operator', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='ast', ctx=Load()),
                                                        attr='Str',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            JoinedStr(
                                                values=[
                                                    Constant(value='operator should be a string, found ', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Call(
                                                                func=Name(id='type', ctx=Load()),
                                                                args=[Name(id='operator', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='__name__',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='lhs', ctx=Load()),
                                            Attribute(
                                                value=Name(id='ast', ctx=Load()),
                                                attr='Str',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fnames', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='lhs', ctx=Load()),
                                                        attr='s',
                                                        ctx=Load(),
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
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='vnames', ctx=Load()),
                            attr='update',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Name(id='get_variable_names', ctx=Load()),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='fnames', ctx=Load()),
                            Name(id='vnames', ctx=Load()),
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
            name='valid_view',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='arch', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='pred', ctx=Store()),
                    iter=Subscript(
                        value=Name(id='_validators', ctx=Load()),
                        slice=Attribute(
                            value=Name(id='arch', ctx=Load()),
                            attr='tag',
                            ctx=Load(),
                        ),
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='check', ctx=Store())],
                            value=Call(
                                func=Name(id='pred', ctx=Load()),
                                args=[Name(id='arch', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='check', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Invalid XML: %s', kind=None),
                                            Attribute(
                                                value=Name(id='pred', ctx=Load()),
                                                attr='__doc__',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='check', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='Warning', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Invalid XML: %s', kind=None),
                                            Attribute(
                                                value=Name(id='pred', ctx=Load()),
                                                attr='__doc__',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='Warning', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='validate',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='view_types', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Registers a view-validation function for the specific view types\n    ', kind=None),
                ),
                FunctionDef(
                    name='decorator',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='fn', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='arch', ctx=Store()),
                            iter=Name(id='view_types', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='_validators', ctx=Load()),
                                                slice=Name(id='arch', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fn', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                Return(
                    value=Name(id='decorator', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='relaxng',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='view_type', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a validator for the given view type, or None. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='view_type', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[Name(id='_relaxng_cache', ctx=Load())],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
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
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='base', kind=None),
                                                    Constant(value='rng', kind=None),
                                                    BinOp(
                                                        left=Constant(value='%s_view.rng', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='view_type', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='frng', ctx=Store()),
                                ),
                            ],
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='relaxng_doc', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='parse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frng', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='_relaxng_cache', ctx=Load()),
                                                    slice=Name(id='view_type', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='RelaxNG',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='relaxng_doc', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Failed to load RelaxNG XML schema for views validation', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='_relaxng_cache', ctx=Load()),
                                                            slice=Name(id='view_type', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Subscript(
                        value=Name(id='_relaxng_cache', ctx=Load()),
                        slice=Name(id='view_type', ctx=Load()),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='schema_valid',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='arch', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Get RNG validator and validate RNG file.', kind=None),
                ),
                Assign(
                    targets=[Name(id='validator', ctx=Store())],
                    value=Call(
                        func=Name(id='relaxng', ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id='arch', ctx=Load()),
                                attr='tag',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='validator', ctx=Load()),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='validator', ctx=Load()),
                                        attr='validate',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='arch', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='error', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='validator', ctx=Load()),
                                attr='error_log',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='ustr',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='error', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='validate', ctx=Load()),
                    args=[
                        Constant(value='calendar', kind=None),
                        Constant(value='graph', kind=None),
                        Constant(value='pivot', kind=None),
                        Constant(value='search', kind=None),
                        Constant(value='tree', kind=None),
                        Constant(value='activity', kind=None),
                    ],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
