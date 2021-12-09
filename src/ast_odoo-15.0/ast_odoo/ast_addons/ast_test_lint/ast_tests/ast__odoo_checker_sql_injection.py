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
        Assign(
            targets=[Name(id='DFTL_CURSOR_EXPR', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='self.env.cr', kind=None),
                    Constant(value='self._cr', kind=None),
                    Constant(value='self.cr', kind=None),
                    Constant(value='cr', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
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
                        keys=[Constant(value='E8501', kind=None)],
                        values=[
                            Tuple(
                                elts=[
                                    Constant(value='Possible SQL injection risk.', kind=None),
                                    Constant(value='sql-injection', kind=None),
                                    Constant(value='See http://www.bobby-tables.com try using execute(query, tuple(params))', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_cursor_name',
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
                            targets=[Name(id='expr_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='node_expr', ctx=Store())],
                            value=Attribute(
                                value=Name(id='node', ctx=Load()),
                                attr='expr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node_expr', ctx=Load()),
                                    Attribute(
                                        value=Name(id='astroid', ctx=Load()),
                                        attr='Attribute',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expr_list', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='node_expr', ctx=Load()),
                                                attr='attrname',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='node_expr', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='node_expr', ctx=Load()),
                                        attr='expr',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node_expr', ctx=Load()),
                                    Attribute(
                                        value=Name(id='astroid', ctx=Load()),
                                        attr='Name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expr_list', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Name(id='node_expr', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='cursor_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='.', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='cursor_name', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_allowable',
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
                        Expr(
                            value=Constant(value='\n        :type node: NodeNG\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='infered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='checkers', ctx=Load()),
                                        attr='utils',
                                        ctx=Load(),
                                    ),
                                    attr='safe_infer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='node', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='infered', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='infered', ctx=Load()),
                                                    attr='pytype',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='psycopg2', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='node', ctx=Load()),
                                    Attribute(
                                        value=Name(id='astroid', ctx=Load()),
                                        attr='Call',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='node', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='node', ctx=Load()),
                                        attr='func',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='node', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='astroid', ctx=Load()),
                                                        attr='Attribute',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='expr',
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
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='attrname',
                                                        ctx=Load(),
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='_', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='node', ctx=Load()),
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='Const',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                    name='_check_concatenation',
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
                                            Name(id='node', ctx=Load()),
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='BinOp',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='op',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='%', kind=None),
                                                    Constant(value='+', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='right',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='Tuple',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='all', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Name(id='map', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_allowable',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        attr='right',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='elts',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='right',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='astroid', ctx=Load()),
                                                        attr='Dict',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='all', ctx=Load()),
                                                            args=[
                                                                GeneratorExp(
                                                                    elt=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_allowable',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='v', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Tuple(
                                                                                elts=[
                                                                                    Name(id='_', ctx=Store()),
                                                                                    Name(id='v', ctx=Store()),
                                                                                ],
                                                                                ctx=Store(),
                                                                            ),
                                                                            iter=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='node', ctx=Load()),
                                                                                    attr='right',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='items',
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
                                                        Return(
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_allowable',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='right',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_allowable',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='left',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_concatenation',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='left',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='node', ctx=Load()),
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='Call',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                                attr='Attribute',
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
                                            attr='attrname',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='format', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='all', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='map', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_allowable',
                                                            ctx=Load(),
                                                        ),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                                List(elts=[], ctx=Load()),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=True, kind=None),
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
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_allowable',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='keyword', ctx=Load()),
                                                                attr='value',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='keyword', ctx=Store()),
                                                            iter=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        attr='keywords',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(elts=[], ctx=Load()),
                                                                ],
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
                                        Return(
                                            value=Constant(value=True, kind=None),
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
                    name='_check_sql_injection_risky',
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
                            targets=[Name(id='current_file_bname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='basename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='linter',
                                            ctx=Load(),
                                        ),
                                        attr='current_file',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
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
                                                Name(id='node', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='astroid', ctx=Load()),
                                                    attr='Call',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
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
                                                    attr='Attribute',
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
                                                attr='attrname',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='execute', kind=None),
                                                        Constant(value='executemany', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        Compare(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_cursor_name',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='func',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[In()],
                                            comparators=[Name(id='DFTL_CURSOR_EXPR', ctx=Load())],
                                        ),
                                        Compare(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[LtE()],
                                            comparators=[Constant(value=1, kind=None)],
                                        ),
                                        UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Attribute(
                                                    value=Name(id='current_file_bname', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='test_', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
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
                        Assign(
                            targets=[Name(id='is_concatenation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_concatenation',
                                    ctx=Load(),
                                ),
                                args=[Name(id='first_arg', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='is_concatenation', ctx=Load()),
                                    ),
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='first_arg', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='astroid', ctx=Load()),
                                                        attr='Name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='astroid', ctx=Load()),
                                                        attr='Subscript',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current', ctx=Store())],
                                    value=Name(id='node', ctx=Load()),
                                    type_comment=None,
                                ),
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='current', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='current', ctx=Load()),
                                                            attr='parent',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='astroid', ctx=Load()),
                                                            attr='FunctionDef',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='current', ctx=Load()),
                                                attr='parent',
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
                                        operand=Name(id='current', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='is_concatenation', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='parent', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='current', ctx=Load()),
                                        attr='parent',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='node_assign', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='parent', ctx=Load()),
                                            attr='nodes_of_class',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='astroid', ctx=Load()),
                                                attr='Assign',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='node_assign', ctx=Load()),
                                                                attr='targets',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='as_string',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='first_arg', ctx=Load()),
                                                            attr='as_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='is_concatenation', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_concatenation',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='node_assign', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='is_concatenation', ctx=Load()),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='is_concatenation', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_sql_injection_risky',
                                    ctx=Load(),
                                ),
                                args=[Name(id='node', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_message',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sql-injection', kind=None)],
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
                            args=[Constant(value='sql-injection', kind=None)],
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
